"""Build the English Godot export without changing script tokens or simulation logic.

Requires Python 3 and zstandard. Input is the original Portuguese index.pck.
Only exact string constants in locales/en.json are replaced; resource paths,
identifiers, token indices, numbers and all other resources remain intact.
"""
import json
import pathlib
import re
import struct

import zstandard


def constants(payload):
    """Read scalar Variant constants from Godot's version 101 token buffer."""
    assert payload[:4] == b"GDSC"
    assert struct.unpack_from("<I", payload, 4)[0] == 101
    data = (zstandard.ZstdDecompressor().decompress(payload[12:])
            if struct.unpack_from("<I", payload, 8)[0] else payload[12:])
    identifiers, count = struct.unpack_from("<II", data)
    offset = 16
    for _ in range(identifiers):
        length = struct.unpack_from("<I", data, offset)[0]
        offset += 4 + length * 4
    for _ in range(count):
        start = offset
        variant = struct.unpack_from("<I", data, offset)[0]
        offset += 4
        kind = variant & 255
        text = None
        if kind in (4, 21):  # String or StringName
            length = struct.unpack_from("<I", data, offset)[0]
            offset += 4
            text = data[offset:offset + length].decode()
            offset += (length + 3) // 4 * 4
        elif kind in (2, 3):
            offset += 8 if variant & 65536 else 4
        elif kind == 1:
            offset += 4
        elif kind == 0:
            pass
        elif kind in (5, 6):
            offset += 8
        elif kind in (7, 9, 20):
            offset += 16
        elif kind in (8, 10):
            offset += 12
        else:
            raise ValueError(f"Unsupported constant Variant type: {kind}")
        yield data, start, offset, text


def read_pack(data):
    assert data[:4] == b"GDPC" and struct.unpack_from("<I", data, 4)[0] == 4
    base, directory = struct.unpack_from("<QQ", data, 24)
    count = struct.unpack_from("<I", data, directory)[0]
    offset = directory + 4
    for _ in range(count):
        length = struct.unpack_from("<I", data, offset)[0]
        offset += 4
        name = data[offset:offset + length].rstrip(b"\0").decode()
        offset += length
        start, size = struct.unpack_from("<QQ", data, offset)
        flags = struct.unpack_from("<I", data, offset + 32)[0]
        offset += 36
        assert flags == 0, "Encrypted or removed entries are unsupported"
        yield name, data[base + start:base + start + size]


def translate_script(payload, translations):
    entries = list(constants(payload))
    if not entries:
        return payload
    data = entries[0][0]
    result = bytearray()
    previous = 0
    for _, start, end, text in entries:
        if text not in translations:
            continue
        replacement = translations[text].encode()
        result.extend(data[previous:start + 4])
        result.extend(struct.pack("<I", len(replacement)))
        result.extend(replacement)
        result.extend(b"\0" * (-len(replacement) % 4))
        previous = end
    if not previous:
        return payload
    result.extend(data[previous:])
    return payload[:8] + struct.pack("<I", len(result)) + zstandard.ZstdCompressor(level=9).compress(result)


def build():
    import hashlib
    root = pathlib.Path(__file__).resolve().parent.parent
    original = (root / "index.pck").read_bytes()
    translations = json.loads((root / "locales/en.json").read_text())
    assert struct.unpack_from("<Q", original, 24)[0] == 112
    for source, target in translations.items():
        # Reordered or missing placeholders would break runtime string formatting.
        placeholders = r"%(?:[-+0-9.]*[sdf]|%)|\{[^}]+\}"
        assert re.findall(placeholders, source) == re.findall(placeholders, target), source
    output = bytearray(original[:112])
    directory = bytearray()
    files = list(read_pack(original))
    directory.extend(struct.pack("<I", len(files)))
    for name, payload in files:
        if name.endswith(".gdc"):
            payload = translate_script(payload, translations)
        output.extend(b"\0" * (-len(output) % 16))
        start = len(output) - 112
        output.extend(payload)
        encoded = name.encode()
        encoded += b"\0" * (-len(encoded) % 4)
        directory.extend(struct.pack("<I", len(encoded)) + encoded)
        directory.extend(struct.pack("<QQ", start, len(payload)))
        directory.extend(hashlib.md5(payload).digest() + struct.pack("<I", 0))
    output.extend(b"\0" * (-len(output) % 16))
    struct.pack_into("<Q", output, 32, len(output))
    output.extend(directory)
    (root / "index.en.pck").write_bytes(output)
    html = root / "index.html"
    html.write_text(re.sub(r"(fileSizes\['index.en.pck'\] = )\d+",
                           lambda match: match[1] + str(len(output)), html.read_text()))
    print(f"Built index.en.pck ({len(output)} bytes)")


if __name__ == "__main__":
    build()

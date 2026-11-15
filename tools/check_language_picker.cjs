// Exercise the exported HTML bootstrap with both choices, without downloading WASM.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync('index.html', 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
async function check(language) {
 const elements = new Map();
 const element = (id) => {
  if (!elements.has(id)) elements.set(id, {
   style: {}, dataset: {}, remove() { this.removed = true; },
   removeAttribute() {}, appendChild() {},
  });
  return elements.get(id);
 };
 const buttons = ['pt-BR', 'en'].map((code) => ({
  dataset: { language: code }, addEventListener(_, callback) { this.choose = callback; },
 }));
 let starts = 0;
 let config;
 const document = {
  documentElement: {}, getElementById: element, querySelectorAll: () => buttons,
 };
 class Engine {
  constructor(value) { config = value; }
  static getMissingFeatures() { return []; }
  startGame() { starts++; return Promise.resolve(); }
 }
 vm.runInNewContext(script, { document, Engine, console });
 assert.equal(starts, 0, 'Game must wait for a language');
 buttons.find((b) => b.dataset.language === language).choose();
 await new Promise(setImmediate);
 assert.equal(starts, 1);
 assert.equal(document.documentElement.lang, language);
 assert.equal(config.mainPack, language === 'en' ? 'index.en.pck' : 'index.pck');
 assert.equal(config.fileSizes[config.mainPack], fs.statSync(config.mainPack).size);
 assert.equal(config.args[1], language === 'en' ? 'en' : 'pt_BR');
 assert.equal(element('language-picker').removed, true);
 assert.equal(document.title, language === 'en' ? 'Shackleton Station' : 'Estação Shackleton');
}
(async () => {
 await check('pt-BR');
 await check('en');
 console.log('Language selection: Portuguese and English passed.');
})();

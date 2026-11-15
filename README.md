<<<<<<< HEAD

# Shackleton Station
### Lunar Mission Simulator for Junior Astronauts

![Godot](https://img.shields.io/badge/Godot-4.7-478CBF?logo=godot-engine&logoColor=white)
![NASA Space Apps](https://img.shields.io/badge/NASA-Space%20Apps-0B3D91)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

> **One lunar mission. Six days of challenges. Every decision matters.**

**Shackleton Station** is a 2D training and evaluation simulator for junior astronauts, developed as a project for **NASA Space Apps**.

The player assumes responsibility for operating a base located on the rim of Shackleton Crater, at the Moon's south pole, facing situations inspired by real challenges of space missions.

More than a game, the proposal is to offer a tool capable of evaluating decision-making, resource management, and emergency response capabilities.

---

## Play Online

The Web version of the simulator can be accessed through GitHub Pages:

### [PLAY SHACKLETON STATION](https://arthursalesse.github.io/Projeto-Nasa-App/)

**Installing Godot is not necessary.** Simply use a compatible browser.

> Access depends on GitHub Pages being enabled in the repository.

---

## About the Project

The project was developed for the space mission simulation challenge for junior astronauts.

Its main objective is to create a training environment that allows the evaluation of important competencies for operations at a lunar base.

The simulation considers aspects such as:

- Electrical power management.
- Water production and recycling.
- Food production and storage.
- Life support systems.
- Protection against space radiation.
- Communication and navigation.
- Crew behavioral health.
- Decision-making under pressure.

The simulator uses parameters inspired by NASA technical documents and research.

**Attention:** this is an independent academic prototype, not an official system or one validated by NASA.

---

## Objectives

### General Objective

Develop an interactive simulator capable of evaluating the readiness of junior astronauts through operational situations inspired by lunar missions.

### Specific Objectives

1. Simulate the operation of a lunar base.
2. Present technical and operational problems.
3. Evaluate decisions made under pressure.
4. Monitor the consumption of essential resources.
5. Apply emergency procedures.
6. Provide educational feedback on decisions.
7. Generate a candidate readiness index.
8. Allow missions to be repeated with different scenarios.

---

## Mission Scenario

The simulation takes place at a fictional base located on the rim of **Shackleton Crater**, at the lunar south pole.

This region is relevant to space exploration because it features areas of prolonged sunlight and permanently shadowed regions that may contain ice deposits.

### Mission Configuration

| Parameter | Description |
|---|---|
| Location | Lunar south pole |
| Base | Shackleton Station |
| Simulated duration | 6 days (144 hours) |
| Approximate real duration | 5 minutes |
| Crew | 4 astronauts |
| Days 1 to 5 | Solar power generation |
| Day 6 | 24 simulated hours without solar power generation |
| Objective | Keep the base operational until the end |

The shadow period is a condition defined for the training cycle, not a universal representation of the duration of the lunar night.

---

## How It Works

During the mission, the player controls an astronaut and moves through different modules of the station.

The simulator presents alarms, emergency situations, and decisions that directly affect the operation of the base.

### Main Mechanics

**Base Exploration**

The player can move through the modules and interact with equipment.

**Decision-Making**

Each scenario presents alternatives with different consequences for the available resources.

**Emergency Procedures**

Some situations require checklists to be completed in a specific order and within a time limit.

**Resource Management**

Decisions affect energy, water, food, oxygen levels, and crew safety.

**Educational Feedback**

The simulator indicates whether the decision was correct, acceptable, or incorrect, presenting an explanation related to the space context.

---

## Emergency Scenarios

Events are organized into different operational areas.

| Area | Scenario 1 | Scenario 2 |
|---|---|---|
| Water | Water quality sensor failure | Urine processor failure |
| Food | High humidity in the greenhouse | Low oxygen in aquaponics |
| Energy | Dust on solar panels | Stuck solar tracker |
| Thermal control | Battery overheating | Ammonia leak |
| Life support | Air leak | CO₂ removal system saturation |
| Radiation | Solar storm during EVA | Solar storm with crew in the rover |
| Communication | Damaged antenna | Damaged navigation beacon |

### Micrometeoroid Impact

A special event may occur at a random moment during the mission.

The player must execute emergency procedures to isolate the impact and reduce oxygen losses.

Depending on the outcome, communication or navigation equipment may be damaged.

### 🧠 Behavioral Health

The simulator also considers situations related to the crew:

- Interpersonal conflicts.
- Sleep deprivation.
- Family news and the need for psychological support.

These events require the player to consider not only technical systems but also the well-being of the astronauts.

---

## Energy Management

One of the main challenges takes place on the sixth day of the mission.

During this period, the station must operate without solar power generation, using only stored energy.

The player must evaluate which systems can have their consumption temporarily reduced.

Manageable systems include:

- Habitat heating.
- Oxygen generator.
- Greenhouse lighting.
- Aquaponics system.
- Regolith processing.
- Battery energy reserve.

Energy autonomy depends on decisions made during the previous days.

---

## Evaluation System

At the end of the mission, the simulator calculates a **Readiness Index**, ranging from 0 to 100.

The evaluation considers the quality of decisions and the execution of procedures.

### Fibonacci Weights

The six decision positions have progressive weights:

| Position | Weight |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 5 |
| 5 | 8 |
| 6 | 13 |
| Micrometeoroid | 21 |
| **Total** | **53** |

Decisions receive the following values:

- **Correct:** 1 point proportional to the weight.
- **Acceptable:** 0.618 points proportional to the weight.
- **Incorrect:** 0 points.

The weighted score is converted into an index from 0 to 100.

### Candidate Classification

The system uses five readiness levels, with score thresholds at 21, 34, 55, and 89.

Level 1 represents the lowest classification, while level 5 corresponds to the best performance.

This classification is an evaluation mechanism of the prototype, not an official astronaut certification.

---

## Randomization and Replayability

To prevent the player from simply memorizing answers, the simulator uses randomization mechanisms.

With each new attempt:

1. One scenario is selected for each topic.
2. The order of the topics may be modified.
3. The alternatives are shuffled.
4. The micrometeoroid impact occurs at a variable time.
5. The consequences depend on previous decisions.

This encourages the player to understand the problems and develop operational reasoning.

---

## Technologies Used

| Technology | Usage |
|---|---|
| Godot Engine 4.7 | Simulator development |
| GDScript | Programming the mechanics |
| Godot Web Export | Browser execution |
| Git | Version control |
| GitHub | Repository hosting |
| GitHub Pages | Web version publishing |

---

## How to Run

### Option 1 — Play in the Browser

Access:

https://arthursalesse.github.io/Projeto-Nasa-App/

The Web version allows the simulator to run without installing Godot.

### Option 2 — Run Locally

Clone the repository:

```bash
git clone https://github.com/ArthurSalesse/Projeto-Nasa-App.git
```

Enter the directory:

```bash
cd Projeto-Nasa-App
```

If you are using the exported Web version, start a local HTTP server:

```bash
python -m http.server 8000
```

Open your browser and access:

http://localhost:8000

> To edit the project in Godot, access to the source files, including `project.godot`, is required. The exported Web files do not replace the editable project.

---

## Testing and Validation

The prototype's technical documentation records **180 automated tests**.

The tests were used to verify aspects such as:

- Functionality of the mechanics.
- Resource balancing.
- Decision processing.
- Scenario randomization.
- Final evaluation calculation.

Validation with users and specialists is still part of the project's next steps.

---

## Scientific Foundation

The simulator uses research and technical documents related to space exploration as references.

The main topics researched include:

- ISS life support systems.
- Oxygen and water consumption.
- Energy production and storage.
- Radiation protection systems.
- Lunar surface operations.
- Space communication and navigation.

### References

1. NASA — *Life Support Baseline Values and Assumptions Document (BVAD)*.
2. NASA — *Environmental Control and Life Support System (ECLSS)*.
3. NASA — *Vertical Solar Array Technology (VSAT)*.
4. NASA — *BEACON: Lunar Surface Beamed Power and Relay*.
5. NASA — *OCHMO-TB-020: Design for Ionizing Radiation Protection*.
6. NASA — *LunaNet: Lunar Networking Standards*.
7. Clowdsley — *Protecting Astronauts from Space Radiation on the Lunar Surface*.

Some parameters used in balancing are design choices made by the team and should not be interpreted as official NASA values.

---

## Funding and Sustainability

The development proposal considers three stages.

### 1. Validation

Seeking support through universities, research scholarships, and scientific initiation programs.

Potential institutions:

- CNPq.
- Fundação Araucária.
- Universities and research centers.

### 2. Product Development

Seeking funding to improve the interface, expand scenarios, and develop additional features.

Potential sources include innovation grants and technological development funding programs.

### 3. Expansion

Possibility of licensing and partnerships with:

- Training centers.
- Educational institutions.
- Science museums.
- Space training programs.

These possibilities represent future proposals, not funding or partnerships already established.

---

## Next Steps

- [ ] Conduct tests with students.
- [ ] Validate parameters with specialists.
- [ ] Expand training scenarios.
- [ ] Improve the interface and audiovisual resources.
- [ ] Implement an online ranking.
- [ ] Develop new mission cycles.
- [ ] Explore simulations of missions to Mars.
- [ ] Investigate multiplayer features.

---

## Development Team

Project developed by:

- **Arthur Salesse**
- **Giova Jovelho**
- **Eliseu Camargo**
- **Desirée Wolf**

**Project:** NASA Space Apps  
**Year:** 2026

---

## License

This project is made available under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

Third-party resources may be subject to specific licenses.

---

## Disclaimer

This is an independent academic project developed for NASA Space Apps.

The simulator uses public references from space research, but it does not represent an official NASA product and does not have certification for real astronaut training or selection.

---

<div align="center">

### Shackleton Station

**Training decisions today for the space challenges of tomorrow.**

Developed with Godot Engine.

</div>
=======
# Projeto-Nasa-App

Simulador da Estação Shackleton em Português (Brasil) e inglês.
Ao abrir o site, escolha o idioma antes de iniciar a simulação. A escolha
vale para toda a partida, incluindo alarmes, procedimentos, minijogos e avaliação.
Recarregue a página para escolher novamente.

O repositório contém a exportação web do Godot. `index.pck` é o pacote original
em português; `index.en.pck` é a versão em inglês. Sirva os arquivos por HTTP
para jogar; abrir `index.html` diretamente como arquivo não carrega o Godot.

As traduções estão em `locales/en.json`. Para reconstruir o pacote inglês,
use Python 3 com o módulo `zstandard` instalado:

```sh
python3 tools/build_english.py
node tools/check_language_picker.cjs
```

O gerador troca somente constantes de texto exatas nos scripts exportados,
preserva identificadores, tokens e recursos e atualiza o tamanho no HTML.
Não altere chaves internas, caminhos ou marcadores como `%s`, `%d` e `{poeira}`.
Os dados e a lógica da simulação são os mesmos nos dois idiomas.

Com Godot 4.7 compatível instalado, execute os 180 testes de simulação
incluídos na exportação em ambos os idiomas:

```sh
godot --headless --main-pack index.pck --script res://testes/teste_simulador.gdc
godot --headless --main-pack index.en.pck --script res://testes/teste_simulador.gdc
```
>>>>>>> d61b986 (Add Portuguese and English language selection before simulation)

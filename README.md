
# Estação Shackleton
### Simulador de Missão Lunar para Astronautas Juniores

![Godot](https://img.shields.io/badge/Godot-4.7-478CBF?logo=godot-engine&logoColor=white)
![NASA Space Apps](https://img.shields.io/badge/NASA-Space%20Apps-0B3D91)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Protótipo-yellow)

> **Uma missão lunar. Seis dias de desafios. Cada decisão importa.**

A **Estação Shackleton** é um simulador 2D de treinamento e avaliação de astronautas juniores, desenvolvido como projeto para o **NASA Space Apps**.

O jogador assume a responsabilidade de operar uma base localizada na borda da cratera Shackleton, no polo sul da Lua, enfrentando situações inspiradas em desafios reais das missões espaciais.

Mais do que um jogo, a proposta é oferecer uma ferramenta capaz de avaliar a tomada de decisões, o gerenciamento de recursos e a capacidade de resposta a emergências.

---

## Jogue Online

A versão Web do simulador pode ser acessada pelo GitHub Pages:

### [JOGAR ESTAÇÃO SHACKLETON](https://arthursalesse.github.io/Projeto-Nasa-App/)

**Não é necessário instalar o Godot.** Basta utilizar um navegador compatível.

> O acesso depende da ativação do GitHub Pages no repositório.

---

## Sobre o Projeto

O projeto foi desenvolvido para o desafio de simulação de missões espaciais para astronautas juniores.

Seu principal objetivo é criar um ambiente de treinamento que permita avaliar competências importantes para operações em uma base lunar.

A simulação considera aspectos como:

- Gerenciamento de energia elétrica.
- Produção e reciclagem de água.
- Produção e armazenamento de alimentos.
- Sistemas de suporte à vida.
- Proteção contra radiação espacial.
- Comunicação e navegação.
- Saúde comportamental da tripulação.
- Tomada de decisões sob pressão.

O simulador utiliza parâmetros inspirados em documentos técnicos e pesquisas da NASA.

**Atenção:** trata-se de um protótipo acadêmico independente, não de um sistema oficial ou validado pela NASA.

---

## Objetivos

### Objetivo Geral

Desenvolver um simulador interativo capaz de avaliar a prontidão de astronautas juniores por meio de situações operacionais inspiradas em missões lunares.

### Objetivos Específicos

1. Simular o funcionamento de uma base lunar.
2. Apresentar problemas técnicos e operacionais.
3. Avaliar decisões tomadas sob pressão.
4. Monitorar o consumo de recursos essenciais.
5. Aplicar procedimentos de emergência.
6. Fornecer feedback educativo sobre as decisões.
7. Gerar um índice de prontidão do candidato.
8. Permitir a repetição das missões com cenários diferentes.

---

## Cenário da Missão

A simulação acontece em uma base fictícia localizada na borda da **cratera Shackleton**, no polo sul lunar.

Essa região é relevante para a exploração espacial por apresentar áreas de iluminação solar prolongada e regiões permanentemente sombreadas, que podem conter depósitos de gelo.

### Configuração da Missão

| Parâmetro | Descrição |
|---|---|
| Localização | Polo sul lunar |
| Base | Estação Shackleton |
| Duração simulada | 6 dias (144 horas) |
| Duração aproximada real | 5 minutos |
| Tripulação | 4 astronautas |
| Dias 1 a 5 | Geração de energia solar |
| Dia 6 | 24 horas simuladas sem geração solar |
| Objetivo | Manter a base operacional até o final |

O período de sombra é uma condição definida para o ciclo de treinamento, não uma representação universal da duração da noite lunar.

---

## Como Funciona

Durante a missão, o jogador controla um astronauta e percorre diferentes módulos da estação.

O simulador apresenta alarmes, situações de emergência e decisões que afetam diretamente o funcionamento da base.

### Mecânicas principais

**Exploração da base**

O jogador pode percorrer os módulos e interagir com os equipamentos.

**Tomada de decisões**

Cada cenário apresenta alternativas com consequências diferentes para os recursos disponíveis.

**Procedimentos de emergência**

Algumas situações exigem a execução de checklists em uma ordem específica e dentro de um prazo.

**Gerenciamento de recursos**

As decisões afetam os níveis de energia, água, alimentos, oxigênio e segurança da tripulação.

**Feedback educativo**

O simulador informa se a decisão foi correta, aceitável ou incorreta, apresentando uma explicação relacionada ao contexto espacial.

---

## Cenários de Emergência

Os eventos são organizados em diferentes áreas operacionais.

| Área | Cenário 1 | Cenário 2 |
|---|---|---|
| Água | Falha no sensor de qualidade | Falha no processador de urina |
| Alimentação | Umidade elevada na estufa | Falta de oxigênio na aquaponia |
| Energia | Poeira nos painéis solares | Rastreador solar travado |
| Controle térmico | Superaquecimento da bateria | Vazamento de amônia |
| Suporte à vida | Vazamento de ar | Saturação do removedor de CO₂ |
| Radiação | Tempestade solar durante EVA | Tempestade solar com equipe no rover |
| Comunicação | Antena danificada | Baliza de navegação danificada |

### Impacto de Micrometeoroide

Um evento especial pode ocorrer em um momento aleatório da missão.

O jogador deve executar procedimentos de emergência para isolar o impacto e reduzir as perdas de oxigênio.

Dependendo do resultado, equipamentos de comunicação ou navegação podem ser danificados.

### 🧠 Saúde Comportamental

O simulador também considera situações relacionadas à tripulação:

- Conflitos interpessoais.
- Privação de sono.
- Notícias familiares e necessidade de apoio psicológico.

Esses eventos exigem que o jogador considere não apenas os sistemas técnicos, mas também o bem-estar dos astronautas.

---

## Gerenciamento de Energia

Um dos principais desafios acontece no sexto dia da missão.

Durante esse período, a estação precisa funcionar sem geração solar, utilizando apenas a energia armazenada.

O jogador deve avaliar quais sistemas podem ter seu consumo reduzido temporariamente.

Entre os sistemas gerenciáveis estão:

- Aquecimento do habitat.
- Gerador de oxigênio.
- Iluminação da estufa.
- Sistema de aquaponia.
- Processamento de regolito.
- Reserva de energia das baterias.

A autonomia energética depende das decisões tomadas durante os dias anteriores.

---

## Sistema de Avaliação

Ao finalizar a missão, o simulador calcula um **Índice de Prontidão**, variando de 0 a 100.

A avaliação considera a qualidade das decisões e a execução dos procedimentos.

### Pesos de Fibonacci

As seis posições de decisão possuem pesos progressivos:

| Posição | Peso |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 5 |
| 5 | 8 |
| 6 | 13 |
| Micrometeoroide | 21 |
| **Total** | **53** |

As decisões recebem os seguintes valores:

- **Correta:** 1 ponto proporcional ao peso.
- **Aceitável:** 0,618 ponto proporcional ao peso.
- **Incorreta:** 0 ponto.

A pontuação ponderada é convertida em um índice de 0 a 100.

### Classificação dos Candidatos

O sistema utiliza cinco níveis de prontidão, com limites de pontuação em 21, 34, 55 e 89.

O nível 1 representa a classificação mais baixa, enquanto o nível 5 corresponde ao melhor desempenho.

Essa classificação é um mecanismo de avaliação do protótipo, não uma certificação oficial de astronautas.

---

## Aleatoriedade e Rejogabilidade

Para evitar que o jogador apenas memorize respostas, o simulador utiliza mecanismos de aleatoriedade.

A cada nova tentativa:

1. Um cenário é selecionado para cada tema.
2. A ordem dos temas pode ser modificada.
3. As alternativas são embaralhadas.
4. O impacto de micrometeoroide ocorre em horário variável.
5. As consequências dependem das decisões anteriores.

Isso incentiva o jogador a compreender os problemas e desenvolver raciocínio operacional.

---

## Tecnologias Utilizadas

| Tecnologia | Utilização |
|---|---|
| Godot Engine 4.7 | Desenvolvimento do simulador |
| GDScript | Programação das mecânicas |
| Godot Web Export | Execução no navegador |
| Git | Controle de versão |
| GitHub | Hospedagem do repositório |
| GitHub Pages | Publicação da versão Web |

---

## Como Executar

### Opção 1 — Jogar pelo navegador

Acesse:

https://arthursalesse.github.io/Projeto-Nasa-App/

A versão Web permite executar o simulador sem instalar o Godot.

### Opção 2 — Executar localmente

Clone o repositório:

```bash
git clone https://github.com/ArthurSalesse/Projeto-Nasa-App.git
```

Entre no diretório:

```bash
cd Projeto-Nasa-App
```

Se estiver utilizando a versão Web exportada, execute um servidor HTTP local:

```bash
python -m http.server 8000
```

Abra o navegador e acesse:

http://localhost:8000

> Para editar o projeto no Godot, é necessário ter acesso aos arquivos-fonte, incluindo o `project.godot`. Os arquivos Web exportados não substituem o projeto editável.

---

## Testes e Validação

A documentação técnica do protótipo registra **180 testes automatizados**.

Os testes foram utilizados para verificar aspectos como:

- Funcionamento das mecânicas.
- Balanceamento de recursos.
- Processamento das decisões.
- Aleatoriedade dos cenários.
- Cálculo da avaliação final.

A validação com usuários e especialistas ainda faz parte dos próximos passos do projeto.

---

## Fundamentação Científica

O simulador utiliza como referência pesquisas e documentos técnicos relacionados à exploração espacial.

Entre os principais temas pesquisados estão:

- Sistemas de suporte à vida da ISS.
- Consumo de oxigênio e água.
- Produção e armazenamento de energia.
- Sistemas de proteção contra radiação.
- Operações de superfície lunar.
- Comunicação e navegação espacial.

### Referências

1. NASA — *Life Support Baseline Values and Assumptions Document (BVAD)*.
2. NASA — *Environmental Control and Life Support System (ECLSS)*.
3. NASA — *Vertical Solar Array Technology (VSAT)*.
4. NASA — *BEACON: Lunar Surface Beamed Power and Relay*.
5. NASA — *OCHMO-TB-020: Design for Ionizing Radiation Protection*.
6. NASA — *LunaNet: Lunar Networking Standards*.
7. Clowdsley — *Protecting Astronauts from Space Radiation on the Lunar Surface*.

Alguns parâmetros utilizados no balanceamento são escolhas de design da equipe e não devem ser interpretados como valores oficiais da NASA.

---

## Financiamento e Sustentabilidade

A proposta de desenvolvimento considera três etapas.

### 1. Validação

Busca de apoio por meio de universidades, bolsas de pesquisa e programas de iniciação científica.

Possíveis instituições:

- CNPq.
- Fundação Araucária.
- Universidades e centros de pesquisa.

### 2. Desenvolvimento do Produto

Busca de financiamento para aprimorar a interface, ampliar os cenários e desenvolver funcionalidades adicionais.

Possíveis fontes incluem editais de inovação e programas de fomento tecnológico.

### 3. Expansão

Possibilidade de licenciamento e parcerias com:

- Centros de treinamento.
- Instituições de ensino.
- Museus de ciência.
- Programas de formação espacial.

Essas possibilidades representam propostas futuras, não financiamentos ou parcerias já estabelecidos.

---

## Próximos Passos

- [ ] Realizar testes com estudantes.
- [ ] Validar parâmetros com especialistas.
- [ ] Ampliar os cenários de treinamento.
- [ ] Aprimorar a interface e os recursos audiovisuais.
- [ ] Implementar ranking online.
- [ ] Desenvolver novos ciclos de missão.
- [ ] Explorar simulações de missões em Marte.
- [ ] Investigar funcionalidades multiplayer.

---

## Equipe de Desenvolvimento

Projeto desenvolvido por:

- **Arthur Salesse**
- **Giova Jovelho**
- **Eliseu Camargo**
- **Desirée Wolf**

**Projeto:** NASA Space Apps  
**Ano:** 2026

---

## Licença

Este projeto está disponibilizado sob a **Licença MIT**.

Consulte o arquivo [LICENSE](LICENSE) para mais informações.

Recursos de terceiros podem estar sujeitos a licenças específicas.

---

## Aviso

Este é um projeto acadêmico independente desenvolvido para o NASA Space Apps.

O simulador utiliza referências públicas de pesquisas espaciais, mas não representa um produto oficial da NASA e não possui certificação para treinamento ou seleção real de astronautas.

---

<div align="center">

### Estação Shackleton

**Treinando decisões hoje para os desafios espaciais de amanhã.**

Desenvolvido com Godot Engine.

</div>

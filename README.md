# 🚢 Port Logistics Cost Analyzer (Santos-SP)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Ferramenta de simulação e análise de viabilidade para custos de armazenagem portuária, focada na identificação de gargalos financeiros em operações de Importação.**

---

## 💼 O Caso de Negócio (Business Case)

Em operações de comércio exterior, a previsibilidade de custos é um dos maiores desafios. Baseado em um estudo de caso real de agenciamento de carga, identificou-se a seguinte "dor" do cliente:

1.  [cite_start]**Falta de Transparência:** Clientes frequentemente solicitam tabelas para projetar custos, mas recebem apenas simulações "caso a caso" dos operadores logísticos[cite: 426, 427].
2.  **Custos Ocultos:** A complexidade das tarifas (que misturam valores fixos e percentuais) dificulta saber se uma carga pagará o valor mínimo ou uma taxa sobre o valor da mercadoria (Ad Valorem).
3.  [cite_start]**Ineficiência:** Cargas de baixo valor agregado acabam pagando tarifas desproporcionais devido às cláusulas de valor mínimo[cite: 133].

**O Objetivo:** Criar um algoritmo que automatize a decisão tarifária e gere visualizações estratégicas para suporte à decisão (Data-Driven Decision Making).

---

## ⚙️ A Solução Lógica

O script desenvolvido em Python simula o cenário tarifário do Porto de Santos, aplicando a regra de cobrança identificada nos documentos de tarifário:

$$Custo = \max(\text{Tarifa Mínima}, \text{Valor CIF} \times 0,20\%)$$

### Regras de Negócio Implementadas:
* [cite_start]**Tarifa Mínima (Floor):** R$ 781,71 (para Container 40')[cite: 133].
* [cite_start]**Ad Valorem (Variable):** 0,20% sobre o valor CIF da carga a cada período de 10 dias[cite: 133].
* **Progressividade:** O custo escala linearmente conforme o número de períodos aumenta.

---

## 📊 Insights de Dados & Visualização

O projeto utiliza `matplotlib` para gerar análises visuais que respondem a perguntas críticas de negócio.

### 1. Análise de Breakeven (Ponto de Inflexão)
Identificamos matematicamente o momento exato em que a cobrança deixa de ser fixa e passa a ser variável.

* **Zona de Ineficiência:** Para cargas com valor CIF abaixo de **R$ 390.855,00**, o cliente paga o valor fixo (R$ 781,71). Nesses casos, a taxa efetiva é **superior a 0,20%**, penalizando cargas baratas.
* **Zona de Risco:** Acima desse valor, o custo torna-se volátil e dependente da variação cambial e do valor da mercadoria.

*(Insira aqui a imagem do gráfico de linha gerado pelo código)*
`![Gráfico Breakeven](images/breakeven_chart.png)`

### 2. Simulação Anual (Combo Chart)
Simulação estocástica de um ano fiscal com variação de valores de carga.

* **Barras (Azul):** Custo mensal efetivo.
* **Linha (Vermelha):** Acumulado anual.
* **Destaque:** O algoritmo destaca visualmente os meses onde a "Cláusula Mínima" foi ativada, sinalizando oportunidades de consolidação de carga.

*(Insira aqui a imagem do gráfico de barras/linhas gerado pelo código)*
`![Gráfico Mensal](images/monthly_analysis.png)`

---

## 🧠 Conceitos Técnicos Aplicados

Este projeto demonstra competências em:

* **Threshold Analysis (Análise de Limiar):** Determinação algorítmica de pontos de mudança de regra de negócio.
* **Mock Data Generation:** Criação de dados sintéticos com distribuição controlada para validar modelos financeiros.
* **Visual Storytelling:** Uso de *Dual-Axis Charts* para correlacionar custos pontuais com tendências acumuladas.
* **Python Libraries:** `pandas` (manipulação de dados), `numpy` (cálculos vetoriais) e `matplotlib` (visualização de dados).

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Python 3.8 ou superior.

### Instalação

1. Clone o repositório:
```bash
git clone [https://github.com/SEU-USUARIO/analise-custos-portuarios-santos.git](https://github.com/SEU-USUARIO/analise-custos-portuarios-santos.git)
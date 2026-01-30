"""
Análise de Custos Portuários Mensais
Data Scientist Sênior - Logística
Regra: Custo = max(781.71, CIF * 0,20%)
"""

import matplotlib
matplotlib.use("Agg")  # Evita abrir no navegador; gráfico só é salvo em arquivo

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Patch

# ========== CONFIGURAÇÃO ==========
np.random.seed(42)

MESES = [
    "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
    "Jul", "Ago", "Set", "Out", "Nov", "Dez"
]

VALOR_MIN_CIF = 200_000
VALOR_MAX_CIF = 600_000
VALOR_MINIMO_ARMAZENAGEM = 781.71
TAXA_AD_VALOREM = 0.0020  # 0,20%

COR_AD_VALOREM = "#3498DB"
COR_VALOR_MINIMO = "#E67E22"
COR_ACUMULADO = "#C0392B"


def custo_armazenagem(valor_cif: pd.Series) -> pd.Series:
    """Custo = maior entre mínimo e ad valorem (0,20% do CIF)."""
    return np.maximum(VALOR_MINIMO_ARMAZENAGEM, valor_cif * TAXA_AD_VALOREM).round(2)


def formatar_reais(valor: float) -> str:
    """Formata valor em R$ com ponto como separador de milhar."""
    return f"R$ {valor:,.0f}".replace(",", ".")


# ========== GERAÇÃO DE DADOS (MOCK) ==========
df = pd.DataFrame({
    "Mes": MESES,
    "Valor_CIF": np.random.uniform(VALOR_MIN_CIF, VALOR_MAX_CIF, size=12).round(2)
})

df["Custo_Armazenagem"] = custo_armazenagem(df["Valor_CIF"])
df["Usou_Minimo"] = df["Custo_Armazenagem"] == VALOR_MINIMO_ARMAZENAGEM
df["Acumulado"] = df["Custo_Armazenagem"].cumsum()

# ========== VISUALIZAÇÃO (COMBO CHART) ==========
fig, ax1 = plt.subplots(figsize=(12, 6))
x = np.arange(len(df["Mes"]))
width = 0.6

cores_barras = [COR_VALOR_MINIMO if uso else COR_AD_VALOREM for uso in df["Usou_Minimo"]]
barras = ax1.bar(x - width/2, df["Custo_Armazenagem"], width, color=cores_barras,
                 edgecolor="white", linewidth=0.8)
ax1.set_xlabel("Mês", fontsize=11)
ax1.set_ylabel("Custo Mensal (R$)", fontsize=11, color=COR_AD_VALOREM)
ax1.tick_params(axis="y", labelcolor=COR_AD_VALOREM)
ax1.set_xticks(x)
ax1.set_xticklabels(df["Mes"])
ax1.yaxis.set_major_formatter(FuncFormatter(lambda v, _: formatar_reais(v)))
ax1.set_ylim(0, df["Custo_Armazenagem"].max() * 1.15)
ax1.grid(axis="y", alpha=0.3, linestyle="--")

for bar, valor in zip(barras, df["Custo_Armazenagem"]):
    ax1.annotate(formatar_reais(valor),
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                 xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                 fontsize=8, fontweight="bold", rotation=90)

ax2 = ax1.twinx()
ax2.plot(x, df["Acumulado"], color=COR_ACUMULADO, marker="o", markersize=8,
         linewidth=2, label="Custo Acumulado")
ax2.set_ylabel("Custo Acumulado (R$)", fontsize=11, color=COR_ACUMULADO)
ax2.tick_params(axis="y", labelcolor=COR_ACUMULADO)
ax2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: formatar_reais(v)))
ax2.set_ylim(0, df["Acumulado"].max() * 1.1)
ax2.legend(loc="upper right", framealpha=0.9)

for xi, yi in zip(x, df["Acumulado"]):
    ax2.annotate(formatar_reais(yi), xy=(xi, yi), xytext=(0, 6),
                 textcoords="offset points", ha="center", fontsize=8,
                 color=COR_ACUMULADO, fontweight="bold")

plt.title("Análise de Custos Portuários: Mínimo vs Ad Valorem (Ano Fiscal)",
          fontsize=14, fontweight="bold", pad=16)

ax1.legend(handles=[
    Patch(facecolor=COR_AD_VALOREM, edgecolor="white", label="Ad Valorem (0,20% CIF)"),
    Patch(facecolor=COR_VALOR_MINIMO, edgecolor="white", label=f"Valor Mínimo (R$ {VALOR_MINIMO_ARMAZENAGEM:,.2f})".replace(",", "X").replace(".", ",").replace("X", "."))
], loc="upper left", framealpha=0.9)
fig.tight_layout()

plt.savefig("analise_custos_portuarios.png", dpi=150, bbox_inches="tight",
            facecolor="white", edgecolor="none")
plt.close(fig)

# ========== RESUMO NO CONSOLE ==========
print("\n" + "=" * 60)
print("RESUMO DA ANÁLISE DE CUSTOS PORTUÁRIOS")
print("=" * 60)
print(df.to_string(index=False))
print("\n--- Regra aplicada por mês ---")
print(f"Meses com Valor Mínimo (R$ 781,71): {df['Usou_Minimo'].sum()}")
print(f"Meses com Ad Valorem (0,20% CIF):   {(~df['Usou_Minimo']).sum()}")
total = df["Custo_Armazenagem"].sum()
print(f"Custo total no ano: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print("=" * 60)
    

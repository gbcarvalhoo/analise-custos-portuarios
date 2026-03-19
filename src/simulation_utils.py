"""
simulation_utils.py
Utilitários de simulação — inclui integração com API do Banco Central
para cotação do dólar em tempo real.
"""

import requests
from datetime import datetime, timedelta


def get_dolar_hoje() -> float:
    """
    Busca a cotação de venda do dólar do dia via API do Banco Central.
    Se não houver cotação hoje (fim de semana/feriado), busca o dia anterior.
    Retorna o valor como float. Em caso de erro, retorna None.
    """
    for dias_atras in range(5):
        data = (datetime.today() - timedelta(days=dias_atras)).strftime("%m-%d-%Y")
        url = (
            f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            f"CotacaoDolarDia(dataCotacao=@dataCotacao)?"
            f"@dataCotacao='{data}'&$format=json&$select=cotacaoVenda"
        )
        try:
            response = requests.get(url, timeout=10)
            data_json = response.json()
            if data_json.get("value"):
                return float(data_json["value"][0]["cotacaoVenda"])
        except Exception:
            continue
    return None


def cif_em_reais(valor_usd: float, dolar: float = None) -> float:
    """
    Converte valor CIF de USD para BRL.
    Se dolar não for informado, busca cotação em tempo real.
    """
    if dolar is None:
        dolar = get_dolar_hoje()
    if dolar is None:
        raise ValueError("Não foi possível obter a cotação do dólar.")
    return round(valor_usd * dolar, 2)
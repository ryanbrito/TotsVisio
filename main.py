import os
from tratamento import *

def main():
    pasta_entrada = 'dados_originais'
    pasta_saida = 'dados_tratados'
    
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Lista de funções e arquivos correspondentes
    tratamentos = {
        'clientes_desde (1).csv': tratar_clientes_desde,
        'contratacoes_ultimos_12_meses.csv': tratar_contratacoes_12m,
        'dados_clientes.csv': tratar_dados_clientes,
        'dicionario.xlsx': tratar_dicionario,
        'historico.csv': tratar_historico,
        'mrr.csv': tratar_mrr,
        'nps_relacional.csv': tratar_nps_relacional,
        'nps_transacional_aquisicao.csv': tratar_nps_aquisicao,
        'nps_transacional_implantacao.csv': tratar_nps_implantacao,
        'nps_transacional_onboarding.csv': tratar_nps_onboarding,
        'nps_transacional_produto.csv': tratar_nps_produto,
        'nps_transacional_suporte.csv': tratar_nps_suporte,
        'tickets.csv': tratar_tickets,
        'telemetria_1.csv': tratar_telemetria_1,
        'telemetria_2.csv': tratar_telemetria_2,
        'telemetria_3.csv': tratar_telemetria_3,
        'telemetria_4.csv': tratar_telemetria_4,
        'telemetria_5.csv': tratar_telemetria_5,
        'telemetria_6.csv': tratar_telemetria_6,
        'telemetria_7.csv': tratar_telemetria_7,
        'telemetria_8.csv': tratar_telemetria_8,
        'telemetria_9.csv': tratar_telemetria_9,
        'telemetria_10.csv': tratar_telemetria_10,
        'telemetria_11.csv': tratar_telemetria_11
    }

    for arquivo, funcao in tratamentos.items():
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        caminho_saida = os.path.join(pasta_saida, f"tratado_{arquivo}")
        if os.path.exists(caminho_entrada):
            try:
                funcao(caminho_entrada, caminho_saida)
            except Exception as e:
                print(f"⚠️ Erro ao tratar {arquivo}: {e}")
        else:
            print(f"⚠️ Arquivo {arquivo} não encontrado na pasta de entrada.")

def tratar_todos():
    main()

if __name__ == "__main__":
    main()

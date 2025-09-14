import os
import pandas as pd
import unicodedata

# Função auxiliar para padronizar colunas
def padronizar_colunas(df):
    return df.rename(columns=lambda x: str(x).strip().replace('\ufeff', ''))

def tratar_clientes_desde(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    if 'CLIENTE' not in df.columns:
        df.rename(columns={df.columns[0]: 'CLIENTE'}, inplace=True)
    if 'CLIENTE_DESDE' in df.columns:
        df['CLIENTE_DESDE'] = pd.to_datetime(df['CLIENTE_DESDE'], errors='coerce')
    df = df.drop_duplicates(subset=['CLIENTE']) if 'CLIENTE' in df.columns else df.drop_duplicates()
    df = df[df['CLIENTE_DESDE'].notnull()] if 'CLIENTE_DESDE' in df.columns else df
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo clientes_desde tratado")

def tratar_contratacoes_12m(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    if 'VLR_CONTRATACOES_12M' in df.columns:
        df['VLR_CONTRATACOES_12M'] = df['VLR_CONTRATACOES_12M'].astype(str).str.replace(',', '.').astype(float)
    if 'QTD_CONTRATACOES_12M' in df.columns:
        df['QTD_CONTRATACOES_12M'] = pd.to_numeric(df['QTD_CONTRATACOES_12M'], errors='coerce').fillna(0).astype(int)
    df = df.drop_duplicates(subset=['CD_CLIENTE']) if 'CD_CLIENTE' in df.columns else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo contratacoes_12m tratado")

def tratar_dados_clientes(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    if 'VL_TOTAL_CONTRATO' in df.columns:
        df['VL_TOTAL_CONTRATO'] = df['VL_TOTAL_CONTRATO'].astype(str).str.replace(',', '.').astype(float)
    if 'DT_ASSINATURA_CONTRATO' in df.columns:
        df['DT_ASSINATURA_CONTRATO'] = pd.to_datetime(df['DT_ASSINATURA_CONTRATO'], errors='coerce')
    if 'CD_CLIENTE' in df.columns and 'DS_PROD' in df.columns:
        df = df.drop_duplicates(subset=['CD_CLIENTE', 'DS_PROD'])
    else:
        df = df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo dados_clientes tratado")

def tratar_dicionario(caminho_entrada, caminho_saida):
    df = pd.read_excel(caminho_entrada)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    if len(df) > 2:
        df = df.iloc[2:]
    df.columns = ['Tabela', 'Campo', 'Significado']
    df = df.dropna(how='all')
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo dicionario tratado")

def tratar_historico(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    if 'DT_UPLOAD' in df.columns:
        df['DT_UPLOAD'] = pd.to_datetime(df['DT_UPLOAD'], errors='coerce')
    colunas_num = ['QTD','VL_PCT_DESC_TEMP','VL_PCT_DESCONTO','PRC_UNITARIO','VL_DESCONTO_TEMPORARIO','VL_TOTAL','VL_FULL','VL_DESCONTO']
    for col in colunas_num:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')
    if all(x in df.columns for x in ['NR_PROPOSTA','ITEM_PROPOSTA','CD_PROD']):
        df = df.drop_duplicates(subset=['NR_PROPOSTA','ITEM_PROPOSTA','CD_PROD'])
    else:
        df = df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo historico tratado")

def tratar_mrr(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    df = df.drop_duplicates(subset=['CLIENTE']) if 'CLIENTE' in df.columns else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo mrr tratado")

def tratar_nps_relacional(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    colunas_lower = {col.lower(): col for col in df.columns}
    if 'respondedat' in colunas_lower:
        df.rename(columns={colunas_lower['respondedat']: 'respondedAt'}, inplace=True)
    if 'respondedAt' in df.columns:
        df['respondedAt'] = pd.to_datetime(df['respondedAt'], errors='coerce')
    for col in df.columns:
        if col not in ['respondedAt','metadata_codcliente']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    if all(x in df.columns for x in ['respondedAt','metadata_codcliente']):
        df = df.drop_duplicates(subset=['respondedAt','metadata_codcliente'])
    else:
        df = df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo nps_relacional tratado")

def tratar_nps_aquisicao(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df.columns = df.columns.str.replace('Cód. Cliente','CD_CLIENTE').str.replace('Data da Resposta','DATA_RESPOSTA')
    if 'DATA_RESPOSTA' in df.columns:
        df['DATA_RESPOSTA'] = pd.to_datetime(df['DATA_RESPOSTA'], errors='coerce')
    for col in df.columns:
        if col not in ['CD_CLIENTE','DATA_RESPOSTA']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.drop_duplicates(subset=['CD_CLIENTE','DATA_RESPOSTA']) if all(x in df.columns for x in ['CD_CLIENTE','DATA_RESPOSTA']) else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo nps_aquisicao tratado")

def tratar_nps_implantacao(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df.columns = df.columns.str.replace('Cód. Cliente','CD_CLIENTE').str.replace('Data da Resposta','DATA_RESPOSTA')
    if 'DATA_RESPOSTA' in df.columns:
        df['DATA_RESPOSTA'] = pd.to_datetime(df['DATA_RESPOSTA'], errors='coerce')
    for col in df.columns:
        if col not in ['CD_CLIENTE','DATA_RESPOSTA']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.drop_duplicates(subset=['CD_CLIENTE','DATA_RESPOSTA']) if all(x in df.columns for x in ['CD_CLIENTE','DATA_RESPOSTA']) else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo nps_implantacao tratado")

def tratar_nps_onboarding(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    renomear = {
        'Data de resposta':'DATA_RESPOSTA','Cod Cliente':'CD_CLIENTE',
        'Em uma escala de 0 a 10, quanto você recomenda o Onboarding da TOTVS para um amigo ou colega?.':'Nota_NPS',
        'Em uma escala de 0 a 10, o quanto você acredita que o atendimento CS Onboarding ajudou no início da sua trajetória com a TOTVS?':'Nota_Atendimento',
        '- Duração do tempo na realização da reunião de Onboarding;':'Nota_Duracao',
        '- Clareza no acesso aos canais de comunicação da TOTVS;':'Nota_Clareza_Canais',
        '- Clareza nas informações em geral transmitidas pelo CS que lhe atendeu no Onboarding;':'Nota_Clareza_Info',
        '- Expectativas atendidas no Onboarding da TOTVS.':'Nota_Expectativas'
    }
    df.rename(columns=renomear,inplace=True)
    if 'DATA_RESPOSTA' in df.columns:
        df['DATA_RESPOSTA'] = pd.to_datetime(df['DATA_RESPOSTA'], errors='coerce')
    for col in df.columns:
        if col not in ['CD_CLIENTE','DATA_RESPOSTA']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.drop_duplicates(subset=['CD_CLIENTE','DATA_RESPOSTA']) if all(x in df.columns for x in ['CD_CLIENTE','DATA_RESPOSTA']) else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo nps_onboarding tratado")

def tratar_nps_produto(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df.rename(columns={'Data da Resposta':'DATA_RESPOSTA','Linha de Produto':'LINHA_PRODUTO','Nome do Produto':'NOME_PRODUTO','Cód. T':'CD_CLIENTE'}, inplace=True)
    if 'DATA_RESPOSTA' in df.columns:
        df['DATA_RESPOSTA'] = pd.to_datetime(df['DATA_RESPOSTA'], errors='coerce')
    if 'Nota' in df.columns:
        df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')
    df = df.drop_duplicates(subset=['CD_CLIENTE','DATA_RESPOSTA','NOME_PRODUTO']) if all(x in df.columns for x in ['CD_CLIENTE','DATA_RESPOSTA','NOME_PRODUTO']) else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo nps_produto tratado")

def tratar_nps_suporte(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    df.rename(columns={'ticket':'TICKET','cliente':'CD_CLIENTE'}, inplace=True)
    for col in df.columns:
        if col not in ['TICKET','CD_CLIENTE','grupo_NPS']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.drop_duplicates(subset=['TICKET','CD_CLIENTE']) if all(x in df.columns for x in ['TICKET','CD_CLIENTE']) else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo nps_suporte tratado")

def tratar_tickets(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=';', on_bad_lines='skip')
    df = padronizar_colunas(df)
    for col in ['DT_CRIACAO','DT_ATUALIZACAO']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(lambda x: unicodedata.normalize('NFKD', str(x)).encode('ascii', errors='ignore').decode('utf-8') if pd.notnull(x) else x)
    df = df.drop_duplicates(subset=['BK_TICKET']) if 'BK_TICKET' in df.columns else df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print("✅ Arquivo tickets tratado")

def template_telemetria(caminho_entrada, caminho_saida):
    df = pd.read_csv(caminho_entrada, encoding='latin1', sep=',', on_bad_lines='skip')
    colunas_esperadas = ['CLIENTE_ID','EVENT_DURATION','MODULO_ID','PRODUCT_LINE_ID','REFERENCE_DATE_START','SLOT_ID','STATUS_LICENCA','TCLOUD','CLIENTE_PRIME']
    if len(df.columns) == len(colunas_esperadas):
        df.columns = colunas_esperadas
    if 'EVENT_DURATION' in df.columns:
        df['EVENT_DURATION'] = pd.to_numeric(df['EVENT_DURATION'], errors='coerce')
    if 'REFERENCE_DATE_START' in df.columns:
        df['REFERENCE_DATE_START'] = pd.to_datetime(df['REFERENCE_DATE_START'], errors='coerce')
    df = df.drop_duplicates()
    df.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print(f"✅ Arquivo {os.path.basename(caminho_entrada)} tratado")

def tratar_telemetria_1(c,e): template_telemetria(c,e)
def tratar_telemetria_2(c,e): template_telemetria(c,e)
def tratar_telemetria_3(c,e): template_telemetria(c,e)
def tratar_telemetria_4(c,e): template_telemetria(c,e)
def tratar_telemetria_5(c,e): template_telemetria(c,e)
def tratar_telemetria_6(c,e): template_telemetria(c,e)
def tratar_telemetria_7(c,e): template_telemetria(c,e)
def tratar_telemetria_8(c,e): template_telemetria(c,e)
def tratar_telemetria_9(c,e): template_telemetria(c,e)
def tratar_telemetria_10(c,e): template_telemetria(c,e)
def tratar_telemetria_11(c,e): template_telemetria(c,e)
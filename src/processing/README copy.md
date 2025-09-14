# Projeto de Tratamento de Dados CSV

Este projeto realiza o tratamento automático de 24 arquivos de dados, incluindo clientes, NPS, tickets e telemetria. Ele lê os arquivos originais, aplica correções de formatação, converte tipos de dados, remove duplicatas e gera arquivos tratados prontos para uso.

## 📂 Estrutura de Pastas
```
projeto_tratamento_csv/
│   main.py
│   tratamento.py (ou script com funções)
│   requirements.txt
│   README.md
└── dados_originais/
└── dados_tratados/
```

---

## ⚙️ Pré-requisitos
- Python 3.8 ou superior instalado.
- Biblioteca **pandas** instalada.

Instale as dependências executando:
```bash
pip install -r requirements.txt
```

---

## 🚀 Como Usar
1. Coloque todos os **24 arquivos originais** (CSV/XLSX) na pasta `dados_originais`.
2. Abra o terminal no VS Code (ou prompt de comando) na pasta do projeto.
3. Execute o script principal:
```bash
python main.py
```
4. Os arquivos tratados serão salvos em `dados_tratados` com o prefixo `tratado_`.

---

## 🗂️ Arquivos Processados
- clientes_desde (1).csv
- contratacoes_ultimos_12_meses.csv
- dados_clientes.csv
- dicionario.xlsx
- historico.csv
- mrr.csv
- nps_relacional.csv
- nps_transacional_aquisicao.csv
- nps_transacional_implantacao.csv
- nps_transacional_onboarding.csv
- nps_transacional_produto.csv
- nps_transacional_suporte.csv
- tickets.csv
- telemetria_1.csv até telemetria_11.csv

---

## ✅ Resultado
- Nomes de colunas padronizados.
- Datas convertidas para formato datetime.
- Valores numéricos corrigidos (vírgula → ponto).
- Duplicatas removidas.
- Arquivos tratados em UTF-8 prontos para análise.

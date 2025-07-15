
🎟️ Gerador de Cupons Promocionais em PDF

Este projeto em Python lê uma planilha Excel com códigos promocionais e gera automaticamente arquivos PDF individuais para cada cupom. Ideal para campanhas de marketing, sorteios, brindes e promoções personalizadas.

---

## 📂 Estrutura do Projeto
# cupons.xlsx
# Planilha com os códigos promocionais 
# gerar_cupons.py 
# Script principal em Python cupom_1.pdf 
# Arquivos PDF gerados (um por cupom)

## 📋 Requisitos

- Python 3.7+
- Bibliotecas:
  - `pandas`
  - `fpdf`

Você pode instalar as dependências com:

```bash
pip install pandas fpdf


#📑 Formato da Planilha (cupons.xlsx)
A planilha deve conter pelo menos duas colunas com os seguintes nomes:

Codigo1	Codigo2
ABC123	XYZ789
DEF456	LMN012
...	...

🚀 Como Usar
Coloque sua planilha cupons.xlsx na mesma pasta do script.
Execute o script:

python gerar_cupons.py

Serão gerados arquivos cupom_1.pdf, cupom_2.pdf, etc., com os códigos da planilha.


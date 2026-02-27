# 📊 Projeto BI — TechStore
Este projeto simula um cenário real de análise de vendas de uma distribuidora de eletrônicos, com foco em geração de insights estratégicos para tomada de decisão.
##  🧠  Objetivo do Projeto
O dashboard foi desenvolvido com o objetivo de transformar dados brutos de vendas em informações visuais claras e acionáveis, permitindo analisar faturamento, desempenho por categoria, produtos estratégicos e oportunidades ocultas no estoque.
<img width="755" height="420" alt="image" src="https://github.com/user-attachments/assets/8da58a97-906a-445d-8163-2b30c4ffb28d" />

---
##  🛠️  Tecnologias Utilizadas
- Python
- Pandas
- Power BI
- Git e GitHub
---
##  🔄  Processo de Tratamento de Dados (ETL)
O script `etl_techstore.py` realiza:
- Leitura dos dados brutos a partir do arquivo vendas_techstore.csv
- Tratamento de valores nulos, aplicando:
- Substituição de cliente e cidade por "Não informado"
- Preenchimento do preco_unitario com a mediana por produto
- Padronização de forma de pagamento
- Padronização e conversão de datas, tratando formatos inconsistentes (., /, -) e removendo registros inválidos
- Criação da coluna valor_total, calculada a partir de quantidade * preco_unitario
- Criação de colunas auxiliares (ano e mes) para permitir análises temporais no Power BI
- Padronização dos meses para português, facilitando a visualização no dashboard
- Exportação do dataset tratado para vendas_techstore_processed.csv, pronto para modelagem no Power BI
---
## ▶️  Como Executar o Projeto
### 1️⃣  Clonar o repositório
```bash
git clone https://github.com/ThiagoMarques16/TechStore.git
cd TechStore
```
### 2️⃣ Criar o ambiente virtual
```bash
python -m venv venv
```
### 3️⃣ Ativar o ambiente
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```
### 4️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 5️⃣ Executar o script
```bash
python python/etl_techstore.py
```
---
## 👨‍💻 Autor
Thiago Marques
🌐 https://thiagomarques.netlify.app/

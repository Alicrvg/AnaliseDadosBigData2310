import pandas as pd
Limpeza tabela 1
df = pd.read_csv("C:\\Users\\biblioteca.nig3\\Downloads\\Projeto_1\\bcdata.sgs.23079.csv", sep=';')

df['valor'] = df['valor'].str.replace(',', '.')

df.to_csv('arquivo_limpo.csv', index=False)

print("Coluna limpa com sucesso!")


df = pd.read_csv("C:\\Users\\biblioteca.nig3\\Downloads\Projeto_1\\bcdata.sgs.23079.csv", sep=';')

df = df.replace({',': '.'}, regex=True)

df.to_csv('tabela_corrigida.csv', sep=';', index=False)

print("Tabela separada e vírgulas trocadas!")

#Limpeza tabela 2
df = pd.read_csv("C:\\Users\\biblioteca.nig3\\Downloads\\Projeto_1\\bcdata.sgs.22885.csv", sep=';')

df = df.replace({',': '.'}, regex=True)

df.to_csv('tabela_corrigida2.csv', sep=';', index=False)

print("Tabela separada e vírgulas trocadas!")


#correção data e coluna
import os

arquivos_na_pasta = [f for f in os.listdir() if os.path.isfile(f)]
for i, f in enumerate(arquivos_na_pasta):
    print(f"[{i}] {f}")


tabela_corrigida2 = "C:\\Users\\biblioteca.nig3.SENACRJEDU\\Documents\\projeto\\projeto\\tabela_corrigida2.csv"


if not os.path.exists(tabela_corrigida2):
    print(f"\n❌ ERRO: O arquivo '{tabela_corrigida2}' ainda não foi encontrado.")
    print("Verifique se você digitou a extensão (.csv ou .xlsx) corretamente.")
else:
    try:
       
        df = pd.read_csv(tabela_corrigida2, sep=';', encoding='latin1')
       
       
        df.columns = df.columns.str.strip()
        print("\nColunas encontradas:", df.columns.tolist())


       
        coluna_alvo = 'data'


        if coluna_alvo in df.columns:
           
            df[coluna_alvo] = pd.to_datetime(df[coluna_alvo], dayfirst=True, errors='coerce')
            df[coluna_alvo] = df[coluna_alvo].dt.strftime('%Y-%m-%d')
           
           
            df.to_excel('resultado_final2.xlsx', index=False)
            print(f"\n✅ CONCLUÍDO! O arquivo 'resultado_final2.xlsx' foi criado.")
        else:
            print(f"\n❌ A coluna '{coluna_alvo}' não existe. Escolha uma da lista acima.")


    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")


#-------------------------------------------------------------------------------------------------------------
#Conexão SQL-Python
import numpy
import mysql.connector
import matplotlib 


def obter_dados_do_banco(query):
    # 1. Ajuste no host para 127.0.0.1
    conexao = mysql.connector.connect(
        host="127.0.0.1", 
        user="root",
        password="",
        database="investimentos_bacen"
    )
    
    cursor = conexao.cursor()
    cursor.execute(query)
    
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()
    
    return resultados


query_join = """
SELECT tc.data_referencia, tc.percentual_pib, idp.valor_usd_milhoes
FROM transacoes_correntes tc
INNER JOIN idp_mensal idp ON tc.data_referencia = idp.data_referencia;
"""

query_filtro_2026 = """
SELECT * 
FROM transacoes_correntes 
WHERE data_referencia BETWEEN '2026-01-01' AND '2026-12-31'
ORDER BY data_referencia ASC;
"""

query_recordes_idp = """
SELECT MAX(valor_usd_milhoes) AS recorde_idp, MIN(valor_usd_milhoes) AS menor_idp
FROM idp_mensal;
"""

query_maior_deficit = "SELECT MIN(percentual_pib) FROM transacoes_correntes;"

query_estatisticas = """
SELECT 
    AVG(percentual_pib) AS media_pib_periodo,
    SUM(valor_usd_milhoes) AS total_idp_acumulado
FROM transacoes_correntes tc
JOIN idp_mensal idp ON tc.data_referencia = idp.data_referencia;
"""

# --- EXECUÇÃO E EXIBIÇÃO ---

# 1. Relatório Geral
print("--- DADOS CRUZADOS ---")
for linha in obter_dados_do_banco(query_join):
    print(linha)

# 2. Filtro 2026
print("\n--- TRANSAÇÕES 2026 ---")
for linha in obter_dados_do_banco(query_filtro_2026):
    print(linha)

# 3. Recordes IDP
print("\n--- RECORDES IDP (MÁX / MÍN) ---")
print(obter_dados_do_banco(query_recordes_idp))

# 4. Maior Déficit
print("\n--- MAIOR DÉFICIT PIB ---")
print(obter_dados_do_banco(query_maior_deficit))

# 5. Estatísticas Acumuladas
print("\n--- MÉDIA PIB E TOTAL IDP ---")
print(obter_dados_do_banco(query_estatisticas))

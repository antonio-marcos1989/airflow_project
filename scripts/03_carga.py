import pandas as pd
import sqlite3

def main():
    df = pd.read_csv('data/dados_transformados.csv')

    conn = sqlite3.connect('data/dados_covid.db')
    df.to_sql('covid_data', conn, if_exists='replace', index=False)
    conn.close()

    print("✅ Dados carregados no banco 'data/dados_covid.db' na tabela 'covid_data'")

if __name__ == "__main__":
    main()

import pandas as pd
import sqlite3

def main():
    conn = sqlite3.connect('/opt/airflow/data/dados_covid.db')

    query = """
    SELECT state, MAX(total_cases) as casos_max
    FROM covid_data
    GROUP BY state
    ORDER BY casos_max DESC
    """

    resultado = pd.read_sql_query(query, conn)
    print(resultado)

    conn.close()
    print("✅ Consulta finalizada")

if __name__ == "__main__":
    main()

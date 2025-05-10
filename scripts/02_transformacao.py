import pandas as pd

def main():
    df = pd.read_csv('/opt/airflow/data/dados_brutos.csv')

    df = df[['state', 'date', 'totalCases', 'deaths']]
    df.columns = ['state', 'date', 'total_cases', 'deaths']
    df['date'] = pd.to_datetime(df['date'])

    df.to_csv('/opt/airflow/data/dados_transformados.csv', index=False)
    print("✅ Dados transformados e salvos em 'data/dados_transformados.csv'")

if __name__ == "__main__":
    main()

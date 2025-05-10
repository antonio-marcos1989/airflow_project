import pandas as pd

def main():
    url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
    df = pd.read_csv(url)
    df.to_csv('/opt/airflow/data/dados_brutos.csv', index=False)
    print("✅ Dados baixados e salvos em 'data/dados_brutos.csv'")

if __name__ == "__main__":
    main()

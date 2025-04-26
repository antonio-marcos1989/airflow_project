import subprocess
import sys
import time

# Definir os passos do pipeline (ordem + script)
PIPELINE_STEPS = [
    ("Ingestão dos dados", "scripts/01_ingestao.py"),
    ("Transformação dos dados", "scripts/02_transformacao.py"),
    ("Carga dos dados no banco", "scripts/03_carga.py"),
    ("Consumo e consulta dos dados", "scripts/04_consumo.py"),
]

def run_step(description, script_path):
    """Executa um script individual com log e captura de erros."""
    print(f"\n🚀 Iniciando etapa: {description}")

    try:
        start_time = time.time()
        subprocess.run(["python3", script_path], check=True)
        elapsed = time.time() - start_time
        print(f"✅ Etapa '{description}' concluída em {elapsed:.2f} segundos.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Erro na etapa '{description}'. Código de erro: {e.returncode}")
        # Se quiser que o pipeline pare se der erro, descomente a linha abaixo:
        sys.exit(1)

def run_pipeline():
    print("\n==============================")
    print("🏗️  Iniciando execução do pipeline completo")
    print("==============================\n")

    for description, script in PIPELINE_STEPS:
        run_step(description, script)

    print("\n==============================")
    print("🏁 Pipeline executado com sucesso!")
    print("==============================\n")

if __name__ == "__main__":
    run_pipeline()

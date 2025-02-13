import subprocess
import sys
import os

def install_requirements():
    # Verifica se existe o arquivo requirements.txt
    if os.path.exists('requirements.txt'):
        print("🛠 Instalando dependências...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependências instaladas com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar as dependências: {e}")
    else:
        print("⚠️ Nenhum arquivo requirements.txt encontrado.")

if __name__ == "__main__":
    install_requirements()

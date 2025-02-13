import os

def create_project_structure(folders):
    # Cria o arquivo main.py
    main_file = "./main.py"
    with open(main_file, "w") as file:
        file.write("# Arquivo main.py para Custom\n")
    
    # Cria a pasta src
    src_dir = './src'
    os.makedirs(src_dir, exist_ok=True)
    
    # Cria as pastas dentro de src
    for folder in folders:
        path_folder = os.path.join(src_dir, folder)
        os.makedirs(path_folder, exist_ok=True)
        print(f'📂 Pasta criada: {path_folder}')
    
    print("\n✅ Estrutura do projeto criada com sucesso!")

def custom_structure():
    # Pergunta para o usuário o número de pastas que deseja criar
    while True:
        quantity = input("Quantas pastas deseja criar? ")
        
        try:
            number = int(quantity)
            if number <= 0:
                print("❌ O número deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("❌ Entrada inválida! Digite um número inteiro.")

    # Solicita os nomes das pastas
    folders = []
    for i in range(number):
        name = input(f"Nome da pasta {i+1}: ")
        folders.append(name)

    # Cria a estrutura do projeto
    create_project_structure(folders)

# O código que será executado ao gerar o projeto
if __name__ == "__main__":
    # Obtém a arquitetura selecionada pelo usuário (definida em cookiecutter.json)
    architecture = "{{cookiecutter.architecture}}"
    
    if architecture == "Custom":
        custom_structure()  # Chama a função custom_structure para criar as pastas
    elif architecture == "MVC - (Models, Views, Controllers)":
        create_project_structure(["models", "views", "controllers"])
    elif architecture == "Automations - by lima":
        create_project_structure(["models", "views", "services", "tasks", "tests", "utils"])

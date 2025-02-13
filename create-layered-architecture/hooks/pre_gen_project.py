import inquirer
import os

def create_project_structure(architecture, folders):
    main_file = "./main.py"
    with open(main_file, "w") as file:
        file.write(f"# Arquivo main.py para {architecture}\n")
    
    src_dir = './src'
    os.makedirs(src_dir, exist_ok=True)
    
    for folder in folders:    
        path_folder = os.path.join(src_dir, folder)
        os.makedirs(path_folder, exist_ok=True)
        print(f'📂 Pasta criada: {path_folder}')
    
    print("\n✅ Estrutura do projeto criada com sucesso!")

def custom_structure():    
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

    folders = []
    for i in range(number):
        name = input(f"Nome da pasta {i+1}: ")
        folders.append(name)

    create_project_structure("Custom", folders)

architecture_options = {
    "MVC - (Models, Views, Controllers)": ["models", "views", "controllers"],
    "Automations - by lima": ["models", "views", "controllers", "tasks", "tests", "utils"],
    "Custom": custom_structure
}

# Remove o questionário para selecionar o tipo de projeto, e passa a usar diretamente o valor
architecture = "MVC - (Models, Views, Controllers)"  # Alterar aqui para o tipo de projeto desejado

# Não faz a escolha interativa e vai direto para a criação da estrutura
if architecture == "Custom":
    architecture_options["Custom"]()
else:
    create_project_structure(architecture, architecture_options[architecture])

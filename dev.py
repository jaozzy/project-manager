import argparse
import os
import subprocess

# Define the path where the code will start
base_dir = os.path.join(os.path.expanduser("~"), "Desktop", "rf", "ucf", "apps", "prog")

def criar_projeto(categoria, tecnologia, nome):
    # Define the paths for the category and technology directories
    categoria_dir = os.path.join(base_dir, categoria)
    tecnologia_dir = os.path.join(categoria_dir, tecnologia)
    
    # Check if the category directory exists
    if not os.path.exists(categoria_dir):
        os.makedirs(categoria_dir, exist_ok=True)
    
    # If a new technology name is provided, create a new technology directory
    if tecnologia and not os.path.exists(tecnologia_dir):
        os.makedirs(tecnologia_dir, exist_ok=True)
        print(f"Tecnologia '{tecnologia}' criada na categoria '{categoria}'.")
    
    # If a project name is provided, create a new project directory
    if nome is not None:
        projeto_dir = os.path.join(tecnologia_dir, nome)
        os.makedirs(projeto_dir, exist_ok=True)
        print(f"Projeto '{nome}' criado em '{projeto_dir}'.")
        abrir_vscode(projeto_dir)
    else:
        # List existing projects within the specified category and technology
        projetos = [projeto for projeto in os.listdir(tecnologia_dir) if os.path.isdir(os.path.join(tecnologia_dir, projeto))]
        if not projetos:
            print(f"Nenhum projeto encontrado na categoria '{categoria}' e tecnologia '{tecnologia}'.")
        else:
            print(f"Projetos disponíveis na categoria '{categoria}' e tecnologia '{tecnologia}':")
            for projeto in projetos:
                print(f"- {projeto}")
            
            # Prompt the user to choose a project by name
            escolha = input("Digite o nome do projeto desejado: ")
            projeto_dir = os.path.join(tecnologia_dir, escolha)
            if not os.path.exists(projeto_dir):
                print(f"Projeto '{escolha}' não encontrado.")
            else:
                print(f"Projeto '{escolha}' selecionado. Diretório: '{projeto_dir}'.")
                abrir_vscode(projeto_dir)


def abrir_vscode(diretorio):
    try:
        subprocess.Popen(["code", diretorio])
    except OSError:
        try:
            subprocess.Popen(["code.cmd", diretorio])
        except OSError:
            print("O Visual Studio Code não foi encontrado. Certifique-se de que está instalado e configurado corretamente.")


if __name__ == "__main__":
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description="Script para criar e listar projetos")
    parser.add_argument("-c", "--categoria", help="Categoria do projeto")
    parser.add_argument("-t", "--tecnologia", help="Tecnologia do projeto")
    parser.add_argument("-nt", "--nova-tecnologia", metavar="nome", help="Adiciona um diretório para uma tecnologia até então não existente")
    parser.add_argument("-np", metavar="nome", help="Criar um novo projeto com o nome fornecido")
    args = parser.parse_args()

    # Extract the values from the arguments
    categoria = args.categoria
    tecnologia = args.tecnologia
    nome = args.np

    # If '-nt' option is provided, set 'tecnologia' to the value of 'nova_tecnologia' to create a new technology directory
    if args.nova_tecnologia:
        tecnologia = args.nova_tecnologia

    # Call the function to create or list projects
    criar_projeto(categoria, tecnologia, nome)

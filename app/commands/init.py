import sys
import app.monalisa.init as monalisa

def start_server():
    print("Servidor iniciado...")

def migrate():
    print("Migrações aplicadas com sucesso!")

def make_controller(name):
    print(f"Controller {name} criado com sucesso!")

def help():
    print("""
    Comandos disponíveis:
    startserver               - Inicia o servidor
    migrate                   - Roda as migrações do banco de dados
    makecontroller [name]     - Cria um novo controller com o nome especificado
    """)

def main():
    if len(sys.argv) < 2:
        help()
        return
    
    command = sys.argv[1]
    
    if command == "startserver":
        start_server()
    elif command == "migrate":
        migrate()
    elif command == "makecontroller":
        if len(sys.argv) < 3:
            print("Erro: Você deve fornecer um nome para o controller.")
        else:
            make_controller(sys.argv[2])
    elif command == "monalisa":
        monalisa.main()
    else:
        print(f"Comando '{command}' não encontrado.")
        help()

if __name__ == "__main__":
    main()

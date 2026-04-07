# gerenciadortarefas.py

# -------------------- funções de interface
def listar_tarefas(tarefas):
    """Exibe tarefas com status"""
    if not tarefas:
        print("\nnenhuma tarefa cadastrada\n")
        return
    print("\ntarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["Concluída"] else "Pendente"
        print(f"{i}. {tarefa['titulo']} - {status}")
    print()

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa"""
    titulo = input("Digite o título da tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "Concluída": False})
        print("Tarefa adicionada com sucesso!\n")
    else:
        print("Título vazio, não foi adicionada!\n")

def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        n = int(input("Digite o número da tarefa para concluir: "))
        if 1 <= n <= len(tarefas):
            tarefas[n-1]["Concluída"] = True
            print("Tarefa concluída!\n")
        else:
            print("Número inválido\n")
    except ValueError:
        print("Entrada inválida\n")

def remover_tarefa(tarefas):
    """Remove uma tarefa"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        n = int(input("Digite o número da tarefa para remover: "))
        if 1 <= n <= len(tarefas):
            tarefa = tarefas.pop(n-1)
            print(f"Tarefa '{tarefa['titulo']}' removida!\n")
        else:
            print("Número inválido\n")
    except ValueError:
        print("Entrada inválida\n")

# -------------------- menu principal
def menu():
    tarefas = []
    while True:
        print("Gerenciador de tarefas")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida\n")

# -------------------- execução
if __name__ == "__main__":
    menu()

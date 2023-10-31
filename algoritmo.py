import random
import os

class DAO:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.ids_salvos = []
        self.id = random.randint(1000, 9999)
        self.titulos_adicionados = False
        self.A = "A"

    def adicionar_tarefa(self, tarefa):
        with open(self.arquivo, 'a') as arquivo:
            if not self.titulos_adicionados:
                arquivo.write("STATUS\tID\tTAREFA\n\n")
                self.titulos_adicionados = True

            while True:
                self.id = random.randint(1000, 9999)
                if self.id not in self.ids_salvos:
                    break

            arquivo.write(f"{self.A}\t{self.id}\t{tarefa}\n")
            self.ids_salvos.append(self.id)

    def listar_tarefas(self):
        tarefas = []
        with open(self.arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if '\t' not in linha:
                    continue
                status, id, tarefa = linha.split('\t', 2)
                tarefas.append((status.strip(), id.strip(), tarefa.strip()))
        return tarefas

class ToDo:
    def __init__(self, arquivo):
        self.dao = DAO(arquivo)

    def adicionar_tarefa(self, tarefa):
        self.dao.adicionar_tarefa(tarefa)
        return True

    def excluir_tarefa(self, excluir):
        tarefas = self.listar_tarefas()
        if excluir >= 0 and excluir < len(tarefas):
            tarefa_removida = tarefas.pop(excluir)
            self.atualizar_lista_tarefas(tarefas)
            return tarefa_removida
        else:
            return None

    def listar_tarefas(self):
        return self.dao.listar_tarefas()

    def alterar_tarefa(self, indice, nova_tarefa):
        tarefas = self.listar_tarefas()
        if 0 <= indice < len(tarefas):
            tarefas[indice] = ("A", tarefas[indice][1], nova_tarefa)
            self.atualizar_lista_tarefas(tarefas)
            return True
        else:
            return False

    def concluir_tarefa(self, indice):
        tarefas = self.listar_tarefas()
        if 0 <= indice < len(tarefas):
            if tarefas[indice][0] == "A":
                tarefas[indice] = ("C", tarefas[indice][1], tarefas[indice][2])
                self.atualizar_lista_tarefas(tarefas)
                return True
            else:
                return False
        else:
            return False

    def listar_tarefas_concluidas(self):
        tarefas = self.listar_tarefas()
        return [tarefa for tarefa in tarefas if tarefa[0] == "C"]

    def atualizar_lista_tarefas(self, tarefas):
        with open(self.dao.arquivo, 'w') as arquivo:
            arquivo.write("STATUS\tID\tTAREFA\n\n")
            for status, id, tarefa in tarefas:
                arquivo.write(f"{status}\t{id}\t{tarefa}\n")

def main():
    arquivo = "Tarefa.txt"
    todo = ToDo(arquivo)
    
    sair = False

    while not sair:
        os.system("cls")
        print("SOFTWARE DE TO-DO\n")
        print("[1] Adicionar tarefa")
        print("[2] Listar tarefas")
        print("[3] Alterar tarefa")
        print("[4] Concluir tarefa")
        print("[5] Listar tarefas concluídas")
        print("[6] Excluir tarefa")
        print("[7] Sair")

        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            os.system("cls")
            print("-- ADICIONAR TAREFA ---\n")
            tarefa = input("Adicione uma tarefa: ")
            todo.adicionar_tarefa(tarefa)
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            os.system("cls")
            print("--- LISTAR TAREFAS ---\n")
            tarefas = todo.listar_tarefas()
            for i, (_, _, descricao) in enumerate(tarefas):
                print(f"{i} - {descricao}")
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            os.system("cls")
            print("--- ALTERAR TAREFA ---\n")
            tarefas = todo.listar_tarefas()
            indice = input("\nDigite o índice da tarefa que deseja alterar: ")
            nova_descricao = input("Digite a nova descrição da tarefa: ")
            todo.alterar_tarefa(int(indice), nova_descricao)
            input("\nPressione Enter para continuar...")

        elif opcao == "4":
            os.system("cls")
            print("--- CONCLUIR TAREFA ---\n")
            tarefas = todo.listar_tarefas()
            indice = input("\nDigite o índice da tarefa que deseja concluir: ")
            todo.concluir_tarefa(int(indice))
            input("\nPressione Enter para continuar...")

        elif opcao == "5":
            os.system("cls")
            print("--- LISTAR TAREFAS CONCLUÍDAS ---\n")
            tarefas_concluidas = todo.listar_tarefas_concluidas()
            for i, (_, _, descricao) in enumerate(tarefas_concluidas):
                print(f"{i} - {descricao}")
            input("\nPressione Enter para continuar...")

        elif opcao == "6":
            os.system("cls")
            print("--- EXCLUIR TAREFA ---\n")
            tarefas = todo.listar_tarefas()
            indice = input("\nDigite o índice da tarefa que deseja excluir: ")
            todo.excluir_tarefa(int(indice))
            input("\nPressione Enter para continuar...")

        elif opcao == "7":
            sair = True

        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()


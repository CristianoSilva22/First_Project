c=5
l=[]
print("Bem vindo a crissystems - To do List")
while(c!=0):
    print("Digite 1 para adicionar uma tarefa\nDigite 2 para listar as tarefas\nDigite 3 para editar alguma tarefa\nDigite 4 para excluir uma tarefa")
    c=int(input())
    if(c==0):
        print("Até a próxima!")
    elif(c==1):
        print("\nDigite a tarefa a ser adicionada")
        l.append(input())
        print("\n")
    elif(c==2):
        print("Lista: ")
        for i in l:
            print(i)
        print("\n")
    elif(c==3):
        print("ainda implementando - editar tarefas")
    elif(c==4):
        print("ainda implementando - excluir tarefas")

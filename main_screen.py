c=5
print("Bem vindo a crissystems - To do List")
while(c!=0):
    print("\nDigite 1 para adicionar uma tarefa\nDigite 2 para listar as tarefas\nDigite 3 para editar alguma tarefa\nDigite 4 para excluir uma tarefa\nDigite 0 para sair")
    c=int(input())
    if(c==0):
        print("Até a próxima!")
    elif(c==1):
        print("\nDigite a tarefa a ser adicionada")
        l.append(input())
        print("Tarefa adicionada!")
    elif(c==2):
        print("\nLista: ")
        for i,e in enumerate(l):
            print(i+1,":",e)
    elif(c==3):
        i=input("\nDigite a tarefa a ser alterada\n")
        i=l.index(i)
        l[i]=input("Digite a tarefa com a alteração\n")
        print("Tarefa alterada!")
    elif(c==4):
        i=input("\nDigite a tarefa a ser alterada\n")
        i=l.index(i)
        del(l[i])
        print("Tarefa excluída!")

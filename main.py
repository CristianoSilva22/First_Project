import os, modulo_adicionar, modulo_listar, modulo_alterar, modulo_excluir
c=5
l=[]
try:
    mt=open("database.txt","r+")
    for i in mt:
        l.append(i.replace("\n",""))
    mt.close()
    os.remove("database.txt")
except:
    print("Primeira Inicialização concluída!\n")
print("Bem vindo a crissystems - To do List")
while(c!=0):
    print("\nDigite 1 para adicionar uma tarefa\nDigite 2 para listar as tarefas\nDigite 3 para editar alguma tarefa\nDigite 4 para excluir uma tarefa\nDigite 0 para sair")
    c=int(input())
    if(c==0):
        print("Até a próxima!")
    elif(c==1):
        l=modulo_adicionar.adicionar_elemento(l)
    elif(c==2):
        modulo_listar.listar_elementos(l)
    elif(c==3):
        l=modulo_alterar.alterar_elemento(l)
    elif(c==4):
        l=modulo_excluir.excluir_elemento(l)
mt=open("database.txt","a")
for i in l:
    mt.write(i)
    mt.write("\n")
mt.close()

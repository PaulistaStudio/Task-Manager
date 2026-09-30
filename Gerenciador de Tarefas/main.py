import json
import os
arquivo="lista.json"
def ler_dados():
    if not os.path.exists(arquivo):
        return {"tarefas":[]}
    with open(arquivo,"r",encoding='utf-8') as f:
        return json.load(f)
def organizador(lista):
    N=1
    for i in lista:
        print(N,i)
        N+=1
class criar():
    def __init__(self,nome,F_P):
        self.Nome=nome
        self.Status=F_P
    def verificacao(self):
        if self.Status==True:
            print("Tarefa realizada")
        else:
            print("Tarefa pedente")
    def alteraçao(self):
        esc=...
        while esc!=4:
            alt=["Nome","Feita/pedente","Apagar","Nada"]
            organizador(alt)
            try:
                esc=int(input("Deseja altera oque?"))
                print()
                if esc==1:
                    print("Coloque o novo nome")
                    nome=input()
                    self.Nome=nome
                    dados["tarefas"][esco]["Nome"]=self.Nome
                elif esc==2:
                    print("Essa tarefa foi realizada?")
                    st=input("S/N").upper()
                    if st=="S":
                        self.Status=True
                        dados["tarefas"][esco]["Status"]=True
                    elif st=="N":
                        self.Status=False
                        dados["tarefas"][esco]["Status"]=False
                    else:
                        print()
                        print("Erro << Responda apenas com as opções disponiveis")
                        print()
                elif esc==3:
                    dados["tarefas"].pop(esco)
                    with open(arquivo, "w", encoding="utf-8") as f:
                        json.dump(dados, f)
                        break
                else:
                    print("Coloque um numero valido")
                with open(arquivo, "w", encoding="utf-8") as f:
                    json.dump(dados, f)
                print()
            except ValueError:
                print()
                print("ERRO << O sistema espera receber um numero")
                print()
print("Tarefas")
opcoes=["Criar tarefa","Ver tarefas"]
while True:
    organizador(opcoes)
    try:
        esc=int(input(""))
        if esc==1:
            print("Qual o nome da sua tarefa?")
            nome=input()
            dados=ler_dados()
            status=False
            livre=True
            for tarefa in dados["tarefas"]:
                if tarefa["Nome"] == nome:
                    print("Essa tarefa já existe!")
                    livre=False
                    break
            if livre==True:  
                dados=ler_dados()
                tarefa=criar(nome,status)
                dados["tarefas"].append(tarefa.__dict__)
                with open(arquivo, "w", encoding="utf-8") as f:
                    json.dump(dados, f)
        elif esc==2:
            dados=ler_dados()
            i=1
            print()
            for tarefa in dados["tarefas"]:
                print(i,tarefa["Nome"])
                i+=1
            print()
            try:
                print("Escolha um para verificar")
                esco=int(input())
                esco-=1
                escolha=...
                tarefa=criar(dados["tarefas"][esco]["Nome"],dados["tarefas"][esco]["Status"])
                tarefa.verificacao()
                escolha=input("deseja altera ele?[S/N]").upper()
                if escolha=="S":
                    tarefa.alteraçao()
                elif escolha=="N":
                    pass
                else:
                    print("Não foi possivel altera")
            except ValueError:
                print("Você digitou algo que não é número")
            except IndexError:
                print("Essa tarefa não existe")
        else:
            print("Coloque um número valido")
    except ValueError:
        print("Você digitou algo que não é um número")
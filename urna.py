import os
import random
mespass=open('mespass.txt','r')
senhamesario=mespass.readline()
mespass.close()
secpass=open('secpass.txt','w')
senhasecretario=secpass.write("")
secpass.close()
mespass=open('mespass.txt','w')
senhamesario=mespass.write("")
mespass.close()
secpass=open('secpass.txt','r')
senhasecretario=secpass.readline()
secpass.close()
prespass=open('prespass.txt','w')
senhapresidente=prespass.write("")
prespass.close()
prespass=open('prespass.txt','r')
senhapresidente=prespass.readline()
prespass.close()
admpass = open('admpass.txt', 'w')
admpass.write("admtse")
admpass.close()

user = int(input("Sistema Eleitoral / Urna Eleetronica \n  \n escolha um user \n  \n Administrador digite - 1 \n secretario digite - 2 \n presidente digite - 3 \n mesario digite - 4 \n : "))

while user!=1:

    user = int(input("Somente o ADMINSITRADOR tem cadastro \n Para administrador, digite 1"))

else:
    admpass=open('admpass.txt','r')
    senhaadm=admpass.read()
    admpass.close()
    s=input("digite sua senha do administrador: ")
    while s!=senhaadm:
        print("senha incorreta")
        s=str(input("digite sua senha: "))
    else:
        escolha = int(input('Seja bem vindo, administrador \n \n Para cadastrar secretário, digite 1 \n : '))
        while escolha !=1:
            escolha = int(input('Opção para cadastro de secretario \n digite 1 para cadastrar secretario \n : '))
        else:
            print("digite uma nova senha para o secretario")
            senhasecretario=str(input())
            secpass=open('secpass.txt', 'w')
            secpass.write(senhasecretario)
            secpass.close()
            print("senha cadastrada com sucesso")
            print("")

input("pressione enter para sair do menu de administrador")
print("Sistema Eleitoral / Urna Eleetronica \n ")
print("escolha um user \n ")
print("Administrador digite 1")
if not(senhasecretario==""):
        print("Secretário digite 2")
if not(senhapresidente==""):
        print("Presidente digite 3")
if not(senhamesario==""):
        print("Mesario digite 4")
print("")
user = int(input(": "))

while user!=2:
    print("administrador já cadastrou o secretário")
    print("")
    user=input("digite 2 para logar como secretario")                
else :
    print("digite sua senha de secretário")
    ss=input()
    secpass=open('secpass.txt','r')
    senhasecretario=secpass.readline()
    secpass.close()
    while ss!=senhasecretario:
        print("senha incorreta")
        ss=str(input("digite sua senha: "))

    else:

        passpresidente=str(input("Bem vindo, secretario \n \n cadastro presidente \n digite a senha do presidente"))
        prespass=open('prespass.txt', 'w')
        prespass.write(passpresidente)
        prespass.close()                                
        print("cadastro presidente realizado com sucesso \n ")
        print("cadastro mesario \n ")            
        SMESARIO=str(input("digite a senha do mesario: "))
        print("cadastro mesario realizado com sucesso \n ")
        print("cadastro de candidatos")
        NC=int(input("Número de candidatos: "))
        candidatos = {}
        LC=[]
        if NC != None:
            for i in range(int(NC)):
                nome = input('Nome: ')
                candidatos.update({
                i: {
                    "name": nome.capitalize(),
                    "numEleitoral": random.randint(1,100),
                    "qtdVotos": 0
                    }
                    })
                os.system('cls||clear')
                for qtdCandidato in candidatos.values():
                    print('Candidato: {} \nNúmero eleitoral: {}\n'.format(qtdCandidato['name'], qtdCandidato['numEleitoral']))                             
print("")
print("cadastro eleitores")
print("digite a quantidade de eleitores")
SE=int(input())
LE=[]
while SE>0:
    print("digite a senha de mais um eleitor")
    E=str(input())
    LE.append(E)
    SE=SE-1
else:

    user=int(input("\n escola um usuario \n \n Secretário digite 1 \n Presidente digite 2 \n Mesario digite 3 \n"))

while user!=2: 

    user=int(input("É preciso que o presidente entre para zerar a votação \n \n escolha um usuario \n \n Secretário digite 1 \n Presidente digite 2 \n Mesario digite 3 \n"))    

else:
    sp=str(input("Digite a senha do presidente: "))
    while sp!=passpresidente:
        print("senha incorreta")
        sp=str(input())
    else:
        QC=len(LC)
        (QC)
        votos=0
        input("\n Bem Vindo PRESIDENTE \n \n para zerar votaçao tecle enter")
        input("votaçao zerada, tecle enter para sair")
        
user=int(input("\n escolha um usuario \n \n Secretário digite 1 \n Presidente digite 2 \n Mesario digite 3 \n"))

while user!=3:

    user=input("entre como mesario para iniciar a votaçao")

else:

    sm=input("digite senha do mesario: ")

while SMESARIO!=sm:
    
    sm=input("senha incorreta \n digite a senha novamente: ")

else:

    input("\n Bem Vindo mesario \n para iniciar votaçao tecle enter")
    
se=input("\n Digite a senha para iniciar a votação")

while not se in LE:
    print()
    se=print("senha incorreta, digite novemente")
else:
    LE.remove(se)
    print(LE)
    input()
    for i in LC:
        print(i)
        print("deseja votar em",i)
        CV=int(input("se sim 1 se nao 2"))
        if CV==2:
            input()
            print("voto computado")
print("votaçao encerrada")

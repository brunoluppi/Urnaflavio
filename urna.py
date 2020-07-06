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
print("              Bem Vindo à Urna Eletrônica")
print("-----------------------------------------------------")
print("|                 escolha um usuario")
print("-----------------------------------------------------")
print("|                Administrador digite 1")
print("|                secretario digite 2")
print("|                presidente digite 3")
print("|                mesario digite 4")
print("-----------------------------------------------------")
usuario=input()
um="1"
while usuario!=um:
        print("somente o administrador tem cadastro")
        print("-----------------------------------------------------")
        print("              Bem Vindo à Urna Eletrônica")
        print("-----------------------------------------------------")
        print("|                 escolha um usuario")
        print("-----------------------------------------------------")
        print("|                Administrador digite 1")
        print("-----------------------------------------------------")
        usuario=input()
else:
        admpass=open('admpass.txt','r')
        senhadoadm=admpass.read()
        admpass.close()
        s=input("digite sua senha do administrador: ")
        print()
        while s!=senhadoadm:
                print("senha incorreta")
                s=str(input("digite sua senha: "))
        else:
                print ("seja bem vindo, administrador!")
                print("-------------------------------------------------------------------")
                print("|              para cadastrar secretário digite 1")
                print("-------------------------------------------------------------------")
                escolha=input()
                um="1"
                while escolha !=um:
                        print("opção apenas para cadastro de secretario \n")
                        print ("digite 1 para cadastrar o secretario")
                        escolha=input()
                else:
                        print("digite uma nova senha para o secretario")
                        senhasecretario=str(input())
                        secpass=open('secpass.txt', 'w')
                        secpass.write(senhasecretario)
                        secpass.close()
                        print("senha cadastrada com sucesso")
                        print()
                        print("-----------------------------------------------------")
input("para sair do perfil de administrador aperte Enter")
print("              Bem Vindo à Urna Eletrônica")
print("-----------------------------------------------------")
print("|                 escolha um usuario")
print("-----------------------------------------------------")
print("|                Administrador digite 1")
if not(senhasecretario==""):
        print("|                Secretário digite 2")
if not(senhapresidente==""):
        print("|                Presidente digite 3")
if not(senhamesario==""):
        print("|                  Mesario digite 4")
print("-----------------------------------------------------")
usuario=input()
dois="2"
while usuario!=dois:
                print("administrador já cadastrou o secretário")
                print("")
                usuario=input("digite 2 para logar como secretario")                
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
                        print()
                        print("seja bem vindo, secretário")
                        print()
                        print("cadastro presidente")
                        print("digite a senha do presidente")
                        SPRESIDENTE=str(input())
                        prespass=open('prespass.txt', 'w')
                        prespass.write(SPRESIDENTE)
                        prespass.close()                                
                        print("cadastro presidente realizado com sucesso")
                        print()
                        print("-----------------------------------------------------")
                        print("cadastro mesario")
                        print("digite a senha do mesario")            
                        SMESARIO=str(input())
                        print("cadastro mesario realizado com sucesso")
                        print("-----------------------------------------------------")
                        print("cadastro candidatos")
                        print("digite a quantidade de candidatos")
                        NC=int(input())
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
print("-----------------------------------------------------")
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
    print("")
print("-----------------------------------------------------")
print("|             escolha um usuario")
print("-----------------------------------------------------")
print("|              Secretário digite 1")
print("|              Presidente digite 2")
print("|                Mesario digite 3")
print("-----------------------------------------------------")
usuario=int(input())
while usuario!=2: 
    print("é necessario que o presidente entre para zerar votos")
    print("-----------------------------------------------------")
    print("|             escolha um usuario")
    print("-----------------------------------------------------")
    print("|              Secretário digite 1")
    print("|              Presidente digite 2")
    print("|                Mesario digite 3")
    print("-----------------------------------------------------")
    usuario=int(input())    
else:
    print("digite sua senha, senhor presidente")
    sp=str(input())
    while sp!=SPRESIDENTE:
        print("senha incorreta")
        sp=str(input())
    else:
        QC=len(LC)
        (QC)
        votos=0
        print("-----------------------------------------------------")
        print("bem-vindo senhor precidente")
        print("-----------------------------------------------------")
        input("para zerar votaçao tecle enter")
        input("votaçao zerar, tecle enter para sair senhor presidente")
print("-----------------------------------------------------")
print("|             escolha um usuario")
print("-----------------------------------------------------")
print("|              Secretário digite 1")
print("|              Presidente digite 2")
print("|                Mesario digite 3")
print("-----------------------------------------------------")
usuario=int(input())
while usuario!=3:
    print("entre como mesario para iniciar a votaçao")
    usuario=input()
else:
    sm=input("digite sua senha de mesario: ")
while SMESARIO!=sm:
    print("senha incorreta")
    sm=input("digite a senha novamente: ")
else:
    print("                                       ")
    print("bem-vindo senhor mesario")
    print("-----------------------------------------------------")
    input("para iniciar votaçao tecle enter")
print()
print("para votar digite sua senha")
se=input()
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
        lol=int(input("se sim 1 se nao 2"))
        if lol==2:
            print("")
            input()
            print("voto computado")
            print("erro")
print("votaçao encerrada")

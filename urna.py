import os
import random
senha_adm = open('senha_adm.txt', 'w')
senha_adm.write("admtse")
senha_adm.close()
senha_secretario=open('senha_secretario.txt','w')
senhadosecretario=senha_secretario.write("")
senha_secretario.close()
senha_presidente=open('senha_presidente.txt','w')
senhadopresidente=senha_presidente.write("")
senha_presidente.close()
senha_mesario=open('senha_mesario.txt','w')
senhadomesario=senha_mesario.write("")
senha_mesario.close()
senha_secretario=open('senha_secretario.txt','r')
senhadosecretario=senha_secretario.readline()
senha_secretario.close()
senha_presidente=open('senha_presidente.txt','r')
senhadopresidente=senha_presidente.readline()
senha_presidente.close()
senha_mesario=open('senha_mesario.txt','r')
senhadomesario=senha_mesario.readline()
senha_mesario.close()
print("              Bem Vindo à Urna Eletrônica")
print(                                                   ")
print("                 escolha um usuario")
print("                Administrador digite 1")
print("|               secretario digite 2")
print("|               presidente digite 3")
print("|                mesario digite 4")
usuario=nput()
um="1"
while usuario!=um:
        print("somente o administrador tem cadastro")
      
        print("              Bem Vindo à Urna Eletrônica")
        print("                                                         ")
        print("|                 escolha um usuario")
        print("                                                         ")
        print("|                Administrador digite 1")
        print("                                                         ")
        usuario=input()
else:
        senha_adm=open('senha_adm.txt','r')
        senhadoadm=senha_adm.read()
        senha_adm.close()
        s=input("digite sua senha do administrador: ")
        print()
        while s!=senhadoadm:
                print("senha incorreta")
                s=str(input("digite senha: "))
        else:
                print ("seja bv, admin")
                print("para fazer o cadastramento de secretário digite 1")
                escolha=input()
                um="1"
                while escolha !=um:
                        print("opção apenas para cadastro de secretario \n")
                        print ("digite 1 para cadastrar o secretario")
                        escolha=input()
                else:
                        print("digite uma nova senha para o secretario")
                        senhadosecretario=str(input())
                        senha_secretario=open('senha_secretario.txt', 'w')
                        senha_secretario.write(senhadosecretario)
                        senha_secretario.close()
                        print("senha cadastrada")
                
                        
input("para sair do perfil de administrador aperte Enter")
print("              Bem Vindo à Urna Eletrônica")
print("                                                     ")
print("|                 escolha um usuario")
print("                                                         ")
print("|                Administrador digite 1")
if not(senhadosecretario==""):
        print("|                Secretário digite 2")
if not(senhadopresidente==""):
        print("|                Presidente digite 3")
if not(senhadomesario==""):
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
                senha_secretario=open('senha_secretario.txt','r')
                senhadosecretario=senha_secretario.readline()
                senha_secretario.close()
                while ss!=senhadosecretario:
                        print("senha incorreta")
                        ss=str(input("digite sua senha: "))

                else:
                        print()
                        print("seja bem vindo, secretário")
                        print()
                        print("cadastro presidente")
                        print("digite a senha do presidente")
                        SPRESIDENTE=str(input())
                        senha_presidente=open('senha_presidente.txt', 'w')
                        senha_presidente.write(SPRESIDENTE)
                        senha_presidente.close()                                
                        print("cadastro presidente feito")
                        print()
                        print("                                            ")
                        print("cadastro mesario")
                        print("digite a senha do mesario")            
                        SMESARIO=str(input())
                        print("cadastro mesario realizado com sucesso")
                        print("                                      ")
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
print("**********************************")
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
    print("-----------------------------------------------------")
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

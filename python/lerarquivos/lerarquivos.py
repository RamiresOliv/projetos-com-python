import os.path
import time
import os
loop = True
while loop:
 os.system('cls')
 time.sleep(3)
 if(os.path.isfile('suport.txt')):
    arquivoread = open('suport.txt', 'r')
    for arquivoprincipalnameread in arquivoread:
        if(os.path.isfile(arquivoprincipalnameread)):
            arquivoreadname = open(arquivoprincipalnameread, 'r')
            for linha in arquivoreadname:
                print(linha)
            arquivoreadname.close()
            loop = False
        else:
            print("O arquivo não existe porfavor digite as informações do arquivo principal:")
            definirname = input('escreva o nome do arquivo')
            creat = open(definirname, 'w')
            suportedit = open('suport.txt', 'w')
            suportedit.write(definirname)
            definirvalor = input('escreva oque tera no arquivo')
            creat.write(definirvalor)
            os.system('cls')
            print("Porfavor espere Criando o arquivo...")
            time.sleep(5)
            suportedit.close()
            creat.close()
 else:
    suportestart = open('suport.txt', 'w')
    suportestart.write('arquivo=null')
    suportestart.close()
    print('Um erro foi achado tente dar start novamente')
    os.system('msg * Um erro foi achado tente dar start novamente')

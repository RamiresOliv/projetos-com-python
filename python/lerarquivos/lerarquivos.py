import os.path
import os
os.system('cls')
if(os.path.isfile('suport.txt')):
    arquivoread = open('suport.txt', 'r')
    for arquivoprincipalnameread in arquivoread:
        if(os.path.isfile(arquivoprincipalnameread)):
            arquivoreadname = open(arquivoprincipalnameread, 'r')
            for linha in arquivoreadname:
                print(linha)
            arquivoreadname.close()
        else:
            definirname = input('escreva o nome do arquivo')
            creat = open(definirname, 'w')
            suportedit = open('suport.txt', 'w')
            suportedit.write(definirname)
            definirvalor = input('escreva oque tera no arquivo')
            print("O arquivo não existe")
            creat.write(definirvalor)
            creat.close()
            suportedit.close()
else:
    suportestart = open('suport.txt', 'w')
    suportestart.write('arquivo=null')
    suportestart.close()
    print('Um erro foi achado tente dar start novamente')
    os.system('msg * Um erro foi achado tente dar start novamente')

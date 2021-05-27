import time
import os

loop = True
nome_arquivo = "suport.txt"

while loop:
 os.system('cls')
 #time.sleep(3)
 
 path_arquivo = os.path.abspath(nome_arquivo)
 
 if(os.path.isfile(path_arquivo)):
    arquivo_read = open(path_arquivo, 'r')
    
    print("Conteúdo do arquivo: ")
    for linha in arquivo_read:
        print(linha)
        
    arquivo_read.close()
    
    print("\n\nFinalizando aplicação...")
    loop = False
    
 else:
    print("O arquivo padrão não existe! \nVamos criar um novo!")
    nome_arquivo = input('Digite o nome do novo arquivo: ')
    criar_arquivo = open(nome_arquivo, 'w')

    conteudo_arquivo = input(f"Digite o conteúdo do arquivo {nome_arquivo}: ")
    criar_arquivo.write(conteudo_arquivo)
    
    os.system('cls')
    
    print("Criando arquivo, aguarde...")
    time.sleep(2)
    criar_arquivo.close()

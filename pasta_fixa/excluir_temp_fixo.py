import os
import shutil
import time
from send2trash import send2trash

def excluir_arquivos(pasta):
    if not os.path.exists(pasta):
        print(f"\nA pasta {pasta} não existe\n")
        return
    
    for item in os.listdir(pasta):
        caminho_item = os.path.join(pasta, item)

        """ if os.path.isdir(caminho_item):
            shutil.rmtree(caminho_item)
        else: """
        send2trash(caminho_item)

    print("\nTodos os arquivos foram excluídos!\n")

pastaRaiz = "C:\\Users\\UserTI\\Desktop\\raiz"
pastaTemp = "C:\\Users\\UserTI\\Desktop\\raiz\\teste-temp"
inter = 300
inicio = 17

while True:
    itens = os.listdir(pastaRaiz)
    itensTemp = os.listdir(pastaTemp)
    num_arqui = sum(1 for item in itens if os.path.join(pastaRaiz, item))
    num_arquiTemp = sum(1 for item in itensTemp if os.path.join(pastaTemp, item))

    if num_arqui > inicio and num_arquiTemp > 0:
        excluir_arquivos(pastaTemp)
    elif num_arqui > inicio and num_arquiTemp == 0:
        print(f"\nA pasta {pastaTemp} está vazia.\n")
    else:
        print(f"\nA pasta {pastaRaiz} está funcionando bem.\n")
    time.sleep(inter)
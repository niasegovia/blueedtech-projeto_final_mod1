from time import sleep
from som import som

def creditos():
    credenciais = {
        'Som de varrendo':  'usuário 170084 em freesound.org',
        'Som de cozinha': 'usuário szegvari em freesound.org',
        'Som de dormindo': 'usuário 180334__sankalp em freesound.org'
    }

    for i in credenciais.items():
        #print(f'{i[0]} por {i[1]}') 
        for letra in i[0]:
            print(letra, end="")
            sleep(0.5)
        for letra in i[1]:
            print(letra, end="")
            sleep(0.5)
creditos()
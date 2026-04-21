rua_livre = False

while not rua_livre:
    if input("Vem vindo carro? (s/n): ").lower() == 'n':
        print("Atravessando... Chegou!")
        rua_livre = True
    else:
        print("Espere o carro passar.")

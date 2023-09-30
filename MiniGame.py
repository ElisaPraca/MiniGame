Palpite = 0
numero = 2

while True:
    print("Qual o numero correto?")
    Palpite = int(input())
    if Palpite == numero:
        print("Parabens você acertou")
        break
    else:
        print('Você errou') 
else: 
    print("Erro na aplicação")
    print(bool(Palpite))

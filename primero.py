print('********************************')
print('Bem vindo ao jogo de adivinhacao')
print('********************************')

numero_secreto = 90
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
     print('Tentativa', rodada, 'de', total_de_tentativas)
     chute_str = input("Digite o seu numero: ")
     chute = int(chute_str)

     if (numero_secreto == chute):
          print ("Acertou Miseravi")
     else:
          print ("Errou Azalado")
     rodada = rodada + 1

print ('Acabou essa porra de adivinhacao')
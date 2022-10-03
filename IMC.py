massa = float(input('insira a sua massa: ')) #leitura da massa em quilos do usuario
altura = float(input('insira a sua altura em cm: ')) #leitura da altura em cm do usuario

altura = altura/100 # transforma a altura em metros

imc = massa/(altura**2) # faz o calculo do IMC

print(f'o seu IMC é de: {round(imc,1)}') # Exibe o valor do imc

if(imc < 18.5): 
    print('você está abaixo do peso')
elif(imc < 25):
    print('você está no peso normal')
elif(imc < 30):
    print('você está acima do peso')
elif(imc < 35):
    print('você está com obesidade nivel I')
elif(imc < 40):
    print('você está com obesidade nivel II')
elif(imc > 40):
    print('você está com obesidade nivel III')# IMC

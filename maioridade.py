import datetime
maiores=0
nao=0
ano=datetime.datetime.now().year
for num in range(1, 8):
    idade = int(input(f"idade da {num}ª pessoa: "))
    if (ano-idade) >= 18:
        maiores+=1
    else:
        nao+=1
print(f"{maiores} são maiores de idade, {nao} não são maiores.")

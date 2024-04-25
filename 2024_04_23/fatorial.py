fat = 1
num = int(input("Insira um número inteiro:"))
for x in range(num):
    fat = fat * (x + 1)
print("Sua fatorial é", fat)
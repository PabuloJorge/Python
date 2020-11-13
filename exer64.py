n = q = s = 0

while n != 999:
        n = int(input("Digite um número: "))
        if n != 999:
            q +=1
            s += n
print("Foram digitados {} números e a soma entre eles é {}".format(q, s))
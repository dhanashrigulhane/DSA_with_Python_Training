import random as rd
num=rd.randint(1,100)
chances=9
while chances>0:
    choice=int(input("Guess the number :"))
    if choice<num:
        print(f'You guessed too low you have only {chances} avaliable')
    elif choice>num:
        print(f'You guessed too high you have only {chances} avaliable ')
    else:
        print("congraulations!!")   
        break
    chances-=1     

# Dice Simulator by Amit 😎
import random
import time

print(f'''
Welcome to Dice game
''')

name = input("Enter your name : ")
name = name.capitalize()
print(f'Welcome {name}')

d = 1


# Creating random numbers
def random_number():
    num = random.randint(1, 6)
    return f"The number is .............. {num}!!"


# User choice question
def question_choice():
    global d
    print(f'''
        To roll dice press 1
        To exit press 0
    ''')
    d = int(input("Enter your choice : "))


while d == 1:
    question_choice()
    if d == 1:
        print("Dice is rolling...")
        time.sleep(1.5)
        print(random_number())
    elif d == 0:
        print("Thanks for using this tool...")
        exit()
    else:
        print(f"Invalid Input!! \n Error!!!! {d}")

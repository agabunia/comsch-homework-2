import random
import string

# Exc 1
def password_generator():
    length = int(input("პაროლის სიგრძე: "))

    charset = ""
    if input("დიდი ასოები? (yes/no): ").lower() == "yes":
        charset += string.ascii_uppercase
    if input("პატარა ასოები? (yes/no): ").lower() == "yes":
        charset += string.ascii_lowercase
    if input("რიცხვები? (yes/no): ").lower() == "yes":
        charset += string.digits
    if input("სპეციალური სიმბოლოები? (yes/no): ").lower() == "yes":
        charset += string.punctuation

    if not charset:
        print("მინიმუმ ერთი ტიპი უნდა აირჩიო!")
    else:
        for c in charset:
            if '\u10D0' <= c <= '\u10FF':
                print("შეიყვანე მხოლოდ ლათინური ასოები")
                break
        else:
            password = "".join(random.choice(charset) for _ in range(length))
            print("შენი პაროლია:", password)

# password_generator()


# Exc 2
# password = input("შეიყვანე პაროლი: ")
 
def password_evaluator(password):
    score = 0
 
    if len(password) >= 8:
        score += 3
    elif len(password) >= 5:
        score += 1
    
    if any(c.isdigit() for c in password):
        score += 2
    
    if any(c in string.punctuation for c in password):
        score += 3
    
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    
    if score <= 3:
        print(f"score: {score}, strength: weak")
    elif score <= 6:
         print(f"score: {score}, strength: medium")
    else:
        print(f"score: {score}, strength: strong")

# password_evaluator(password)


# Exc 3
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def fibonacci_iterative():
    while True:
        user_input = input("შეიყვანე რიცხვი: ")
    
        if not user_input.lstrip().isdigit():
            print("შენი შემოტანილი სიმბოლო არასწორია, მხოლოდ რიცხვი შეიყვანე!")
            continue
    
        n = int(user_input)
    
        if n < 0:
            print("შემოიყვანე დადებითი რიცხვი!")
            continue
    
        print(f"ფიბონაჩი({n}) =", fibonacci(n))
        break

# fibonacci_iterative()


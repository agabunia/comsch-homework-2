import random

# Exc 4
# text = input("შეიყვანე ტექსტი: ")
 
def polindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalpha())
    
    if cleaned == cleaned[::-1]:
        print("პალინდრომია!")
    else:
        print("არ არის პალინდრომი.")
        
        chars = list(cleaned)
        left = 0
        right = len(chars) - 1
        while left < right:
            chars[right] = chars[left]
            left += 1
            right -= 1
    
        suggestion = ''.join(chars)
        print(f"ახლო პალინდრომი: {suggestion}")

# polindrome(text)


# Exc 5
# word = input("Enter a word: ")

def generate_nickname(word):
    if " " in word:
        print("მხოლოდ 1 სიტყვა უნდა შეიყვანოთ")
    else:
        for _ in range(5):
            choice = random.randint(1, 3)
            num = random.randint(1, 999)
            
            if choice == 1:
                print(f"{word}{num}")
            elif choice == 2:
                print(f"{word}_{num}")
            else:
                print(f"{num}_{word}")

# generate_nickname(word)


# Exc 6
# raw = input("შეიყვანე რიცხვები გამოტოვებით: ")

def rewrite_list(raw):
    numbers = [int(x) for x in raw.split() if x.lstrip().isdigit()]
    unique = input("მხოლოდ უნიკალური? (yes/no): ").strip().lower()
    if unique == "yes":
        numbers = list(set(numbers))
    
    method = input("სორტირება: კლებადობით (k), ზრდადობით (z), random (r): ").strip().lower()
    
    if method == "k":
        result = sorted(numbers, reverse=True)
    elif method == "z":
        result = sorted(numbers)
    elif method == "r":
        random.shuffle(numbers)
        result = numbers
    else:
        result = []
        print("არასწორი არჩევანი!")
    
    if result:
        print("შედეგი:", result)

# rewrite_list(raw)
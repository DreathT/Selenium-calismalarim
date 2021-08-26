import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","w","x","q"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

normal = random.choice(letters)
big = random.choice(letters).upper()
number = random.choice(numbers)
normal2 = random.choice(letters)
big2 = random.choice(letters).upper()
number2 = random.choice(numbers)
normal3 = random.choice(letters)
big3 = random.choice(letters).upper()
number3 = random.choice(numbers)
normal4 = random.choice(letters)
big4 = random.choice(letters).upper()
number4 = random.choice(numbers)

email = [normal,big,number,normal2,big2,number2,normal3,big3,number3,normal4,big4,number4]
password = [normal,big,number,normal2,big2,number2,normal3,big3,number3,normal4,big4,number4]
password.reverse()
username = [password]
name = [password]
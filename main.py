name = input("Введіть ваше імя: ")
age = int(input("Введіть ваш вік: "))
yearsleft = 100 - age

import datetime
current_year = datetime.datetime.now().year

year100old = current_year + yearsleft

print(f"{name}, вам буде 100 років у {year100old} році.")


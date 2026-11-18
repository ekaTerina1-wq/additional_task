import json
try:
    with open("points.json", "r", encoding="utf-8") as file:
        points = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    points = []
def read_points():
    while True:
        try:
            number = int(input("Введите число от 0 до 20: "))
            if 0 <= number <= 20:
                 return number
            else:
                 print("Вне диапазона")
        except ValueError:
            print("Введен символ, введите число")
score = read_points()
print("Ваш балл:", score)
points.append(score)
with open("points.json", "w", encoding = "utf-8") as file:
    json.dump(points, file, ensure_ascii = False, indent=4)
print("История ваших баллов:")
print(points)

# Проверки:
# abc - ожидается Введите число
# фактически - Введите число

# -1 - ожидается Введите число снова
# фактически - Введите число снова

# 21 - ожидается Введите число снова
# фактически - Введите число снова

# 0 - ожидается возврат 0
# фактически - возвращается 0

# 20 - ожидается возврат 20
# фактически - возвращается 20
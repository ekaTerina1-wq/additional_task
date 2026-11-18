score = 2
def local_demo():
    score = 100
    print(score)
def add_score():
    global score
    score += 4
def outer():
    counter = 0
    def inc():
        nonlocal counter #nonlocal - показывает что берем переменную не из локальной ,
        # а из глобальной функции, без него - новая переменная
        counter += 1
    inc()
    inc()
    return counter #2
print("До вызова:", score)
local_demo()
print("После:", score)
add_score()
print("После:", score)
counter = outer()
print("После:", counter)
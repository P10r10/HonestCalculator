message = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
           "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
           "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
           "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy",
           " ... very, very lazy", "You are", "Are you sure? It is only one digit! (y / n)",
           "Don't be silly! It's just one number! Add to the memory? (y / n)",
           "Last chance! Do you really want to embarrass yourself? (y / n)"]
result = 0
memory = 0


def is_one_digit(v):
    return float(v).is_integer() and 10 > v > -10


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + message[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + message[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + message[8]
    if msg != "":
        msg = message[9] + msg
        print(msg)


def store_the_result():
    global memory
    if is_one_digit(result):
        msg_index = 10
        while True:
            print(message[msg_index])
            answer = input()
            if answer == "y":
                if msg_index < 12:
                    msg_index = msg_index + 1
                else:
                    memory = result
                    break
            elif answer == "n":
                break
    else:
        memory = result


while True:
    print(message[0])  # Enter an equation
    x, operator, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(message[1])
        continue
    else:
        if operator not in "+-*/":
            print(message[2])
            continue
        else:
            check(x, y, operator)
            if operator == "+":
                result = x + y
            if operator == "-":
                result = x - y
            if operator == "*":
                result = x * y
            if operator == "/":
                try:
                    result = x / y
                except ZeroDivisionError:
                    print(message[3])
                    continue
        print(result)
        while True:
            print(message[4])  # Do you want to store the result? (y / n):
            answer = input()
            if answer == "y":
                store_the_result()
                break
            elif answer == "n":
                break
    while True:
        print(message[5])  # Do you want to continue calculations? (y / n):
        answer = input()
        if answer == "y":
            break
        elif answer == "n":
            exit()

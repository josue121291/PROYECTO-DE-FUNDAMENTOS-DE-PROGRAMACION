y = (10 - 45)
x = 20
a = 40

if y >= 10:
    print("continuemos")
    if x == 10:
        print("incorrecto")
    elif x == 20:
        print("continuemos")
        if a > 41:
            print("incorrecto")
        elif a > 10:
            print("las condiciones son correctas")
elif y < 10:
    print("las condiciones son incorrectas")
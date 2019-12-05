try :
    a = float(input("Введите А = "))
    b = float(input("Введите B = "))
    x = float(input("Введите X = "))
    try :
        if x > 4 :
            y = (4 * pow(a, 2) + b * x) / (b + x)
        else:
            y = 3 * pow((a + b + x), 2)
        print('y = ', y)
    except:
        print("Нет решения")
except :
    print ("Неверный тип входных данных")
input('')
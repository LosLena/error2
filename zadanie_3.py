t = ['+', '-', '*', '/']
vvod =input("Введите выражение в виде польской нотации: математическкая операция и два положительных числа, разделенных пробелом: ")
spisok = vvod.split()
if len(spisok) == 3:
    list = spisok[0]
    number1 = spisok[1]
    number2 = spisok[2]
    print(spisok)
    assert list in t,"Нет такой операции" 
    try:
       if int(number1) >= 0 and int(number2) >= 0:
        if list == t[0]:
          print(f"Значение сложение {int(number1)+int(number2)}")
        elif list == t[1]:
          print(f"Значение вычитания {int(number1)-int(number2)}")
        elif list == t[2]:
          print(f"Значение умножения {int(number1)*int(number2)}")
        elif list == t[3]:
          try:
            print(f" Значение  {int(number1)/int(number2)}")
          except ZeroDivisionError:
            print("Вы ввели 0, деление на 0 невозможно") 
    except:
      print("Вы ввели не положительные числа") 
      
else:
  print("Вы ввели некорректное выражение")
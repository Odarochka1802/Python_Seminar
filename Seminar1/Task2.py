print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

flag = ''
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Треугольник есть")
        else:
            flag = 'a'
    else:
        flag = 'b'
else:
    flag = 'c'

if flag != '':
    print("Треугольника нет")
    print("'%s' > суммы других" % flag)

else:
    if a==b==c:
        print("Треугольник равносторонний")
    elif a!=b!=c:
        print("Треугольник зазносторонний")
    elif a==b or a==c or b==c:
        print("Треугольник равнобедренный")
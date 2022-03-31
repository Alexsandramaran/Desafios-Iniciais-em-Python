a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
if (a >= b+c) or (b >= a+c) or (c >= a+b):
    area = float(((a + b) * c) / 2)
    print("Area = %.1f"%(area))
else:
    perimetro = a + b + c
    print("Perimetro = %.1f"%(perimetro))
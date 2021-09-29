a=int(input("Введите число для возведения в степень"))
b=int(input("Введите степень"))
k=a
for i in range(b-1):
	a=a*k
print(a)
# Python introduction: operators and expressions
x = 10
x, y = 10, 20

x, y = y, x
x, y = y, x + y

s = "Hello, %s!" % ("world")
s = "x = %d, y = %d" % (x, y)
s = f"x = {x}, y = {y}"

x, y = 14, 6
print( "%d + %d = %f" % (x, y, x + y))
print( "%d - %d = %f" % (x, y, x - y))
print( "%d * %d = %f" % (x, y, x * y))
print( "%d / %d = %f" % (x, y, x / y))
print( "%d %% %d = %f" % (x, y, x % y))
print( "%d ** %d = %f" % (x, y, x ** y))
print( "%d // %d = %f" % (x, y, x // y))


if x > 2 and y > 2:
    print("Both x and y are greater than 2")

if x > 2 or y > 2:
    print("Either x or y is greater than 2")

if not(x > 2 and y > 2):
    print("Both x and y are not greater than 2")

if x > 2:
    print("x is greater than 2")

# ternary operator
s = 10 if x > 0 else 20; print(s)

# loops 
while y > 0:
    print(y, end=" ")
    y -= 1;
else:
    print("Loop is over")

r10 = range(10)
for i in r10:
    print(i, end=' ') # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(1,10):
    print(i, end=' ') # 1 2 3 4 5 6 7 8 9
print()

for i in range(1,10,2):
    print(i, end=' ') # 1 3 5 7 9
print()

for i in range(10,1,-2):
    print(i, end=' ') # 10 8 6 4 2
print()

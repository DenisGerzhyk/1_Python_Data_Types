# 1).

x = int(input())
x1 = x%10
x = x/10
x2 = int(x)%10
x = x/10
x3 = int(x)%10
x = x/10
x4 = int(x)%10


# x = int(input())
# print (x[::-1])


# 2).

x = int(input())

x,y = divmod(x,100)
x1,x2 = divmod(x,10)
x3,x4 = divmod(y,10)

print(x1)
print(x2)
print(x3)
print(x4)


# Training
# def foo(a):
#     return divmod(a,-11)
# a = int(input())
# print(foo(a))





your_name=input("your_name:")
your_caple_name=input("your_caple_name:")

c=set(your_name)
d=set(your_caple_name)
c.intersection_update(d)

g=len(c)

if g in [5,14,16,18,21,23]:
    f=open("word","w")
    f.write("friends")


elif g in [3,10,19]:
    f = open("word", "w")
    f.write("lover")


elif g in [8,12,13,17]:
    f = open("word", "w")
    f.write("affection")


elif g in [6,11,15,26]:

    f = open("word", "w")
    f.write("marriage")

elif g in [2,4,7,9,20,22,24,25]:

   f = open("word", "w")
   f.write("enemy")

else:

   f = open("word", "w")
   f.write("sibilings")





key = input('Enter printing a keyword: ')

f=open("word","r")
a = f.read()



value = list(a)




# b
def b():
    for row in range(7):
        for col in range(6):
            if (row == 0 and col != 4 and col != 5) or (col == 0) or (row == 6 and col != 4 and col != 5) or (
                    row == 3 and col != 4 and col != 5) or (col == 4 and row != 0 and row != 3 and row != 6):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")



# a
def a():
    for row in range(5):
        for col in range(6):
            if (col != 0 and row == 0 and col != 4 and col != 5) or (row == 2 and col != 5) or (
                    col == 0 and row != 0) or (col == 4 and row != 0):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("", end="")


# l
def l():
    for row in range(7):
        for col in range(6):
            if (col == 0) or (row == 6):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")



# u
def u():
    for row in range(4):
        for col in range(6):
            if (col == 0 and row != 3) or (row == 3 and col % 4 != 0 and col % 5 != 0) or (col == 4 and row != 3):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


# e
def e():
    for row in range(7):
        for col in range(6):
            if (row == 0 and col != 4 and col != 5) or (col == 0) or (row == 6 and col != 4 and col != 5) or (
                    row == 3 and col != 4 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


# f
def f():
    for row in range(7):
        for col in range(6):
            if (row == 0 and col != 4 and col != 5) or (col == 0) or (row == 3 and col != 4 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")



# p
def p():
    for row in range(7):
        for col in range(6):
            if (row == 0 and col != 4 and col != 5) or (col == 0) or (row == 3 and col != 4 and col != 5) or (
                    col == 4 and row != 0 and row != 3 and row != 4 and row != 5 and row != 6):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


# c
def c():
    for row in range(5):
        for col in range(5):
            if (col == 0 and row != 0 and row != 4) or (row == 0 and col != 0 and col != 4) or (
                    row == 4 and col != 0 and col != 4):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#d
def d():
    for row in range(5):
        for col in range(6):
            if (row == 0 and col != 4 and col != 5) or (col == 1) or (row == 4 and col != 4 and col != 5) or (
                    col == 4 and row != 0 and row != 4):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#g
def g():
    for row in range(5):
        for col in range(5):
            if (row == 0 and col != 3 and col != 4 and col != 5) or (col == 0) or (
                    row == 4 and col != 4 and col != 5) or (col == 3 and row != 0 and row != 1) or (
                    row == 2 and col != 1 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#h
def h():
    for row in range(5):
        for col in range(4):
            if (col == 0) or (col == 3) or (row == 2 and col != 4):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#i
def i():
    for row in range(4):
        for col in range(5):
            if (row==0)or(row==3)or(col==2):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#j
def j():
    for row in range(5):
        for col in range(5):
            if (col == 2) or (row == 0) or (row == 4 and col != 3 and col != 4 and col != 5) or (
                    col == 0 and row != 1 and row != 2):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#k
def k():
    for row in range(5):
        for col in range(4):
            if (row == 2 and col != 3 and col != 2) or (col == 0) or (
                    col == 3 and row != 1 and row != 2 and row != 3) or (
                    col == 2 and row != 0 and row != 2 and row != 4):
                print(key, end=" ")
            else:
                print(" ", end=" ")

        print()
        print("",end="")


#m
def m():
    for row in range(5):
        for col in range(7):
            if (col == 0) or (col == 6) or (row == 0 and col != 2 and col != 3 and col != 4 and col != 7) or (
                    row == 1 and col != 1 and col != 3 and col != 5 and col != 7) or (
                    col == 3 and row != 0 and row != 1 and row != 3 and row != 4):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#n
def n():
    for row in range(5):
        for col in range(5):
            if (col == 0) or (col == 4) or (row == 1 and col != 2 and col != 3 and col != 5) or (
                    row == 2 and col != 1 and col != 3 and col != 5) or (
                    row == 3 and col != 1 and col != 2 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#o
def o():
    for row in range(5):
        for col in range(5):
            if (col == 0 and row != 0 and row != 4) or (col == 4 and row != 0 and row != 4) or (
                    row == 0 and col != 0 and col != 4 and col != 5) or (
                    row == 4 and col != 0 and col != 4 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")

#q
def q():
    for row in range(6):
        for col in range(5):
            if (col == 0 and row != 0 and row != 4 and row != 5) or (col == 4 and row != 0 and row != 4) or (
                    row == 0 and col != 0 and col != 4 and col != 5) or (
                    row == 4 and col != 0 and col != 4 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")

#r
def r():
    for row in range(7):
        for col in range(6):
            if (row == 0 and col != 4 and col != 5) or (col == 0) or (row == 3 and col != 4 and col != 5) or (
                    col == 4 and row != 0 and row != 3 and row != 4 and row != 5 and row != 6) or (
                    row == 4 and col != 2 and col != 3 and col != 4 and col != 5) or (
                    row == 5 and col != 1 and col != 3 and col != 4 and col != 5) or (
                    row == 6 and col != 1 and col != 2 and col != 4 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


#s
def s():
    for row in range(7):
        for col in range(5):
            if (row == 0 and col != 0) or (row == 6 and col != 4) or (row == 3 and col != 0 and col != 4) or (
                    col == 0 and row != 0 and row != 3 and row != 4 and row != 5) or (
                    col == 4 and row != 1 and row != 2 and row != 3 and row != 6):
                print(key, end=" ")
            else:
                print(" ", end=" ")

        print()
        print("",end="")


#t
def t():
    for row in range(7):
        for col in range(5):
            if (row == 0) or (col == 2):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")

#v
def v():
    for row in range(5):
        for col in range(5):
            if (col == 0 and row != 3 and row != 4) or (col == 4 and row != 3 and row != 4) or (
                    row == 3 and col != 0 and col != 2 and col != 4 and col != 5) or (
                    col == 2 and row != 0 and row != 1 and row != 2 and row != 3):
                print(key, end=" ")
            else:
                print(" ", end="   ")
        print()
        print("",end="")

#w
def w():
    for row in range(4):
        for col in range(5):
            if (col == 0 and row != 3) or (col == 1 and row != 0 and row != 1 and row != 2) or (
                    col == 2 and row != 0 and row != 3) or (col == 3 and row != 0 and row != 1 and row != 2) or (
                    col == 4 and row != 3):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")

#x
def x():
    for row in range(5):
        for col in range(5):
            if (col == 0 and row != 1 and row != 2 and row != 3) or (
                    col == 1 and row != 0 and row != 2 and row != 4) or (
                    col == 2 and row != 0 and row != 1 and row != 3 and row != 4) or (
                    col == 4 and row != 1 and row != 2 and row != 3) or (
                    col == 3 and row != 0 and row != 2 and row != 4):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")

#y
def y():
    for row in range(5):
        for col in range(5):
            if (col == 2 and row != 0 and row != 1) or (
                    row == 0 and col != 1 and col != 2 and col != 3 and col != 5) or (
                    row == 1 and col != 0 and col != 2 and col != 4 and col != 5):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")

#z
def z():
    for row in range(4):
        for col in range(4):
            if (row == 0) or (row == 3) or (col == 1 and row != 1) or (col == 2 and row != 2):
                print(key, end=" ")
            else:
                print(" ", end=" ")
        print()
        print("",end="")


for mm in value:
    eval(mm + '()')
    print('\t\t  ')
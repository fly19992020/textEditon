a = """"""
th = 0
file = open(input("Enter the address of the file to be imported>>"), "w")
print("________________________________________")


while True:
    th += 1
    n = input(str(th) + " ")
    if n == "q":
        file.write(a)
        break
    else:
        a += "\n" + n

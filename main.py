th = 0
file = open(input("Enter the address of the file to be imported>>"), "w")
print("__________")
strs = {}    #head


def h(a):
    s = input(str(a))
    strs[a] = s
    return 0


while True:
    th += 1
    n = input(str(th) + " ")
    if n == "QUIT":
        break
    elif n[0] == "i":
        h(n[1:])
        th -= 1
    else:
        strs[str(th)] = n  #main


for a in strs:
    file.write(strs[a])
    file.write("\r")    #write

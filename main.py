a = """"""
th = 0
file = open(input("请输入要保存的文件>>"), "w")


while True:
    th += 1
    n = input(str(th) + " ")
    if n == "q":
        file.write(a)
        break
    else:
        a += "\n" + n

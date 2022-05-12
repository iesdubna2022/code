arg1 = ["my", "name", "is", "Masha"]
arg2 = ["my", "name", "is", "Zhenya"]

def sovpad(arg1, arg2):
    arg_rez = []
    for i in range(len(arg1)):
        if arg1[i] in arg2:
            arg_rez.append(arg1[i])
    return arg_rez

rezult = sovpad(arg1, arg2)
print(rezult)
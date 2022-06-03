arg = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]

def slowar(arg):
    args = {}
    for i in range(len(arg)):
        if arg[i] not in args:
            args[arg[i]] = [i,]
        else:
            args[arg[i]].append(i)
    return args

rezult = slowar(arg)
print(rezult)
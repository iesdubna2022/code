arg = ["aaa", "aaa", "bbb", "ccc", "bbb"]

def slow_raz(arg):
    args = {}
    for i in range(len(arg)):
        if arg[i] not in args:
            args[arg[i]] = 1
        else:
            args[arg[i]] = args.get(arg[i], 0) + 1
    
    return args

rezult = slow_raz(arg)

print(rezult)
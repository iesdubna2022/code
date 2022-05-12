arg = ["a", "ab", "abc"]

def sredn(arg):
    return sum(len(w) for w in arg) / float(len(arg))

rezult = sredn(arg)
print(rezult)
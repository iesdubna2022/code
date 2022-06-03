arg = ["abcd", "a", "ab", "abc", "bazinga", "bar"]

def sort_mas(arg):
    return sorted(arg, key = len)

result = sort_mas(arg)
print(result)
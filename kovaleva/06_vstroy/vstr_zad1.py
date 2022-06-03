res = [
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"],
    [],
    ["Hello"],
]

new_resg = {res[i][1] : res[i][0] for i in range(0, len(res)) if len(res[i]) > 1}
print(new_resg)
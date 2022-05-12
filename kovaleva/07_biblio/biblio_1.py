text = """Мы одновременно летим и падаем и это неизбежно"""
text_mass = text.split()

print(text_mass)
args = {}
for i in text_mass:
    if i not in args:
        args[i] = 0

    args[i] += 1        

print(args)
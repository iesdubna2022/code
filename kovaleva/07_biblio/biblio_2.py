def cache(dit):
    cached = {}
    def func(key):
        cached[key] = dit(key)
        return cached[key]
    return func


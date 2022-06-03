def partial(func, /, *args, **keywords):
    def funcis(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
    
        return func(*args, *fargs, **newkeywords)
    
    funcis.func = func
    funcis.args = args
    funcis.keywords = keywords
    
    return funcis

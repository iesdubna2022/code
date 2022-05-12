def bread(item):
    def function(whats):
        print("bread")
        item(whats)
        print("bread")
    return function

def vegitables(item):
    def function(whats):
        print("tomatos")
        item(whats)
        print("salad")
    return function

def mayonnaise(item):
    def function(whats):
        print("mayonnaise")
        item(whats) 
    return function

@bread
@mayonnaise
@vegitables
def sandwich(what):
    print(what)

sandwich("ham")
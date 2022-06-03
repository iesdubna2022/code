class Studend:
    
    def __init__(self, first_name, second_name, major_subject = "engineering"):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject
        
    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")

def priem(**kwargs):
    if "first_name" and "second_name" and "major_subject" in kwargs:
        a = Studend(kwargs["first_name"], kwargs["second_name"], kwargs["major_subject"])
        a.print()

    elif "first_name" and "second_name" in kwargs:
        a = Studend(kwargs["first_name"], kwargs["second_name"])
        a.print()

priem(first_name = 'Далина', second_name = 'снов')



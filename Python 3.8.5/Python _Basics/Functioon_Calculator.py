print("Thsi A Program for Calclator")
def Calculator():
    In1 = float(input("Enter The First Integer"))
    In2 = input("Enter Add, Sub, Multi, Div")
    In3 = float(input("Enter The Second Integer"))

    def Add (a, b):
        
        c = a +b
        print(c)
    def Sub (a, b):
        c = a - b
        print(c)
    def Multi (a, b):
        c = a * b
        print(c)
    def Div (a,b):
        c = a / b
        print(c)

    if In2 == "Add":
        Add(In1, In3)
    elif In2 == "Sub":
        Sub(In1, In3)
    elif In2 == "Multi":
        Multi(In1, In3)
    elif In2 == "Div":
        Div(In1, In3)           

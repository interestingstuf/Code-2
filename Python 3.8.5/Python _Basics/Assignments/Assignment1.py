while True:
    nhl = input("Enter the stop light")

    if nhl == "Red":
        print("STOP!")
    elif nhl == "Yellow":
        print("Slow!")


    elif nhl == "Green":
        print("Go!") 
    elif nhl == "Close":
        break   
    else:
        print("That Is Not A Stoplight Color") 

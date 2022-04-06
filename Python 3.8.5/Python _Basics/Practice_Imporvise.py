Fruit = ["Apple","Watermelon","Orange","Pear"]
Veggie = ["Corn","carrots","beans"]
Apple_Products = ["Iphone","Mac","Watch"]



supermarket = [Fruit, Veggie, Apple_Products]
categories = ["Fruit", "Veggie", "Apple Products"]
basket = []
print("Welcome, We Sell These Categories ", categories)
print("Please select one of the cartegories")
while True:
   
    catergory1 = input("Enter The Catergory You Want To Shop In")
    if catergory1 == ("Fruit"):
        print(Fruit)
        item1 = input("Enter Item From Super Market")
        if item1 in Fruit:

            basket.append(item1)
            Fruit.remove(item1)
        else:
            print("We Are Out Of Stock")    
        print("In your basket there is: ",basket)
        print("The Categories That Are Left In This Section are: ",Fruit)
        #if Fruit == []:
            #print("We are out of stock of", catergory1)
    elif catergory1 == ("Veggie"):
        print(Veggie)
        item1 = input("Enter Item From Super Market")
        basket.append(item1)
        Veggie.remove(item1)
        print("In your basket there is: ",basket)
        print("The Categories That Are Left In This Section are: ",Veggie)
        if Veggie == []:
            print("We are out of stock of", catergory1)
    elif catergory1 == ("Apple Products"):
        print(Apple_Products)
        item1 = input("Enter Item From Super Market")
        basket.append(item1)
        Apple_Products.remove(item1)
        print("In your basket there is: ",basket)
        print("The Categories That Are Left In This Section are: ",Apple_Products)
        if Apple_Products == []:
            print("We are out of stock of", catergory1)
    else:
        print("We Dot Not Sell This: ", catergory1)
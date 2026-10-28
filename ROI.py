


def Get_Price():
    while True:
        price1 = input("How much was the item that you bought? (Please type in 00.00 format.): ")
        try:
            number = float(price1)
            break
        except ValueError:
            print("Please only type the number in 00.00 format!")
    print()
    print(f"Awesome, so it costed: ${number} Dollars.")

    return number

print()

print("Hello, Elias! Thrift some new things? Let's get those numbers looking right for ya!")

print()

####

A = "Clothing"
B = "Art"
C = "Shoes"
print()
def Typa_Item():
    while True:
        print()
        item = input("Was the item:\n\nA. Clothing\nB. Art\nor C. Shoes?\n(Please put either A, B or C. Do not include the period.):")

        if item == "A":
            print()
            print(f"So it's: {A}!")
            print()
            return A
            break
        elif item == "B":
            print()
            print(f"So it's: {B}!")
            print()
            return B
            break
        elif item == "C":
            print()
            print(f"So it's: {C}!")
            print()
            return C
            break
        else:
            print()
            print("ERROR : 404 --> Please make sure you only input A, B or C! Please try again.")
            print()

pricee = Get_Price()
itemm = Typa_Item()

print(f"Okay, so you spent {pricee} and it was {itemm}")
print()

###

def idealPrice(priceee):
    theGoodPrice = (priceee) + (priceee/100 * 300)
    return theGoodPrice

percentageUp = idealPrice(pricee)

print(f"Ideally, you want to sell the {itemm} for {percentageUp} or above to make a 300% profit or more!")
print()
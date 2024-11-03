#Assignments

print("Assignment 3")
print("")

print("Exercise 1:")
print("")


def recursive_binarySearch(grades, num1, start, end):
    
    if start > end:
        return False
    
    mid = (start + end)//2

    if grades[mid] == num1:
        return True
    
    elif grades[mid] > num1:
        return recursive_binarySearch(grades, num1, start, mid - 1)

    else:
        return recursive_binarySearch(grades, num1, mid + 1, end)

grades = [5 ,25 ,39 ,56 ,67 ,75 ,90]

print(recursive_binarySearch(grades, 100, 0, len(grades) - 1))
print(recursive_binarySearch(grades, 75, 0, len(grades) - 1)) 

print("")
print("Exercise 2:")
print("")


def findCharcters(charcters, num2 ,reCharcters):
    if num2 == 0:
        print(reCharcters)
        return
    
    for i in charcters:
       findCharcters(charcters, num2 - 1, reCharcters + i)

charcters = ["a","b","c"]

findCharcters(charcters, 2 , "")

print("")
print("Exercise 4:")
print("")

def add_to_sort(integers, int1_4):

    for min in range(0, len(integers)):
        if int1_4 <= integers[min]:

            integers.insert(min, int1_4)
            return integers

    integers.appeend(int1_4)
    return integers

print(add_to_sort([1,2,4,6,32,45,76,99,110] , 55))    
print(add_to_sort([1,2,4,6,32,45,76,99,110,120,122,140] , 460))    


print("")
print("Exercise 3:")
print("")

items = {
    "123456": {"name": "Cupcake", "price": 30},
    "234567": {"name": "Cheesecake", "price": 120},
    "345678": {"name": "Juice", "price": 20},
    "456789": {"name": "Darkblue", "price": 50},
    "536789": {"name": "Snips", "price": 30},
    "454589": {"name": "Master", "price": 30}
}

def askReceipt():
    while True:
        puechase = input("Do you want to make a new purchase?")
    
        if puechase.lower() not in ("yes" , "no"):     
            print("This option is  unavailable. Please try again.")

        elif puechase.lower() == "no":
            print("Purchase cancelled.")
            return
        
        else:
            handleReceipt()

def handleReceipt():
    receipt = []

    while True:
        barcode = input("Enter the barcode of the item you want: ").strip()

        if barcode not in items:
            print("Barcode not found. Please try again.")
            continue
        
        item_name = items[barcode]["name"]
        item_price = items[barcode]["price"]
        print(f"You've selected {item_name} of Price {item_price}")

        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item_name}:"))
                if quantity <= 0:
                    print("Negative amount does't work")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        item_total = quantity * item_price
        receipt.append({"name": item_name, "quantity": quantity, "price": item_price, "total_price": item_total})


        while True:
            add_item = input("Would you like to add another item?").strip()

            if add_item.lower() == "yes":
                break

            elif add_item.lower() == "no":
                printReceipt(receipt)
                return
        
            else: 
                 print("This option is unavailable. Please try again.")

            
def printReceipt(receipt):
    total_amount = 0
    print("\n--- Receipt ---")

    for item in receipt:
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        total_price = item["total_price"]

        print(f"{name}: {quantity} x {price} = {total_price}")
        total_amount += total_price

    print(f"Total amount: {total_amount}")
    print("--- End of receipt ---\n")

askReceipt()
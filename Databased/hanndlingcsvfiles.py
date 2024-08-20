from os import path
import csv
from userinput import keyboardInput

filename = "products.csv"

def create(filename):
    if not path.exists(filename):
        try:
            handler = open(filename, "xt")
            handler.close()
            createColumns(filename)
        except:
            print("Sorry unable to create the file")

def createColumns(filename):
    try:
        with open(filename, "wt", newline='') as handler:
            csv_writter = csv.writer(handler, delimiter="|")
            csv_writter.writerow(["Product Name", "Quantity", "Price"])
    except:
        print("Not able to create the column header")

def createProducts(filename):
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    try:
        with open(filename, "at", newline='') as handler:
            csv_writter = csv.writer(handler, delimiter="|")
            csv_writter.writerow([productname, quantity, price])
    except:
        print("Not able to append a product")

def listProducts(filename):
    try:
        with open(filename, "rt") as handler:
            csv_reader = csv.reader(handler, delimiter="|")
            print("=" * 67)
            for index, data in enumerate(csv_reader):
                product, quantity, price = data
                if (index == 0):
                    print(f"{product:40s}{quantity:>12s}{price:>15s}")
                    print("=" * 67)
                else:
                    print(f"{product:40s}{int(quantity):12d}{float(price):15.2f}")
            print("=" * 67)
    except Exception as e:
        print("Not able to read the file", e)

def editProduct(filename):
    try:
        with open(filename, "rt") as handler:
            reader = csv.reader(handler, delimiter="|") # list of lists
            csv_reader = list(reader)
        producttoedit = keyboardInput("Enter product to edit: ", str, "Product must be string")
        productindex = None
        for index, item in enumerate(csv_reader):
            product, quantity, price = item
            if (product == producttoedit):
                productindex = index
                break
        if (productindex != None):
            productname = keyboardInput(f"Product Name [{product}] : ", str, "Product Name must be String", product)
            quantity = keyboardInput(f"Quantity [{quantity}]: ", int, "Quantity must be Integer", quantity)
            price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
            csv_reader[productindex] = [productname, quantity, price]
            with open(filename, "wt", newline='') as handler:
                csv_writter = csv.writer(handler, delimiter="|")
                csv_writter.writerows(csv_reader)
        else:
            print("Product not found")
    except Exception as e:
        print("An error occured while updating the product", e)

def deleteProduct(filename):
    try:
        with open(filename, "rt") as handler:
            reader = csv.reader(handler, delimiter="|") # list of lists
            products = list(reader)            
        producttoedit = keyboardInput("Enter product to delete: ", str, "Product must be string")
        productindex = None
        for index, item in enumerate(products):
            product, quantity, price = item
            if (product == producttoedit):
                productindex = index
                break
        if (productindex != None):
            print(f"Product: {product}")
            print(f"Quantity: {quantity}")
            print(f"Price: {price}")
            confirm = keyboardInput("Are you sure (Y/N): ", str, "Confirm must be string")
            if (confirm == "Y"): 
                del products[productindex]
                with open(filename, "wt", newline='') as handler:
                    csv_writter = csv.writer(handler, delimiter="|")
                    csv_writter.writerows(products)
        else:
            print("Product not found")
    except Exception as e:
        print("An error occured while deleting the product", e)

def doMenu():
    choice = -1
    while (choice != 0):
        print("======================")
        print("| 1. List Products   |")
        print("| 2. Create Product  |")
        print("| 3. Edit Product    |")
        print("| 4. Delete Product  |")
        print("| 0. Exit            |")
        print("======================")
        choice = keyboardInput("Enter your choice: ", int, "Choice must be Integer")
        if (choice == 1):
            listProducts(filename)
        elif (choice == 2):
            createProducts(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)
        elif (choice == 0):
            print("Thank you")
        else:
            print("Choice can be [0, 1, 2] only")

create(filename)
doMenu()
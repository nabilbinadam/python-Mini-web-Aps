# 1. Open or Create a file
# 2. Write into the file
# 3. Read from the file
# 4. Close the file (not delete)

# Why we have to close the file ?

# If you open the file and did not close the file
# operating system will not let any other process
# to open that file. So you must close after you
# use that file

# To handle the files there are various modes
# You have to open the file with specific mode
# 1. To create a file you have to use the mode (x) 
# When you use the mode (x) python create the specified file. 
# If the file already exists it will throw us an error
# 2. To write into a file we have use the mode (w)
# When we use the mode (w) if the file does not exists
# python will create it. But if the file already exists
# python will erase the content inside the file and opens it
# 3. To append data inside the file we have to use the mode (a)
# When we use the mode (a) if the file does not exists
# python will create it. If the file already exists 
# it will not erase the content inside the file.
# 4. To read data inside the file we have to use the mode (r)


# we do have some extra modes
# 1. t stands for text file
# 2. b stands for binary file



import mysql.connector as mysql



def getDbConnection(host,username,password,database):
    # In python to open a file we have a built in function called open
    # open built in function takes 2 parameters filename, mode
    # if the file already exist it throw us the error
    # opening a file is an I/O operation
    
        connection=mysql.connect(
            host= host,
            user = username,
            password=password,
            database=database
        )
        return connection
        


def createProducts(filename):
    # Let us take input from the user and append the data inside the file
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
     try:
     SQL = f """ INSERT INTO products (name,quantity,price)
     VALUES ('{productname}',{quantity},{price}) """
     cursor = connection.cursor()
     cursor.execute(SQL)
     cursor.commit()        
     except:
    print("Not able to append a product")
'''
def listProducts(connection):
    try:
            SQL = "SELECT id,name,quantity,price FROM products"
            cursor= connection.cursor()
            cursor.execute(SQL)
            print("=" * 67)
            print(f"{'Id':10s}{'Name':>40s}{'Quantity':>15s}{'Price':>20s}")
            print("=" * 67)
            for id,name,quantity,price in cursor:
                print(f"{int(id):10d}{name:>40s}{int(quantity):>15s}{float(price):>20s}")
                print("=" * 67)
    except Exception as e:
        print("Not able to read the file", e)
'''
def editProduct(connection):
    try:
        # open the file in read mode and get all the products
        with open(filename, "rt") as handler:
            products = handler.readlines()
        # find the index of the product which we want to edit
        producttoedit = keyboardInput("Enter product to edit: ", str, "Product must be string")
        productindex = None
        for index, item in enumerate(products):
            product, quantity, price = item.strip().split("|")
            if (product == producttoedit):
                productindex = index
                break
        if (productindex != None):
            # Get the product details and update the list
            productname = keyboardInput(f"Product Name [{product}] : ", str, "Product Name must be String", product)
            quantity = keyboardInput(f"Quantity [{quantity}]: ", int, "Quantity must be Integer", quantity)
            price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
            products[productindex] = f"{productname}|{quantity}|{price}\n"
            with open(filename, "wt") as handler:
                handler.writelines(products)
        else:
            print("Product not found")
    except Exception as e:
        print("An error occured while updating the product", e)
        
        
def deleteProduct(filename):
    try:
        # open the file in read mode and get all the products
        with open(filename, "rt") as handler:
            products = handler.readlines()
        # find the index of the product which we want to edit
        producttoedit = keyboardInput("Enter product to edit: ", str, "Product must be string")
        productindex = None
        for index, item in enumerate(products):
            product, quantity, price = item.strip().split("|")
            if (product == producttoedit):
                productindex = index
                break
        if (productindex != None):
            print(f"Product:{product}")
            print(f"Quantity:{quantity}")
            print(f"Price:{price}")
            confirm = ("Are you sure (Y/N)",str,"Confirm must be string")
            if (confirm=="Y"):
                del product[productindex]
            with open(filename, "wt") as handler:
                handler.writelines(products)
        else:
            print("Product not found")
    except Exception as e:
        print("An error occured while updating the product", e)
        
                

def doMenu(connection):
    choice = -1
    while (choice != 0):
        print("======================")
        print("| 1. List Products   |")
        print("| 2. Create Product  |")
        print("| 3. Edit Product    |")
        print("| 4. Delete Product    |")
        print("| 0. Exit            |")
        print("======================")
        choice = keyboardInput("Enter your choice: ", int, "Choice must be Integer")
        if (choice == 1):
           # listProducts(connection)
           pass
        elif (choice == 2):
           # createProducts(connection)
           pass
        elif (choice == 3):
          #  editProduct(connection)
          pass
        elif (choice == 4):
          #  deleteProduct(connection)
          pass
        elif (choice == 0):
           # print("Thank you")
           pass
        else:
            print("Choice can be [0, 1, 2] only")

connection = getDbConnection("localhost","root","ecatalog")
doMenu(connection)
from  import keyboardInput
from pymongo import MongoClient 
from bson.objectid import ObjectId

def getDbConnection(host, username, password, database):
    connection = MongoClient("mongodb:localhost:27017")
    db= connection("ecatalog")
    return db

def createProducts(connection):
    db = db['products']
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    try:
        
        connection.insert_one(db)

def listProducts(connection):
    try:
        SQL = "SELECT id, name, quantity, price FROM products"
        # In python to executed SQL you must create cursor from the connection
        cursor = connection.cursor()
        cursor.execute(SQL)
        # now the data is in the cursor
        print("=" * 85)
        print(f"{'Id':10s}{'Name':40s}{'Quantity':>15s}{'Price':>20s}")
        print("=" * 85)
        for document in collection.find():
            print(f"{int(id):<10d}{name:40s}{int(quantity):15d}{float(price):20.2f}")
        print("=" * 85)
    except Exception as e:
        print("Not able to read the file", e)

def editProduct(connection):
    productid = keyboardInput("Enter product id: ", int, "Product Id must be integer")
    SQL = f"SELECT id, name, quantity, price FROM products WHERE id = {productid}"
    cursor = connection.cursor()
    cursor.execute(SQL)
    try:
        (id, name, quantity, price) = cursor.fetchone()
    except:
        print("Product for this Id does not exists")
    else:
        name = keyboardInput(f"Product Name [{name}] : ", str, "Name must be String", name)
        quantity = keyboardInput(f"Quantity [{quantity}]: ", int, "Quantity must be Integer", quantity)
        price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
        SQL = f"""UPDATE products SET name = '{name}', quantity = {quantity}, price = {price}
                    WHERE id = {id}"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()

def deleteProduct(connection):
    productid = keyboardInput("Enter product id: ", int, "Product id must be integer")
    SQL = f"SELECT id, name, quantity, price FROM products WHERE id = {productid}"
    cursor = connection.cursor()
    cursor.execute(SQL)
    try:
        (id, name, quantity, price) = cursor.fetchone()
    except:
        print("Product for this Id does not exists")
    else:        
        print(f"Product: {name}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")
        confirm = keyboardInput("Are you sure (Y/N): ", str, "Confirm must be string")
        if (confirm == "Y"):
            SQL = f"DELETE FROM products where id = {id}"
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

def doMenu(connection):
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
            listProducts(connection)
        elif (choice == 2):
            createProducts(connection)
        elif (choice == 3):
            editProduct(connection)
        elif (choice == 4):
            deleteProduct(connection)
        elif (choice == 0):
            print("Thank you")
        else:
            print("Choice can be [0, 1, 2] only")
"""
db = getDbConnection("ecatalog")
doMenu(connection)
from os import path 
from userinput import keyboardInput


filename = "product.dat"

if not path.exists(filename):
    
    try:
        handler=open(filename,"xt")
        handler.close()
        
    except: 
          print("SOrry unable to create the file")
          
          
          
    try:
        with open(filename,"wt") as handler:
            handler.writer("Product Name|Quantity|Price")
        
    except:
        print("Not able to create the column header") 
        
productname = keyboardInput("Product Name:",str,"Product Name must be string")
quantity = keyboardInput("Quantity :",int,":Quantity must be Integer")
price= keyboardInput("Price:",float,"Price must be float")

try:
    with open(filename,"at") as handler:
        handler.write(f"{productname}|{quantity}|{price}")
                
except:
    print("Not able to append a product")                
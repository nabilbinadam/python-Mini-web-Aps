#let us open
filename="armor.bmp"
outputfilename="try.bmp"
with open(filename,"rb")as handler:
    file_header=handler.read(14)
    print(type(file_header))
    file_type = file_header[0:2].decode()
    print(file_type)
    
    
    file_size=int.from_bytes(file_header[2:6],'little')
   
    print("File Size:",file_size)
    reserved_one = int.from_bytes(file_header[6:8],'little')
    reserved_two = int.from_bytes(file_header[8:10],'little')
    offset = int.from_bytes(file_header[10:14],'little')
    
    print("reserved_one",reserved_one)
    print("reserved_two",reserved_two)
    print("offset:",offset)
    
    dip_header=handler.read(40)
    dip_size = int.from_bytes(dip_header[0:4],'little')
    
    print("DIP size:",dip_size)
    
    width= int.from_bytes(dip_header[4:8],'little')
    height= int.from_bytes(dip_header[8:12],'little')
    print("Image Size:",width,"x",height)
    
    planes =int.from_bytes(dip_header[12:14],'little')
    bit_count=int.from_bytes(dip_header[14:16],'little')
    print("Bits per pixel:",bit_count)
    
    
    unpadded_row_size = (width *(bit_count//3))
    row_size = ((width*(bit_count//3)+3))&~3
    print("Row size (in bytes):",row_size)
    
    pixel_data = []
    handler.seek(offset)
    for index in range(height):
        row =handler.read(row_size)
        pixel_data.append(row)
        
 #let us increase the brightness of the image
    bytes_per_pixes= bit_count//8
                
    for y in range(height):
        #bmp images are bottoms up
        new_row = bytearray() 
        row=pixel_data[height-y-1]
        for x in range(width):
            start_index =x * bytes_per_pixes
            end_index=start_index + bytes_per_pixes
            pixel=row[start_index:end_index]
            if (len(pixel)==3):
             b,g,r=pixel 
             r=min(255,int(r*510))
             g=min(255,int(r*510))
             b=min(255,int(r*510))
             new_row.extend((b,g,r))
        pixel_data[height-y-1]=new_row    
        
with open(outputfilename,"wb")as handler:
    handler.write(file_header)
    handler.write(dip_header)
    for row in pixel_data:
        handler.write(row.ljust(row_size, b'\x00'))
        
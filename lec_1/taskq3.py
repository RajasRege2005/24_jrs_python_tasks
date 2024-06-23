Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
brand=[]
os=[]
for i in Computers:
    choice=Computers[i]["brand"]
    brand.append(choice)

for i in Computers:
    choice=Computers[i]["OS"]
    os.append(choice)    
print(brand)    
print(os)
#3.write a python program to print even and odd numbers seperatly in list.
product = [33,15,101,250,230,256,500,600,700]
new_product = []
for num in product:
    if num % 2 !=0:
        new_product.append(num)
        print(new_product)


def calculate_discount(price,discount):
    if discount>=20:
        final_price = price-price*(discount/100)
        return final_price
    else:
        final_price = price
        return final_price
       
        
price = int(input("Enter the price:  "))
discount = int(input("Enter the discount:  "))
final_price = calculate_discount(price,discount)
print(f'the final price is : {final_price}')







        
   
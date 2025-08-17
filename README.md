

# 🛒 Discount Calculator 🎉



## Overview 🚀

This simple Python program helps you calculate the final price of an item after applying a discount! No more guessing—just enter your price and discount, and let the code do the math for you! 🧮

***

## How It Works 🤔

1. 🏷️ **Enter the price** of your item
2. 🎯 **Enter the discount percentage**
3. ✅ Get your **final price** instantly!

***

## Example Usage 💻

```python
def calculate_discount(price, discount):
    if discount >= 20:
        final_price = price - price * (discount / 100)
        return final_price
    else:
        final_price = price
        return final_price

price = int(input("Enter the price:  "))
discount = int(input("Enter the discount:  "))
final_price = calculate_discount(price, discount)
print(f'The final price is : {final_price}')
```

***

## Why Use It? 🤩

- Save time ⏰
- Avoid manual calculations 🏃♂️
- Get accurate results every time ✔️

***

## Try It Yourself! ✨

- Clone the repo  
- Run the script  
- Enjoy smart shopping 🎁

Happy coding & happy shopping! 🛍️

***

(see the generated image above)

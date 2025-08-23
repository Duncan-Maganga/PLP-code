def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price.

    Parameters:
    price (float): Original price of the item.
    discount_percent (float): Discount percentage to be applied.

    Returns:
    float: Price after discount.
     """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else: 
        return price
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Lets calculaate the final price

    final_price = calculate_discount(original_price, discount_percent)

    # Lets display the result

    if discount_percent >= 20:
        print(f"Original price: {original_price:}")
        print(f"Discounted applied: {discount_percent}%")
        print(f"Final price after discount: {final_price}")
    else:
        print(f"No discount applied. final price: {final_price}")
except ValueError:
    print("Invalid input! Please enter numeric value")
    






    
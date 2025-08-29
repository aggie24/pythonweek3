def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    price (float): The original price
    discount_percent (float): The discount percentage (e.g., 20 for 20%)
    
    Returns:
    float: The final price after discount if discount is 20% or higher,
           otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    1
    # Calculate final price using the function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display the result
    if discount_percentage >= 20:
        print(f"Original price: ${original_price:.2f}")
        print(f"Discount applied: {discount_percentage}%")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"No discount applied (discount must be 20% or higher)")
        print(f"Original price: ${original_price:.2f}")
        
except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
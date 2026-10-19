def calculate_subtotal(itmes):
    subtotal=0
    for item in itmes:
        price=item["price"]
        quantity=item["quantity"]
        
        if price < 0:
            raise ValueError(f"Invalid price for item '{item['name']}': {price}. Price cannot be negative.")
        if quantity < 0:
            raise ValueError(f"Invalid quantity for item '{item['name']}': {quantity}. Quantity cannot be negative.")

        subtotal += price * quantity
    
    
    
    return subtotal
    
def calculate_discount(subtotal):
    
    if subtotal >= 3000:
        rate = 0.10
    elif subtotal >= 1000:
        rate = 0.05
    else:
        rate = 0.0

    return subtotal * rate 


def calculate_tax(amount,tax_rate):
    
    if tax_rate < 0:
        raise ValueError(f"Invalid tax rate: {tax_rate}. Tax rate cannot be negative.")

    return amount * tax_rate
    
    
    
def generate_receipt(items,tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    
    # Tax is typically calculated on the discounted amount
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount, tax_rate)
    final_amount = taxable_amount + tax

    # Display receipt breakdown
    print("=" * 35)
    print(f"{'SHOPPING RECEIPT':^35}")
    print("=" * 35)
    for item in items:
        line_total = item["price"] * item["quantity"]
        print(f"{item['name']:<15} {item['quantity']:>3} x {item['price']:>7.2f} = {line_total:>8.2f} Birr")
    
    print("-" * 35)
    print(f"{'Subtotal:':<22} {subtotal:>10.2f} Birr")
    print(f"{'Discount:':<22} -{discount:>9.2f} Birr")
    print(f"{f'Tax ({tax_rate * 100:.0f}%):':<22} {tax:>10.2f} Birr")
    print("=" * 35)
    print(f"{'Final Amount:':<22} {final_amount:>10.2f} Birr")
    print("=" * 35)

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount,
    }
items=[
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5},
    {"name": "Textbook", "price": 950, "quantity": 3}
]
    
generate_receipt(items, tax_rate=0.15)
  
        
        
        
  
    

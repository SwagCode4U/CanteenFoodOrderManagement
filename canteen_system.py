"""
🍔 CANTEEN FOOD ORDER SYSTEM
====================
A simple and relatable food ordering system for students.
Browse menu, place orders, and generate bills instantly!

Author: Coders Jaunt by @mit
Purpose: Teaching Python basics (dictionaries, lists, loops, math)
"""

# Import datetime for order timestamps
from datetime import datetime

# ============================================================================
# GLOBAL DATA STRUCTURES
# ============================================================================

# Menu Item Database
# Nested Dictionary: Category -> Item -> Price
MENU = {
    'Snacks': {
        'Samosa': 15,
        'Sandwich': 50,
        'Burger': 60,
        'Fries': 40
    },
    'Beverages': {
        'Tea': 10,
        'Coffee': 20,
        'Cold Drink': 40,
        'Milkshake': 70
    },
    'Meals': {
        'Veg Thali': 120,
        'Fried Rice': 90,
        'Noodles': 80,
        'Chole Bhature': 100
    }
}

# Order History List
# Stores past orders for the session: [{id, total, date, items}]
order_history = []  # Kept the bucket empty for now
order_counter = 1   # count starts as orders

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_main_menu():
    """Display the main navigation menu."""
    print("\n" + "="*50)
    print("🍔  CANTEEN MANAGEMENT SYSTEM")
    print("="*50)
    print("1. 📜 View Menu")
    print("2. 🛒 Place Order")
    print("3. 🕒 Order History")
    print("4. 🚪 Exit")
    print("="*50)

def display_food_menu():
    """
    Display the food menu in a categorized format.
    
    Concepts:
    - Nested loops (Category -> Items)
    - String formatting for alignment
    """
    print("\n" + "-"*40)
    print("🍱  TODAY'S SPECIAL MENU  🍱")
    print("-"*40)
    
    # Iterate through categories in the MENU dictionary
    for category, items in MENU.items():
        print(f"\n🔹 {category.upper()}")
        print(f"{'Item Name':<20} {'Price (₹)'}")
        print("."*30)
        
        # Iterate through items in each category
        for item, price in items.items():
            print(f"{item:<20} ₹{price}")
    print("-"*40)

# ============================================================================
# ORDER PROCESSING FUNCTIONS
# ============================================================================

def take_order():
    """
    Interactive function to take customer orders.
    
    Process:
    1. Show menu
    2. Loop to add items
    3. Validate item existence
    4. Calculate item total
    5. Generate final bill
    """
    global order_counter
    
    print("\n--- 🛒 PLACE NEW ORDER ---")
    display_food_menu()
    
    current_order = []  # List to store items: [{name, price, qty, total}]
    grand_total = 0
    
    while True:
        item_name = input("\nEnter Item Name (or 'done' to finish): ").strip().title()
        
        if item_name.lower() == 'done':
            break
            
        # Search for item in menu
        # We need to find which category the item belongs to
        found_item = False
        item_price = 0
        
        for category, items in MENU.items():
            if item_name in items:
                item_price = items[item_name]
                found_item = True
                break
        
        if not found_item:
            print("❌ Item not found! Please check spelling.")
            continue
            
        # Get Quantity with try & except to keep errors dont halt the app
        try:
            qty = int(input(f"Enter Quantity for {item_name}: "))
            if qty <= 0:
                print("❌ Quantity must be positive!")
                continue
        except ValueError:
            print("❌ Invalid number! Please enter a valid quantity.")
            continue
            
        # Add to order
        item_total = item_price * qty
        current_order.append({
            'name': item_name,
            'price': item_price,
            'qty': qty,
            'total': item_total
        })
        grand_total += item_total
        print(f"✅ Added: {item_name} x {qty} = ₹{item_total}")
    
    # If order is not empty, generate bill
    if current_order:
        generate_bill(current_order, grand_total)
    else:
        print("❌ Order cancelled (No items added).")

def generate_bill(order_items, total_amount):
    """
    Print a professional receipt and save to history.
    """
    global order_counter        # using global keyword to make use of order_counter everywhere needed
    
    print("\n" + "="*50)
    print(f"{'🧾 BILL RECEIPT':^50}")
    print("="*50)
    print(f"Order ID: #{order_counter}")
    print(f"Date: {datetime.now().strftime('%d-%b-%Y %I:%M %p')}")  # datetime used
    print("-" * 50)
    print(f"{'Item':<20} {'Qty':<10} {'Price':<10} {'Total':<10}")
    print("-" * 50)
    
    for item in order_items:
        print(f"{item['name']:<20} {item['qty']:<10} {item['price']:<10} {item['total']:<10}")
        
    print("-" * 50)
    print(f"{'GRAND TOTAL':<40} ₹{total_amount}")
    print("="*50)
    print("🙏 Thank you! Visit Again!")
    print("="*50)
    
    # Save to history
    order_history.append({
        'id': order_counter,
        'date': datetime.now().strftime('%d-%b-%Y'),
        'items': len(order_items),
        'total': total_amount
    })
    order_counter += 1

def view_order_history():
    """Display summary of all past orders."""
    print("\n--- 🕒 ORDER HISTORY ---")
    
    if not order_history:
        print("📭 No orders placed yet.")
        return
        
    print(f"{'ID':<10} {'Date':<15} {'Items':<10} {'Amount':<10}")
    print("-" * 50)
    
    for order in order_history:
        print(f"#{order['id']:<9} {order['date']:<15} {order['items']:<10} ₹{order['total']:<10}")
    print("-" * 50)

# ============================================================================
# MAIN PROGRAM LOOP - While so asks each things required
# ============================================================================

def main():
    while True:
        display_main_menu()
        choice = input("\nEnter Choice (1-4): ").strip()
        
        if choice == '1':
            display_food_menu()
            input("\nPress Enter to continue...")
        elif choice == '2':
            take_order()
            input("\nPress Enter to continue...")
        elif choice == '3':
            view_order_history()
            input("\nPress Enter to continue...")
        elif choice == '4':
            print("\n👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid Choice!")

if __name__ == "__main__":
    main()

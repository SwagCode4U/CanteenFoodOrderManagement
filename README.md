# 🍔 Canteen / Food Order Management System By @mit

A beginner-friendly yet practical Python project that simulates a real-world canteen ordering experience. 

## 🎯 What It Does

This system allows students/users to:
1. **View Menu** - Browse food items across different categories (Snacks, Beverages, Meals).
2. **Place Order** - Select items, specify quantities, and get live cost updates.
3. **Generate Bill** - Get a formatted receipt with date, time, and grand total.
4. **Order History** - Track past orders in the current session.

## 🚀 How to Run

```bash
# Navigate to the project directory
cd /home/john/Documents/learn/Learn_Dec_PYTHON/Basic-Projects/Canteen-FoodOrderManagement

# Run the system
python3 canteen_system.py
python canteen_system.py
Or
Just run from VSCODE / PYCHARM 
```

## ✨ Why This is Good for Learning

- **Relatable Logic**: Everyone understands how ordering food works, making the code logic intuitive.
- **Data Structures**:
  - `Dictionaries` for storing the menu (Categories -> Items -> Prices).
  - `Lists` for tracking the current order and order history.
- **Loops & Conditions**: Used extensively for the menu selection and input validation.
- **Clean output**: Demonstrates string formatting `f"{item:<20}"` for aligning text in bills.

## 💡 Sample Usage

```
🍔  CANTEEN MANAGEMENT SYSTEM
==================================================
1. 📜 View Menu
2. 🛒 Place Order
3. 🕒 Order History
4. 🚪 Exit
==================================================

Enter Choice (1-4): 2

--- 🛒 PLACE NEW ORDER ---
Enter Item Name (or 'done' to finish): Samosa
Enter Quantity for Samosa: 2
✅ Added: Samosa x 2 = ₹30
```

## 🧾 Sample Bill Output

```
==================================================
                 🧾 BILL RECEIPT                 
==================================================
Order ID: #1
Date: 28-Jan-2026 11:30 AM
--------------------------------------------------
Item                 Qty        Price      Total     
--------------------------------------------------
Samosa               2          15         30        
Tea                  1          10         10        
--------------------------------------------------
GRAND TOTAL                              ₹40
==================================================
🙏 Thank you! Visit Again!
==================================================
```

## 🔧 Technical Details
- **Language**: Python 3.x
- **Modules**: `datetime` (for timestamping bills)
- **Input Handling**: Handles invalid numbers and non-existent items gracefully.

---
**Perfect for**: Beginners looking to build their first interactive "System" project.

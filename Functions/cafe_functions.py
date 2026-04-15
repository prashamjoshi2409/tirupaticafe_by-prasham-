# Backend Functions for Tirupati Cafe - Demo
# Test and demo purpose

from datetime import datetime
import json
import random
import string

# Sample Menu Data
MENU = {
    'beverages': [
        {'id': 1, 'name': 'Coffee', 'price': 80, 'category': 'Hot Drinks'},
        {'id': 2, 'name': 'Tea', 'price': 60, 'category': 'Hot Drinks'},
        {'id': 3, 'name': 'Iced Coffee', 'price': 100, 'category': 'Cold Drinks'},
    ],
    'snacks': [
        {'id': 4, 'name': 'Samosa', 'price': 30, 'category': 'Snacks'},
        {'id': 5, 'name': 'Vada Pav', 'price': 40, 'category': 'Snacks'},
    ],
    'meals': [
        {'id': 6, 'name': 'Idli Dosa', 'price': 150, 'category': 'Main Course'},
        {'id': 7, 'name': 'Biryani', 'price': 250, 'category': 'Main Course'},
    ]
}

# Validate email
def validate_email(email):
    """Validate email format"""
    return '@' in email and '.' in email.split('@')[1]

# Validate phone
def validate_phone(phone):
    """Validate Indian phone number"""
    return len(phone) == 10 and phone.isdigit()

# Generate order ID
def generate_order_id():
    """Generate unique order ID"""
    timestamp = str(int(datetime.now().timestamp()))
    random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"ORD-{timestamp[-6:]}-{random_code}"

# Get menu items
def get_menu_by_category(category):
    """Get menu items by category"""
    items = []
    for items_list in MENU.values():
        for item in items_list:
            if item['category'].lower() == category.lower():
                items.append(item)
    return items

# Calculate bill
def calculate_bill(items, tax_percent=5):
    """Calculate total bill with tax"""
    subtotal = sum(item.get('price', 0) * item.get('quantity', 1) for item in items)
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    
    return {
        'subtotal': round(subtotal, 2),
        'tax': round(tax, 2),
        'total': round(total, 2),
        'discount': 0,
        'final_amount': round(total, 2)
    }

# Create order
def create_order(customer_name, phone, items):
    """Create a new order"""
    if not validate_phone(phone):
        return {'error': 'Invalid phone number'}
    
    order_id = generate_order_id()
    bill = calculate_bill(items)
    
    order = {
        'order_id': order_id,
        'customer_name': customer_name,
        'phone': phone,
        'items': items,
        'bill': bill,
        'status': 'Received',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return order

# Check if restaurant is open
def is_restaurant_open():
    """Check if restaurant is open (9 AM to 10 PM)"""
    hour = datetime.now().hour
    return 9 <= hour < 22

# Get all menu items
def get_all_menu():
    """Get all menu items"""
    all_items = []
    for category, items in MENU.items():
        all_items.extend(items)
    return all_items

# Log order (for testing)
def log_order(order):
    """Print order details"""
    print("\n" + "="*40)
    print("ORDER DETAILS")
    print("="*40)
    print(f"Order ID: {order['order_id']}")
    print(f"Customer: {order['customer_name']}")
    print(f"Phone: {order['phone']}")
    print(f"Items: {order['items']}")
    print(f"Bill: {json.dumps(order['bill'], indent=2)}")
    print(f"Status: {order['status']}")
    print(f"Time: {order['timestamp']}")
    print("="*40 + "\n")

# Test function
if __name__ == "__main__":
    print("Testing Tirupati Cafe Functions...")
    print(f"Restaurant Open: {is_restaurant_open()}")
    print(f"All Menu Items: {len(get_all_menu())} items")
    
    # Test order
    test_order = create_order(
        customer_name="John Doe",
        phone="9876543210",
        items=[
            {'id': 1, 'name': 'Coffee', 'price': 80, 'quantity': 2},
            {'id': 4, 'name': 'Samosa', 'price': 30, 'quantity': 3}
        ]
    )
    log_order(test_order)

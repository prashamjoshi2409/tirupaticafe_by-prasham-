# Functions Directory - Tirupati Cafe

Demo and test functions for the Tirupati Cafe website. These are utility functions for both frontend and backend operations.

## Files

### 1. `utils.js` - Frontend/JavaScript Functions
Utility functions for client-side operations:

- **validateEmail(email)** - Validate email format
- **validatePhone(phone)** - Validate 10-digit phone number
- **calculateOrderTotal(items, taxPercent)** - Calculate bill with tax
- **formatCurrency(amount)** - Format amount in INR currency
- **generateOrderId()** - Generate unique order ID
- **getCurrentTime()** - Get current time in Indian format
- **isRestaurantOpen()** - Check if restaurant is open (9 AM - 10 PM)
- **logOrder(orderId, items, customerName)** - Log order details

### 2. `cafe_functions.py` - Backend/Python Functions
Server-side functions for cafe operations:

- **validate_email(email)** - Validate email
- **validate_phone(phone)** - Validate Indian phone number
- **generate_order_id()** - Create unique order ID
- **get_menu_by_category(category)** - Get menu items by category
- **calculate_bill(items, tax_percent)** - Calculate total with tax
- **create_order(customer_name, phone, items)** - Create new order
- **is_restaurant_open()** - Check restaurant status
- **get_all_menu()** - Get all menu items
- **log_order(order)** - Print order details

## Usage

### JavaScript
```javascript
const utils = require('./utils.js');
utils.validateEmail('customer@email.com');
utils.calculateOrderTotal(items);
```

### Python
```python
from cafe_functions import create_order, get_all_menu

order = create_order("John", "9876543210", items)
menu = get_all_menu()
```

## Test Data
- Sample menu with beverages, snacks, and meals
- Menu items include: Coffee, Tea, Samosa, Vada Pav, Idli Dosa, Biryani
- Tax percentage: 5% (default)
- Operating hours: 9 AM to 10 PM

## Next Steps
- Add database integration
- Add payment gateway
- Create API endpoints
- Add customer authentication
- Add order tracking system

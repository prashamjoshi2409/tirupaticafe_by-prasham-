// Utility Functions for Tirupati Cafe Website - Demo

// Validate Email
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Validate Phone Number
function validatePhone(phone) {
  const phoneRegex = /^[0-9]{10}$/;
  return phoneRegex.test(phone);
}

// Calculate Order Total
function calculateOrderTotal(items, taxPercent = 5) {
  let subtotal = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  let tax = subtotal * (taxPercent / 100);
  return {
    subtotal: subtotal.toFixed(2),
    tax: tax.toFixed(2),
    total: (subtotal + tax).toFixed(2)
  };
}

// Format Currency
function formatCurrency(amount) {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR'
  }).format(amount);
}

// Generate Order ID
function generateOrderId() {
  return 'ORD-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9).toUpperCase();
}

// Get Current Time
function getCurrentTime() {
  return new Date().toLocaleTimeString('en-IN');
}

// Check if Restaurant is Open (Demo: 9 AM to 10 PM)
function isRestaurantOpen() {
  const hour = new Date().getHours();
  return hour >= 9 && hour < 22;
}

// Log order details
function logOrder(orderId, items, customerName) {
  console.log('=== Order Details ===');
  console.log('Order ID:', orderId);
  console.log('Customer:', customerName);
  console.log('Items:', items);
  console.log('Time:', getCurrentTime());
  console.log('===================');
}

// Export functions
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    validateEmail,
    validatePhone,
    calculateOrderTotal,
    formatCurrency,
    generateOrderId,
    getCurrentTime,
    isRestaurantOpen,
    logOrder
  };
}

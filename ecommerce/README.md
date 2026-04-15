# 🛍️ ShopDjango - Full-Featured Ecommerce Project

A complete Django ecommerce web application with product listings, shopping cart, checkout, user authentication, and order management.

## ✨ Features

- **Product Catalog** — Categories, search, filters, sorting, product images, discount prices
- **Shopping Cart** — Session-based cart (works for guests too), quantity updates
- **Checkout & Orders** — Address form, COD/Online payment, order tracking with progress bar
- **User Accounts** — Register, login, profile management
- **Product Reviews** — Star ratings and comments (one per user per product)
- **Admin Panel** — Manage products, categories, orders, users via Django Admin
- **Responsive UI** — Bootstrap 5 + Font Awesome, mobile-friendly

## 🗂️ Project Structure

```
ecommerce/
├── ecommerce/          # Project config (settings, urls, wsgi)
├── store/              # Products, categories, reviews
├── cart/               # Shopping cart (session-based)
├── orders/             # Checkout and order management
├── accounts/           # User registration, login, profile
├── templates/          # All HTML templates
│   ├── base.html
│   ├── store/
│   ├── cart/
│   ├── orders/
│   └── accounts/
├── media/              # Uploaded product images
├── manage.py
├── requirements.txt
└── setup.sh
```

## 🚀 Quick Start

### 1. Extract the ZIP and navigate to the project
```bash
cd ecommerce
```

### 2. Run the setup script (recommended)
```bash
chmod +x setup.sh
./setup.sh
```

### OR set up manually:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### 3. Open in browser
- **Site:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

## 🖥️ Admin Panel Usage

1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Add **Categories** first (e.g., Electronics, Clothing, Books)
4. Add **Products** with images, prices, and stock
5. Mark products as **Featured** to show them on the homepage

## 📦 Dependencies

- **Django 4.2+** — Web framework
- **Pillow** — Image handling for product photos

## 🔧 Configuration

Edit `ecommerce/settings.py` to configure:
- `SECRET_KEY` — Change before deploying to production
- `DEBUG` — Set to `False` in production
- `ALLOWED_HOSTS` — Add your domain in production
- `DATABASES` — Switch to PostgreSQL/MySQL for production

## 📱 Pages

| URL | Page |
|-----|------|
| `/` | Homepage with featured & latest products |
| `/products/` | Product listing with filters |
| `/products/<slug>/` | Product detail with reviews |
| `/cart/` | Shopping cart |
| `/orders/checkout/` | Checkout page |
| `/orders/my-orders/` | User order history |
| `/accounts/register/` | Registration |
| `/accounts/login/` | Login |
| `/accounts/profile/` | User profile |
| `/admin/` | Admin dashboard |

## 🤝 Contributing

Feel free to extend this project with:
- Payment gateway (Razorpay, Stripe)
- Wishlist functionality
- Product image gallery
- Coupon codes
- Email notifications

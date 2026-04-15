#!/bin/bash
echo "============================================"
echo "  ShopDjango - Ecommerce Setup Script"
echo "============================================"

# Create virtual environment
echo "[1/5] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "[2/5] Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "[3/5] Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "[4/5] Creating superuser..."
echo "Please create an admin account:"
python manage.py createsuperuser

# Load sample data (optional)
echo "[5/5] Setup complete!"
echo ""
echo "============================================"
echo "  To start the server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "  Admin panel: http://127.0.0.1:8000/admin/"
echo "  Site:        http://127.0.0.1:8000/"
echo "============================================"

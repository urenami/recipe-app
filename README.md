# 🍽️ Recipe App

Welcome to **Recipe App**, a Django-based portfolio project that demonstrates **full-stack development** with a polished UI/UX.  
This application allows users to explore recipes, filter them by difficulty, and view analytics with beautiful chart visualizations.  

---

## ✨ Features

- 🔐 **Authentication system** with login/logout (demo credentials provided)  
- 🍳 **Recipe detail view** with cooking time, difficulty, and ingredients  
- 🎨 **Glassmorphic UI** styled with custom CSS and Google Fonts  
- 📌 **Difficulty highlighting** (Easy = Green, Intermediate = Orange, Hard = Red)  
- 📊 **Dynamic charts** (bar, pie, line) using Matplotlib for recipe analytics  
- 📱 **Responsive design** for mobile and desktop  
- 🚫 No registration or password reset (demo-only for portfolio purposes)  

---

## 🔑 Demo Login

Use this account to explore the app:

- **Username:** `demo`  
- **Password:** `demo123`  

⚠️ *Note: This demo account cannot access the Django Admin — only the main app.*  

---

## 🚀 Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/urenami/recipe-app.git
   cd recipe-app

2. **Set up environment, install dependencies, and run the project**

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # On Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# (Optional) create superuser for admin access
python manage.py createsuperuser

# Run the server
python manage.py runserver

3. **Access the app**

Visit: http://127.0.0.1:8000/
Log in with demo credentials above
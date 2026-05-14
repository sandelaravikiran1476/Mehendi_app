# 🌹 Mehendi Designs - Web Application

A beautiful, full-featured web application for discovering, sharing, and organizing Mehendi designs across different styles and cultures.

## 📋 Features

### 🔐 Authentication
- **User Registration** - Create new account with validation
- **Secure Login** - Password hashing with Werkzeug security
- **User Profiles** - Personalized user accounts with account creation date
- **Session Management** - Secure session handling with Flask-Login

### 🎨 Mehendi Design Categories
1. **Indian Mehndi** - Traditional North Indian designs with intricate patterns
2. **Arabic Mehndi** - Bold geometric patterns with floral elements
3. **Indo-Arabic Mehndi** - Perfect fusion of Indian and Arabic styles
4. **Bridal Mehndi** - Elaborate designs for special occasions
5. **Western/Contemporary Mehndi** - Modern minimalist and artistic styles

### ⭐ Core Features
- **Browse Designs** - Explore 15+ pre-loaded Mehendi designs
- **Filter & Search** - Filter by category and complexity level
- **Design Details** - View detailed design information, complexity, and duration
- **Favorites** - Save your favorite designs to personal collection
- **Reviews & Ratings** - Rate and review designs (1-5 stars)
- **User Dashboard** - View saved favorites and written reviews
- **Like Counter** - See how many people like each design

### 🎯 User Experience
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Beautiful UI** - Mehendi-inspired color scheme and elegant styling
- **Fast Navigation** - Intuitive menu and category browsing
- **Flash Messages** - Real-time feedback for all user actions

## 🛠️ Tech Stack

- **Backend**: Python 3.x with Flask 2.3.2
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login with Werkzeug security
- **Frontend**: HTML5, CSS3 (custom styling)
- **Forms**: Flask-WTF for form handling
- **Server**: WSGI-compatible Flask development server

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
cd mehendi-app
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python run.py
```

### Step 3: Access the App
Open your browser and navigate to:
```
http://localhost:5000
```

## 🔓 Demo Credentials

To quickly test the application:
- **Username**: `demo`
- **Password**: `demo123`

## 📂 Project Structure

```
mehendi-app/
├── app/
│   ├── __init__.py          # Flask app factory and configuration
│   ├── models.py            # Database models (User, Design, Review)
│   ├── routes.py            # Application routes and endpoints
│   └── templates/           # HTML templates
├── templates/               # Jinja2 HTML templates
│   ├── base.html           # Base template with navbar and footer
│   ├── login.html          # Login page
│   ├── signup.html         # Registration page
│   ├── index.html          # Home page with hero and categories
│   ├── designs.html        # Design gallery with filters
│   ├── design_detail.html  # Individual design page with reviews
│   └── profile.html        # User profile and favorites
├── static/
│   └── css/
│       └── style.css       # Custom stylesheet (18KB+)
├── run.py                  # Application entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🗄️ Database Models

### User Model
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `password_hash` - Hashed password
- `full_name` - User's full name
- `created_at` - Account creation timestamp
- `favorites` - Relationship to favorite designs

### Design Model
- `id` - Primary key
- `title` - Design name
- `description` - Design description
- `category` - Mehendi type
- `image_url` - Design image URL
- `complexity` - Easy/Medium/Hard
- `duration` - Time to apply
- `created_at` - Upload timestamp
- `likes` - Like counter

### Review Model
- `id` - Primary key
- `design_id` - Foreign key to Design
- `user_id` - Foreign key to User
- `rating` - 1-5 star rating
- `review_text` - Review content
- `created_at` - Review timestamp

## 🎯 Usage Guide

### 1. Create an Account
- Click "Sign Up" in the navigation bar
- Fill in your full name, username, email, and password
- Click "Create Account"

### 2. Browse Designs
- Click "Gallery" to view all designs
- Use category filters to narrow down options
- Filter by complexity level (Easy, Medium, Hard)

### 3. Explore Categories
From the home page, click on any category to explore:
- Indian Mehndi
- Arabic Mehndi
- Indo-Arabic Mehndi
- Bridal Mehndi
- Western/Contemporary

### 4. View Design Details
- Click on any design card to see full details
- View complexity, duration, and description
- See average rating and existing reviews

### 5. Save Favorites
- Click "Add to Favorites" button on design detail page
- View all favorites in your profile

### 6. Write Reviews
- On the design detail page, fill out the review form
- Rate from 1-5 stars
- Write your review text
- Click "Submit Review"

### 7. View Your Profile
- Click "My Profile" in the navigation bar
- See your favorite designs
- View all reviews you've written

## 🎨 Color Scheme

The app uses a sophisticated Mehendi-inspired color palette:

| Color | Hex | Usage |
|-------|-----|-------|
| Gold | #d4af37 | Primary buttons, accents |
| Purple | #8b4789 | Secondary buttons, gradients |
| Dark Brown | #2c1810 | Text, headers, backgrounds |
| Light Cream | #f5f1ed | Background color |
| Pink | #e91e63 | Accent elements |

## 🚀 Deployment Guide

### Using Gunicorn (Recommended for Production)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Using Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run.py"]
```

Build and run:
```bash
docker build -t mehendi-app .
docker run -p 5000:5000 mehendi-app
```

## 📱 Responsive Design

The application is fully responsive:
- **Desktop** (1200px+) - Full feature set
- **Tablet** (768px-1199px) - Optimized layout
- **Mobile** (< 768px) - Touch-friendly interface

## 🔒 Security Features

- Password hashing using Werkzeug security
- CSRF protection on all forms
- Secure session management
- SQL injection prevention via SQLAlchemy ORM
- User authentication required for reviews and favorites

## 🐛 Troubleshooting

### Port 5000 Already in Use
```bash
# On Linux/Mac: Kill the process using port 5000
lsof -ti:5000 | xargs kill -9

# On Windows: Find and end the process
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Database Errors
```bash
# Delete the database and restart (will regenerate with sample data)
rm app/instance/mehendi.db
python run.py
```

### Missing Dependencies
```bash
pip install --upgrade -r requirements.txt
```

## 📊 Sample Data

The app includes 15 pre-loaded Mehendi designs across all categories:
- 3 Indian Mehndi designs
- 3 Arabic Mehndi designs
- 3 Indo-Arabic Mehndi designs
- 3 Bridal Mehndi designs
- 3 Western/Contemporary designs

Each design includes sample ratings, likes, and descriptions.

## 🎓 Learning Resources

### Flask Documentation
- https://flask.palletsprojects.com/

### SQLAlchemy ORM
- https://docs.sqlalchemy.org/

### Jinja2 Templating
- https://jinja.palletsprojects.com/

## 📝 Future Enhancements

- [ ] Image upload feature for custom designs
- [ ] User follow system
- [ ] Design sharing via social media
- [ ] Advanced search with tags
- [ ] Mehendi artist marketplace
- [ ] Mobile app (React Native)
- [ ] Real-time notifications
- [ ] Design recommendation engine
- [ ] Video tutorials for application
- [ ] Community forum

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👥 Credits

- Built with ❤️ for Mehendi design enthusiasts
- Design inspiration from traditional and contemporary Mehendi art
- Color palette inspired by authentic Mehendi aesthetics

## 📞 Support

For issues, questions, or suggestions:
- Create an issue on the GitHub repository
- Contact: support@mehendi-designs.app
- Visit our website: www.mehendi-designs.app

---

**Made with 🌹 by Mehendi Designs Team**

Happy Mehendi exploring! 🎨

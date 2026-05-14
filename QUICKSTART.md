# 🌹 Mehendi Designs - Quick Start Guide

## ⚡ Get Started in 3 Minutes

### 1. **Install & Run**
```bash
cd mehendi-app
pip install -r requirements.txt
python run.py
```

### 2. **Open in Browser**
Visit: `http://localhost:5000`

### 3. **Login with Demo Account**
- **Username**: `demo`
- **Password**: `demo123`

---

## 🎯 What You Can Do

### 👤 User Registration & Login
- Create a new account with email verification
- Secure login with password hashing
- Personal user profile with account stats

### 🎨 Browse Mehendi Designs
Explore designs across 5 unique categories:

| Category | Style | Examples |
|----------|-------|----------|
| 🇮🇳 Indian Mehndi | Traditional & intricate | North Indian, Rajasthani, Bengali |
| 🇸🇦 Arabic Mehndi | Bold & geometric | Gulf Arabic, Lebanese, Moroccan |
| 🎭 Indo-Arabic Mehndi | Fusion style | Combined traditions |
| 👰 Bridal Mehndi | Elaborate & premium | Full coverage, special occasion |
| ✨ Western/Contemporary | Modern & minimalist | Abstract, artistic, trendy |

### ⭐ Rate & Review Designs
- Give 1-5 star ratings
- Write detailed reviews
- See average ratings from community
- View other user reviews

### ❤️ Save Favorites
- Add designs to your personal favorites collection
- Remove favorites anytime
- View all favorites in your profile

### 📊 Personalized Dashboard
- View all your saved favorite designs
- See all reviews you've written
- Track your engagement stats
- Account information

---

## 🗂️ Key Pages

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | Hero section, categories, featured designs |
| Sign Up | `/signup` | Create new account |
| Login | `/login` | Sign in to account |
| Gallery | `/designs` | Browse all designs with filters |
| Design Detail | `/design/<id>` | Full design info, reviews, ratings |
| Profile | `/profile` | Your favorites and reviews |
| By Category | `/category/<name>` | Browse designs by category |

---

## 🔍 Filtering & Search

### Filter by Category
- Indian Mehndi
- Arabic Mehndi
- Indo-Arabic Mehndi
- Bridal Mehndi
- Western/Contemporary Mehndi

### Filter by Complexity
- **Easy** (20-30 min) - Perfect for beginners
- **Medium** (45-60 min) - Intermediate level
- **Hard** (90-180 min) - Advanced/bridal designs

---

## 📱 Features Showcase

### 1. **Homepage**
- Hero banner with tagline
- 5 category cards with emojis
- Featured designs section
- Call-to-action for new users

### 2. **Design Gallery**
- Grid layout of designs
- Hover effects showing "View Details"
- Category and complexity badges
- Like counter
- Responsive grid (auto-adjusting columns)

### 3. **Design Details Page**
- Large design image
- Design statistics (complexity, duration, likes)
- Detailed description
- Average rating display
- Add/remove from favorites
- Review submission form
- Community reviews section

### 4. **User Profile**
- Profile header with user info
- Stats cards (favorites count, reviews count)
- Favorite designs grid
- All written reviews
- Account creation date

---

## 🎨 Sample Data Included

The app comes with **15 pre-loaded designs**:

### Indian Mehndi (3 designs)
- Traditional North Indian Bridal
- Rajasthani Full Hand
- Bengali Simple Floral

### Arabic Mehndi (3 designs)
- Gulf Arabic Bold Design
- Lebanese Floral Arabesque
- Moroccan Geometric

### Indo-Arabic Mehndi (3 designs)
- Fusion Crown Design
- Elegant Indo-Arabic
- Minimal Fusion

### Bridal Mehndi (3 designs)
- Opulent Bridal Masterpiece
- Royal Bridal Gold
- Graceful Bride

### Western/Contemporary (3 designs)
- Modern Minimalist
- Artistic Abstract
- Mandala Modern

---

## 🛠️ Troubleshooting

### **Port 5000 in use?**
```bash
# Find and kill the process
lsof -ti:5000 | xargs kill -9
```

### **Database issues?**
```bash
# Delete and regenerate
rm mehendi.db
python run.py
```

### **Missing dependencies?**
```bash
pip install --upgrade -r requirements.txt
```

### **Template not found?**
```bash
# Verify templates directory exists
ls -la templates/
# Make sure you're in mehendi-app directory
pwd
```

---

## 🚀 Next Steps

1. **Create Your Account** - Sign up with new username and email
2. **Explore All Categories** - Click through each Mehendi style
3. **Save Favorites** - Build your collection of designs
4. **Write Reviews** - Share your thoughts on designs
5. **Check Profile** - See all your activities

---

## 📱 Responsive Design

The app works perfectly on:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px-1199px)
- ✅ Mobile (< 768px)

---

## 🔐 Security Notes

- Passwords are hashed with Werkzeug security
- All forms protected with CSRF tokens
- User sessions are secure and encrypted
- No passwords stored in plain text
- SQL injection prevention via SQLAlchemy ORM

---

## 💡 Tips & Tricks

### Pro Tips:
1. **Use demo account first** to explore without creating account
2. **Check complexity level** before choosing a design
3. **Read reviews** to see what others think
4. **Filter by level** if looking for specific difficulty
5. **Visit profile often** to track your favorites and reviews

### Design Recommendations:
- Beginners → Start with "Western/Contemporary" (Easy)
- Intermediate → Try "Indian Mehndi" (Medium)
- Advanced → Explore "Bridal Mehndi" (Hard)

---

## 📞 Support & Feedback

- Found a bug? Create an issue
- Want a feature? Submit a pull request
- Questions? Check README.md for detailed docs

---

**Happy Mehendi Exploring! 🌹🎨**

# 🏗️ Mehendi Designs - Architecture Guide

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Web Browser (Client)                     │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         HTML/CSS/JavaScript Frontend                │   │
│  │  - Responsive Design (Mobile, Tablet, Desktop)      │   │
│  │  - Interactive Forms & Filters                      │   │
│  │  - Dynamic User Interface                           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                          ↓ HTTP/HTTPS
┌─────────────────────────────────────────────────────────────┐
│                    Flask Web Server                          │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            Route Handlers (routes.py)               │   │
│  │  - Authentication (auth_bp)                         │   │
│  │  - Main Pages (main_bp)                             │   │
│  │  - Design Management (designs_bp)                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            Business Logic Layer                      │   │
│  │  - User Authentication                              │   │
│  │  - Design Filtering & Search                        │   │
│  │  - Review Management                                │   │
│  │  - Favorites Management                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │       Template Rendering (Jinja2)                   │   │
│  │  - base.html (Navigation & Layout)                  │   │
│  │  - Authentication Templates                         │   │
│  │  - Gallery & Detail Templates                       │   │
│  │  - Profile Template                                 │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                          ↓ SQL Queries
┌─────────────────────────────────────────────────────────────┐
│                    Database Layer                            │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         SQLAlchemy ORM (models.py)                  │   │
│  │  - User Model                                        │   │
│  │  - Design Model                                      │   │
│  │  - Review Model                                      │   │
│  │  - Relationships & Associations                      │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │          SQLite Database                             │   │
│  │  - mehendi.db (Local File)                          │   │
│  │  - Tables: users, designs, reviews, user_favorites  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## File Structure

```
mehendi-app/
│
├── app/                          # Main application package
│   ├── __init__.py              # Flask app factory & config
│   ├── models.py                # Database models (User, Design, Review)
│   └── routes.py                # All route handlers
│
├── templates/                    # Jinja2 HTML templates
│   ├── base.html                # Base layout with navbar/footer
│   ├── login.html               # Login page
│   ├── signup.html              # Registration page
│   ├── index.html               # Homepage
│   ├── designs.html             # Design gallery with filters
│   ├── design_detail.html       # Single design detail page
│   └── profile.html             # User profile & favorites
│
├── static/                      # Static assets
│   └── css/
│       └── style.css            # Main stylesheet (18KB+)
│
├── run.py                       # Application entry point
├── start.sh                     # Bash startup script
├── requirements.txt             # Python dependencies
├── README.md                    # Full documentation
├── QUICKSTART.md               # Quick start guide
├── ARCHITECTURE.md             # This file
├── mehendi.db                  # SQLite database (auto-generated)
└── venv/                       # Virtual environment (optional)
```

## Data Flow

### User Registration Flow
```
1. User → /signup page
2. User fills form (full_name, username, email, password)
3. POST → /signup route
4. Validation:
   - Check username uniqueness
   - Check email uniqueness
   - Validate password match
   - Check password length (min 6)
5. If valid:
   - Create User instance
   - Hash password with Werkzeug
   - Save to database
   - Redirect to login page
6. If invalid:
   - Flash error message
   - Redirect back to signup
```

### Authentication Flow
```
1. User → /login page
2. User enters username & password
3. POST → /login route
4. Query database for user
5. If user exists:
   - Check password hash
   - If correct:
     - login_user() (Flask-Login)
     - Create session
     - Redirect to home
   - If incorrect:
     - Flash "Invalid credentials"
     - Reload login page
6. If user doesn't exist:
   - Flash "Invalid credentials"
   - Reload login page
```

### Design Browsing Flow
```
1. User → /designs
2. Optional: Apply filters (category, complexity)
3. GET parameters processed
4. Query designs with filters:
   - category = request.args.get('category')
   - complexity = request.args.get('complexity')
5. Render designs.html with filtered results
6. Display grid of designs
7. User clicks design → /design/<id>
```

### Review & Rating Flow
```
1. User on /design/<id> page
2. Must be logged in (checked by @login_required)
3. User fills review form:
   - Select 1-5 star rating
   - Write review text
4. POST → /design/<id>/review
5. Check if user already reviewed this design
6. If yes: Update existing review
7. If no: Create new Review instance
8. Save to database
9. Redirect back to design detail
10. Display updated reviews and average rating
```

### Favorites Flow
```
1. User clicks "Add to Favorites" on design detail
2. AJAX POST → /design/<id>/favorite
3. Server checks if design in user's favorites
4. If yes: Remove from favorites
5. If no: Add to favorites
6. Return JSON response with new status
7. Update button text dynamically
8. User can view all favorites in /profile
```

## Database Schema

### users table
```sql
id (INTEGER, PK)
username (VARCHAR(80), UNIQUE)
email (VARCHAR(120), UNIQUE)
password_hash (VARCHAR(255))
full_name (VARCHAR(120))
created_at (DATETIME)
```

### designs table
```sql
id (INTEGER, PK)
title (VARCHAR(150))
description (TEXT)
category (VARCHAR(50))
image_url (VARCHAR(255))
complexity (VARCHAR(20))
duration (VARCHAR(50))
created_at (DATETIME)
likes (INTEGER)
```

### reviews table
```sql
id (INTEGER, PK)
design_id (INTEGER, FK → designs.id)
user_id (INTEGER, FK → users.id)
rating (INTEGER 1-5)
review_text (TEXT)
created_at (DATETIME)
```

### user_favorites table (Association)
```sql
user_id (INTEGER, FK → users.id)
design_id (INTEGER, FK → designs.id)
PRIMARY KEY (user_id, design_id)
```

## Request/Response Examples

### GET / (Homepage)
```
Request:
  GET /

Response:
  - Status: 200 OK
  - Template: index.html
  - Context:
    - designs: [Design objects]
    - categories: ['Indian Mehndi', 'Arabic Mehndi', ...]
```

### POST /signup (Registration)
```
Request:
  POST /signup
  Body:
    - full_name: "Jane Doe"
    - username: "janedoe"
    - email: "jane@example.com"
    - password: "secure123"
    - confirm_password: "secure123"

Response:
  - Status: 302 Redirect
  - Location: /login
  - Flash: "Account created successfully! Please log in."
```

### GET /designs (Gallery with Filters)
```
Request:
  GET /designs?category=Bridal Mehndi&complexity=Hard

Response:
  - Status: 200 OK
  - Template: designs.html
  - Context:
    - designs: [filtered Design objects]
    - selected_category: "Bridal Mehndi"
    - selected_complexity: "Hard"
```

### POST /design/<id>/review (Add Review)
```
Request:
  POST /design/1/review
  Body:
    - rating: 5
    - review_text: "Beautiful design!"

Response:
  - Status: 302 Redirect
  - Location: /design/1
  - Flash: "Review added successfully!"
```

## Security Considerations

### Password Security
- ✅ Hashed with Werkzeug PBKDF2
- ✅ Salt automatically included
- ✅ Never stored in plain text

### Session Security
- ✅ Flask-Login manages secure sessions
- ✅ User ID stored in secure cookie
- ✅ CSRF protection on all forms

### Database Security
- ✅ SQLAlchemy ORM prevents SQL injection
- ✅ Input validation on all forms
- ✅ Parameterized queries

### Authentication
- ✅ @login_required decorator for protected routes
- ✅ User can only access own data
- ✅ Reviews and favorites tied to user

## Performance Considerations

### Query Optimization
- Design queries filtered at database level
- Relationships pre-loaded via SQLAlchemy
- Pagination ready for scaling

### Frontend Optimization
- CSS minification (18KB)
- Minimal JavaScript dependencies
- Responsive images with proper sizes

### Scalability Path
1. Add database connection pooling
2. Implement caching with Redis
3. Move to PostgreSQL for production
4. Add background jobs (Celery)
5. Implement CDN for static assets

## Deployment Architecture

### Development
```
Local Machine
└── python run.py
    └── Flask built-in server (localhost:5000)
```

### Production
```
Production Server
├── Gunicorn (WSGI Application Server)
├── Nginx (Reverse Proxy)
├── PostgreSQL (Database)
├── Redis (Caching)
└── SSL/TLS (HTTPS)
```

## Key Technologies

| Component | Technology | Version |
|-----------|-----------|---------|
| Web Framework | Flask | 2.3.2 |
| ORM | SQLAlchemy | 3.0.5 |
| Authentication | Flask-Login | 0.6.2 |
| Database | SQLite/PostgreSQL | - |
| Password Hashing | Werkzeug | 2.3.6 |
| Forms | Flask-WTF | 1.1.1 |
| Templating | Jinja2 | Built-in |

## Extensibility Points

### 1. Add New Routes
```python
# In app/routes.py
@new_bp.route('/new-feature')
def new_feature():
    # Implementation
    pass

# In app/__init__.py
app.register_blueprint(new_bp)
```

### 2. Add New Models
```python
# In app/models.py
class NewModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add fields
```

### 3. Add New Templates
```
# In templates/
new_template.html
```

### 4. Customize Styling
```css
/* In static/css/style.css */
/* Add or modify CSS rules */
```

## Testing Strategy

### Unit Tests
- Model validation
- Password hashing
- Database operations

### Integration Tests
- Authentication flow
- Review submission
- Favorites management

### End-to-End Tests
- Full user journey
- Form submissions
- Page navigation

## Monitoring & Logging

### Development
- Flask debug mode
- Console logging
- Error stack traces

### Production Ready
- File-based logging
- Error tracking (Sentry)
- Performance monitoring (NewRelic)

---

**Next Steps**: See README.md for installation and QUICKSTART.md for usage guide.

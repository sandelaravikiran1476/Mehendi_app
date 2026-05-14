# 📦 Mehendi Designs - Installation & Setup Guide

## System Requirements

- **Python**: 3.7 or higher
- **pip**: Python package manager
- **RAM**: Minimum 512MB
- **Disk Space**: ~100MB
- **OS**: Windows, macOS, or Linux

## Installation Methods

---

## Method 1: Quick Start (Recommended)

### Step 1: Navigate to the Project
```bash
cd mehendi-app
```

### Step 2: Run the Startup Script

**On macOS/Linux:**
```bash
./start.sh
```

**On Windows:**
```bash
python run.py
```

### Step 3: Open in Browser
```
http://localhost:5000
```

**Done!** ✅

---

## Method 2: Manual Installation

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the Application
```bash
python run.py
```

### Step 3: Access the App
Open your browser to `http://localhost:5000`

---

## Method 3: Using Virtual Environment (Best Practice)

### Step 1: Create Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
python run.py
```

### Step 4: Access the App
```
http://localhost:5000
```

### Step 5: Deactivate Virtual Environment (when done)
```bash
deactivate
```

---

## Default Demo Account

Use these credentials to login immediately:

```
Username: demo
Password: demo123
```

---

## Troubleshooting Installation

### Issue: "Python not found" or "command not found: python3"

**Solution:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install with "Add Python to PATH" checked
3. Restart terminal/command prompt
4. Verify: `python --version`

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
# Make sure you're in the right directory
cd mehendi-app

# Install dependencies again
pip install -r requirements.txt
```

### Issue: "Address already in use" on port 5000

**Solution (macOS/Linux):**
```bash
# Find process using port 5000
lsof -ti:5000

# Kill the process (replace PID with actual ID)
kill -9 <PID>
```

**Solution (Windows):**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual ID)
taskkill /PID <PID> /F
```

### Issue: Database locked error

**Solution:**
```bash
# Navigate to instance folder
cd app/instance

# Delete the database file
rm mehendi.db

# Navigate back and restart
cd ../..
python run.py
```

### Issue: "No such file or directory: 'templates/'"

**Solution:**
Make sure you're running from the correct directory:
```bash
# Correct way
cd mehendi-app
python run.py

# Wrong way
cd .. && python mehendi-app/run.py
```

---

## File Structure After Installation

```
mehendi-app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── instance/
│       └── mehendi.db (created on first run)
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── index.html
│   ├── designs.html
│   ├── design_detail.html
│   └── profile.html
├── static/
│   └── css/
│       └── style.css
├── venv/ (optional, if using virtual environment)
├── run.py
├── start.sh
├── requirements.txt
├── README.md
├── QUICKSTART.md
├── ARCHITECTURE.md
└── INSTALLATION.md
```

---

## First Time Setup Checklist

- [ ] Python installed and accessible
- [ ] Navigated to `mehendi-app` directory
- [ ] Dependencies installed via `pip install -r requirements.txt`
- [ ] Database created (auto-generates on first run)
- [ ] App started with `python run.py`
- [ ] Opened `http://localhost:5000` in browser
- [ ] Logged in with demo account (demo / demo123)
- [ ] Explored design gallery
- [ ] Created new user account
- [ ] Added design to favorites
- [ ] Wrote a review

---

## Upgrading Dependencies

To ensure you have the latest compatible versions:

```bash
pip install --upgrade -r requirements.txt
```

---

## Docker Installation (Advanced)

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "run.py"]
```

### Step 2: Build Image
```bash
docker build -t mehendi-app .
```

### Step 3: Run Container
```bash
docker run -p 5000:5000 mehendi-app
```

### Step 4: Access App
```
http://localhost:5000
```

---

## Production Deployment

### Using Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Using Nginx (Reverse Proxy)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Environment Variables

Create `.env` file for production:
```
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/mehendi
```

---

## Database Migration (PostgreSQL)

For production use, switch from SQLite to PostgreSQL:

### Step 1: Install PostgreSQL Driver
```bash
pip install psycopg2-binary
```

### Step 2: Update Config
```python
# In app/__init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mehendi'
```

### Step 3: Migrate Data
```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
```

---

## Performance Optimization

### Enable Caching
```bash
pip install flask-caching
```

### Use Redis
```bash
pip install redis
```

### Database Indexing
```python
# Add to models for faster queries
class Design(db.Model):
    __table_args__ = (
        db.Index('idx_category', 'category'),
        db.Index('idx_complexity', 'complexity'),
    )
```

---

## Monitoring & Logging

### Enable Application Logging
```python
import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)
```

### Monitor Database
```bash
# Check database size
ls -lh app/instance/mehendi.db

# Backup database
cp app/instance/mehendi.db app/instance/mehendi.db.backup
```

---

## Security Hardening

### 1. Update Secret Key
```python
# In app/__init__.py
import secrets
app.config['SECRET_KEY'] = secrets.token_hex(32)
```

### 2. Enable HTTPS
```bash
pip install flask-talisman
```

### 3. Add Rate Limiting
```bash
pip install flask-limiter
```

### 4. Security Headers
```python
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response
```

---

## Maintenance

### Regular Backups
```bash
# Daily backup
cp -r mehendi-app mehendi-app.backup.$(date +%Y%m%d)
```

### Clear Old Sessions
```bash
# Remove old session files if using file-based sessions
find app/sessions -type f -mtime +7 -delete
```

### Monitor Logs
```bash
# Watch log file in real-time
tail -f app.log
```

---

## Support & Troubleshooting

### Check Installation
```bash
python -c "import flask; print(flask.__version__)"
```

### Verify Database
```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
>>>     from app.models import User, Design, Review
>>>     print(f"Users: {User.query.count()}")
>>>     print(f"Designs: {Design.query.count()}")
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| ModuleNotFoundError | Missing dependencies | `pip install -r requirements.txt` |
| Address already in use | Port 5000 taken | Kill process or use different port |
| TemplateNotFoundError | Wrong directory | Ensure in `mehendi-app` folder |
| DatabaseError | Corrupted database | Delete `mehendi.db` and restart |

---

## Next Steps After Installation

1. ✅ **Verify Installation**: Open `http://localhost:5000`
2. ✅ **Test Login**: Use demo credentials (demo / demo123)
3. ✅ **Create Account**: Sign up with new credentials
4. ✅ **Explore Designs**: Browse all 5 categories
5. ✅ **Save Favorites**: Add designs to collection
6. ✅ **Write Reviews**: Rate and review designs
7. ✅ **Check Profile**: View favorites and reviews

---

## Getting Help

- **Documentation**: See README.md
- **Quick Start**: See QUICKSTART.md
- **Architecture**: See ARCHITECTURE.md
- **GitHub Issues**: Report bugs or request features
- **Email**: support@mehendi-designs.app

---

**Installation Complete!** 🎉

You now have a fully functional Mehendi Designs application ready to explore. Enjoy! 🌹

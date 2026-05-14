from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Design, Review
from datetime import datetime

auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('main', __name__)
designs_bp = Blueprint('designs', __name__)

# ============ AUTHENTICATION ROUTES ============

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('auth.signup'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('auth.signup'))
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.signup'))
        
        if len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
            return redirect(url_for('auth.signup'))
        
        user = User(username=username, email=email, full_name=full_name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('main.index'))

# ============ MAIN ROUTES ============

@main_bp.route('/')
def index():
    designs = Design.query.limit(6).all()
    categories = ['Indian Mehndi', 'Arabic Mehndi', 'Indo-Arabic Mehndi', 'Bridal Mehndi', 'Western/Contemporary Mehndi']
    return render_template('index.html', designs=designs, categories=categories)

@main_bp.route('/profile')
@login_required
def profile():
    user_designs = current_user.favorites
    user_reviews = current_user.reviews
    return render_template('profile.html', designs=user_designs, reviews=user_reviews)

# ============ DESIGN ROUTES ============

@designs_bp.route('/designs')
def all_designs():
    category = request.args.get('category')
    complexity = request.args.get('complexity')
    
    query = Design.query
    
    if category:
        query = query.filter_by(category=category)
    if complexity:
        query = query.filter_by(complexity=complexity)
    
    designs = query.all()
    categories = ['Indian Mehndi', 'Arabic Mehndi', 'Indo-Arabic Mehndi', 'Bridal Mehndi', 'Western/Contemporary Mehndi']
    
    return render_template('designs.html', designs=designs, categories=categories, selected_category=category, selected_complexity=complexity)

@designs_bp.route('/design/<int:design_id>')
def design_detail(design_id):
    design = Design.query.get_or_404(design_id)
    reviews = Review.query.filter_by(design_id=design_id).all()
    user_review = None
    
    if current_user.is_authenticated:
        user_review = Review.query.filter_by(design_id=design_id, user_id=current_user.id).first()
    
    avg_rating = 0
    if reviews:
        avg_rating = sum(r.rating for r in reviews if r.rating) / len([r for r in reviews if r.rating])
    
    return render_template('design_detail.html', design=design, reviews=reviews, user_review=user_review, avg_rating=avg_rating)

@designs_bp.route('/design/<int:design_id>/favorite', methods=['POST'])
@login_required
def toggle_favorite(design_id):
    design = Design.query.get_or_404(design_id)
    
    if design in current_user.favorites:
        current_user.favorites.remove(design)
        is_favorite = False
    else:
        current_user.favorites.append(design)
        is_favorite = True
    
    db.session.commit()
    return jsonify({'success': True, 'is_favorite': is_favorite})

@designs_bp.route('/design/<int:design_id>/review', methods=['POST'])
@login_required
def add_review(design_id):
    design = Design.query.get_or_404(design_id)
    rating = request.form.get('rating', type=int)
    review_text = request.form.get('review_text')
    
    existing_review = Review.query.filter_by(design_id=design_id, user_id=current_user.id).first()
    
    if existing_review:
        existing_review.rating = rating
        existing_review.review_text = review_text
        existing_review.created_at = datetime.utcnow()
    else:
        review = Review(design_id=design_id, user_id=current_user.id, rating=rating, review_text=review_text)
        db.session.add(review)
    
    db.session.commit()
    flash('Review added successfully!', 'success')
    return redirect(url_for('designs.design_detail', design_id=design_id))

@designs_bp.route('/category/<category>')
def category_designs(category):
    designs = Design.query.filter_by(category=category).all()
    categories = ['Indian Mehndi', 'Arabic Mehndi', 'Indo-Arabic Mehndi', 'Bridal Mehndi', 'Western/Contemporary Mehndi']
    return render_template('designs.html', designs=designs, categories=categories, selected_category=category)

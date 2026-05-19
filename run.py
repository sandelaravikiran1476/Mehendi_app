#!/usr/bin/env python3
"""
Main application entry point for Mehendi Designs App
"""
from app import create_app, db
from app.models import User, Design, Review

if __name__ == '__main__':
    app = create_app()
    
    with app.app_context():
        # Create sample designs if the database is empty
        if Design.query.count() == 0:
            sample_designs = [
                # Indian Mehndi
                Design(
                    title="Traditional North Indian Bridal",
                    description="Intricate traditional North Indian design with detailed floral patterns and dots",
                    category="Indian Mehndi",
                    image_url="https://images.unsplash.com/photo-1585906868735-e8e4c9e9c9e9?w=300&h=400&fit=crop",
                    complexity="Hard",
                    duration="60-90 minutes",
                    likes=245
                ),
                Design(
                    title="Rajasthani Full Hand",
                    description="Beautiful Rajasthani style design covering the entire hand",
                    category="Indian Mehndi",
                    image_url="https://images.unsplash.com/photo-1590080876614-3e82221d5f3a?w=300&h=400&fit=crop",
                    complexity="Medium",
                    duration="45-60 minutes",
                    likes=189
                ),
                Design(
                    title="Bengali Simple Floral",
                    description="Elegant Bengali style with simple floral motifs",
                    category="Indian Mehndi",
                    image_url="https://images.unsplash.com/photo-1604654894610-df63bc536371?w=300&h=400&fit=crop",
                    complexity="Easy",
                    duration="30-45 minutes",
                    likes=156
                ),

                # Arabic Mehndi
                Design(
                    title="Gulf Arabic Bold Design",
                    description="Bold geometric patterns typical of Gulf Arabic mehndi",
                    category="Arabic Mehndi",
                    image_url="https://images.unsplash.com/photo-1548787959-4197a5fef901?w=300&h=400&fit=crop",
                    complexity="Medium",
                    duration="45-60 minutes",
                    likes=267
                ),
                Design(
                    title="Lebanese Floral Arabesque",
                    description="Elegant Lebanese style with flowing floral patterns",
                    category="Arabic Mehndi",
                    image_url="https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?w=300&h=400&fit=crop",
                    complexity="Hard",
                    duration="60-90 minutes",
                    likes=198
                ),
                Design(
                    title="Moroccan Geometric",
                    description="Moroccan inspired geometric patterns with traditional elements",
                    category="Arabic Mehndi",
                    image_url="https://images.unsplash.com/photo-1611003228941-98852ba62227?w=300&h=400&fit=crop",
                    complexity="Medium",
                    duration="50-65 minutes",
                    likes=212
                ),

                # Indo-Arabic Mehndi
                Design(
                    title="Fusion Crown Design",
                    description="Perfect blend of Indian intricacy and Arabic boldness",
                    category="Indo-Arabic Mehndi",
                    image_url="https://images.unsplash.com/photo-1599599810694-b5ac4dd10b20?w=300&h=400&fit=crop",
                    complexity="Hard",
                    duration="70-90 minutes",
                    likes=334
                ),
                Design(
                    title="Elegant Indo-Arabic",
                    description="Harmonious combination of both styles for sophisticated look",
                    category="Indo-Arabic Mehndi",
                    image_url="https://images.unsplash.com/photo-1615572412537-b1ef3c3231b7?w=300&h=400&fit=crop",
                    complexity="Medium",
                    duration="50-70 minutes",
                    likes=289
                ),
                Design(
                    title="Minimal Fusion",
                    description="Simplified Indo-Arabic fusion for everyday wear",
                    category="Indo-Arabic Mehndi",
                    image_url="https://images.unsplash.com/photo-1598361959091-48908009fe33?w=300&h=400&fit=crop",
                    complexity="Easy",
                    duration="35-50 minutes",
                    likes=201
                ),

                # Bridal Mehndi
                Design(
                    title="Opulent Bridal Masterpiece",
                    description="Elaborate full coverage bridal design with premium details",
                    category="Bridal Mehndi",
                    image_url="https://images.unsplash.com/photo-1510784722466-f2aa9c52fff6?w=300&h=400&fit=crop",
                    complexity="Hard",
                    duration="120-180 minutes",
                    likes=512
                ),
                Design(
                    title="Royal Bridal Gold",
                    description="Regal design featuring intricate patterns with gold accents",
                    category="Bridal Mehndi",
                    image_url="https://images.unsplash.com/photo-1540575467063-178f50002cee?w=300&h=400&fit=crop",
                    complexity="Hard",
                    duration="100-150 minutes",
                    likes=445
                ),
                Design(
                    title="Graceful Bride",
                    description="Elegant bridal design balancing intricacy and grace",
                    category="Bridal Mehndi",
                    image_url="https://images.unsplash.com/photo-1563181286-d3fee5d55364?w=300&h=400&fit=crop",
                    complexity="Hard",
                    duration="90-120 minutes",
                    likes=378
                ),

                # Western/Contemporary Mehndi
                Design(
                    title="Modern Minimalist",
                    description="Clean lines and simple geometric shapes for contemporary look",
                    category="Western/Contemporary Mehndi",
                    image_url="https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=300&h=400&fit=crop",
                    complexity="Easy",
                    duration="20-30 minutes",
                    likes=234
                ),
                Design(
                    title="Artistic Abstract",
                    description="Creative abstract design for modern artistic expression",
                    category="Western/Contemporary Mehndi",
                    image_url="https://images.unsplash.com/photo-1578296469835-cab62fe60d7e?w=300&h=400&fit=crop",
                    complexity="Medium",
                    duration="40-55 minutes",
                    likes=198
                ),
                Design(
                    title="Mandala Modern",
                    description="Contemporary mandala design with artistic twist",
                    category="Western/Contemporary Mehndi",
                    image_url="https://images.unsplash.com/photo-1474631245872-86e7f7ddf237?w=300&h=400&fit=crop",
                    complexity="Medium",
                    duration="45-60 minutes",
                    likes=267
                ),
            ]

            for design in sample_designs:
                db.session.add(design)

            # Create demo user
            demo_user = User(
                username='demo',
                email='demo@mehendi.com',
                full_name='Demo User'
            )
            demo_user.set_password('demo123')
            db.session.add(demo_user)

            db.session.commit()
            print("✅ Database initialized with sample designs and demo user!")
            print("📝 Demo Credentials:")
            print("   Username: demo")
            print("   Password: demo12345")

    # Run the application
    print("\n🌹 Mehendi Designs App is starting...")
    print("🌐 Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False, threaded=True)

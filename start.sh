#!/bin/bash

# Mehendi Designs App - Startup Script

echo "🌹 Mehendi Designs App Startup"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

echo "✅ Dependencies installed"
echo ""

# Display startup info
echo "🚀 Starting Mehendi Designs App..."
echo "=================================="
echo ""
echo "📱 Access the app at: http://localhost:5000"
echo ""
echo "🔓 Demo Credentials:"
echo "   Username: demo"
echo "   Password: demo123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the application
python3 run.py

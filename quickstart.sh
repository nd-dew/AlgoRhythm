#!/bin/bash

# Strudel AI Live Coding - Quick Start Script

echo "🎵 Strudel AI Live Coding - Quick Start"
echo "========================================"
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 16 or higher."
    exit 1
fi

# Check for Gemini API key
if [ -z "$GEMINI_API_KEY" ]; then
    echo "❌ GEMINI_API_KEY environment variable not set."
    echo ""
    echo "Please set your API key:"
    echo "  export GEMINI_API_KEY='your-api-key-here'"
    echo ""
    echo "Get your API key at: https://makersuite.google.com/app/apikey"
    echo ""
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo "✅ Node.js found: $(node --version)"
echo "✅ Gemini API key is set"
echo ""

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install Python dependencies"
    exit 1
fi
echo "✅ Python dependencies installed"

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install --silent
if [ $? -ne 0 ]; then
    echo "❌ Failed to install Node.js dependencies"
    exit 1
fi
echo "✅ Node.js dependencies installed"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the system:"
echo ""
echo "1️⃣  Start the Strudel server (in Terminal 1):"
echo "   npm start"
echo ""
echo "2️⃣  Open your browser to:"
echo "   http://localhost:3000"
echo ""
echo "3️⃣  Run the AI agent (in Terminal 2):"
echo "   python3 strudel_ai_agent.py"
echo ""
echo "Or see examples:"
echo "   python3 demo_examples.py list"
echo ""


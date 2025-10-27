#!/bin/bash

# System Test Script for Strudel AI Live Coding

echo "🧪 Strudel AI Live Coding - System Test"
echo "========================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
PASSED=0
FAILED=0

# Test function
test_check() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2"
        ((FAILED++))
    fi
}

echo "1️⃣  Checking Prerequisites..."
echo ""

# Check Python
python3 --version &> /dev/null
test_check $? "Python 3 installed"

# Check Node.js
node --version &> /dev/null
test_check $? "Node.js installed"

# Check npm
npm --version &> /dev/null
test_check $? "npm installed"

# Check pip
pip --version &> /dev/null
test_check $? "pip installed"

echo ""
echo "2️⃣  Checking Files..."
echo ""

# Check required files
test -f strudel_ai_agent.py
test_check $? "strudel_ai_agent.py exists"

test -f strudel_server.js
test_check $? "strudel_server.js exists"

test -f package.json
test_check $? "package.json exists"

test -f requirements.txt
test_check $? "requirements.txt exists"

test -f README.md
test_check $? "README.md exists"

test -d public
test_check $? "public/ directory exists"

test -f public/index.html
test_check $? "public/index.html exists"

echo ""
echo "3️⃣  Checking Environment..."
echo ""

# Check Gemini API key
if [ -z "$GEMINI_API_KEY" ]; then
    echo -e "${YELLOW}⚠${NC}  GEMINI_API_KEY not set (required for AI features)"
    ((FAILED++))
else
    echo -e "${GREEN}✓${NC} GEMINI_API_KEY is set"
    ((PASSED++))
fi

echo ""
echo "4️⃣  Checking Python Dependencies..."
echo ""

# Check if Python packages can be imported
python3 -c "import google.generativeai" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} google-generativeai package installed"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠${NC}  google-generativeai package not installed (run: pip install -r requirements.txt)"
    ((FAILED++))
fi

python3 -c "import requests" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} requests package installed"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠${NC}  requests package not installed (run: pip install -r requirements.txt)"
    ((FAILED++))
fi

echo ""
echo "5️⃣  Checking Node.js Dependencies..."
echo ""

# Check if node_modules exists
if [ -d "node_modules" ]; then
    echo -e "${GREEN}✓${NC} node_modules directory exists"
    ((PASSED++))
    
    # Check for express
    if [ -d "node_modules/express" ]; then
        echo -e "${GREEN}✓${NC} express package installed"
        ((PASSED++))
    else
        echo -e "${YELLOW}⚠${NC}  express package not installed"
        ((FAILED++))
    fi
    
    # Check for cors
    if [ -d "node_modules/cors" ]; then
        echo -e "${GREEN}✓${NC} cors package installed"
        ((PASSED++))
    else
        echo -e "${YELLOW}⚠${NC}  cors package not installed"
        ((FAILED++))
    fi
else
    echo -e "${YELLOW}⚠${NC}  node_modules not found (run: npm install)"
    ((FAILED++))
fi

echo ""
echo "6️⃣  Checking File Permissions..."
echo ""

# Check if scripts are executable
if [ -x strudel_ai_agent.py ]; then
    echo -e "${GREEN}✓${NC} strudel_ai_agent.py is executable"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠${NC}  strudel_ai_agent.py not executable (run: chmod +x strudel_ai_agent.py)"
    ((FAILED++))
fi

echo ""
echo "7️⃣  Syntax Checks..."
echo ""

# Check Python syntax
python3 -m py_compile strudel_ai_agent.py 2>/dev/null
test_check $? "strudel_ai_agent.py syntax valid"

# Check Node.js syntax
node -c strudel_server.js 2>/dev/null
test_check $? "strudel_server.js syntax valid"

echo ""
echo "========================================"
echo "Test Results:"
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo "========================================"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 All tests passed!${NC}"
    echo ""
    echo "You're ready to start:"
    echo "  1. npm start              # Start the server"
    echo "  2. Open http://localhost:3000"
    echo "  3. python3 strudel_ai_agent.py"
    exit 0
else
    echo -e "${YELLOW}⚠️  Some tests failed${NC}"
    echo ""
    echo "Please fix the issues above before running."
    echo ""
    echo "Quick fixes:"
    echo "  - pip install -r requirements.txt"
    echo "  - npm install"
    echo "  - chmod +x strudel_ai_agent.py"
    echo "  - export GEMINI_API_KEY='your-key'"
    exit 1
fi


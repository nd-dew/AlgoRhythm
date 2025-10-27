# 🔑 Gemini API Setup Guide

This project now uses **Google's Gemini AI** instead of OpenAI's GPT models.

## 🎯 Why Gemini?

- **Free tier available** with generous limits
- **Fast response times** with Gemini 1.5 Flash
- **High quality** code generation
- **Easy to get started** - no credit card required for testing

## 📝 Getting Your API Key

### Step 1: Visit Google AI Studio

Go to: **https://makersuite.google.com/app/apikey**

Or alternatively: **https://aistudio.google.com/app/apikey**

### Step 2: Sign In

- Sign in with your Google account
- Accept the terms of service if prompted

### Step 3: Create API Key

1. Click **"Create API Key"** button
2. Select an existing project or create a new one
3. Copy the generated API key (it will look like: `AIza...`)

### Step 4: Set Environment Variable

**For current session:**
```bash
export GEMINI_API_KEY='your-api-key-here'
```

**To make it permanent (Linux/Mac):**

For bash:
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

For zsh:
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

**Verify it's set:**
```bash
echo $GEMINI_API_KEY
```

## 🚀 Quick Start After Setup

Once your API key is set:

```bash
# Install dependencies
pip install -r requirements.txt
npm install

# Terminal 1: Start the server
npm start

# Terminal 2: Run the AI agent
python3 strudel_ai_agent.py
```

## 📊 Gemini Free Tier Limits

- **60 requests per minute**
- **1,500 requests per day**
- **1 million tokens per minute**

This is more than enough for live coding sessions!

## 🔧 Technical Details

The project uses:
- **Model**: `gemini-1.5-flash` (fast, efficient)
- **Temperature**: 0.7 (balanced creativity)
- **Max tokens**: 2048 (sufficient for Strudel code)

## 🆚 Differences from OpenAI

| Feature | Gemini | OpenAI |
|---------|--------|--------|
| Free tier | ✅ Yes | ❌ No |
| Speed | ⚡ Very fast | 🚀 Fast |
| Setup | Easy | Requires payment |
| API key | Free instantly | Requires card |

## 🐛 Troubleshooting

### "API key not found"
```bash
# Check if it's set
echo $GEMINI_API_KEY

# If empty, set it again
export GEMINI_API_KEY='your-key'
```

### "Invalid API key"
- Make sure you copied the entire key
- Check for extra spaces or quotes
- Regenerate the key if needed

### "Quota exceeded"
- You've hit the daily limit (1,500 requests)
- Wait 24 hours or create a new API key with a different project

### "Module not found: google.generativeai"
```bash
pip install google-generativeai
```

## 📚 Additional Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini Pricing](https://ai.google.dev/pricing)

## ✨ Ready to Create!

Once your API key is set, you're ready to generate AI-powered electronic music!

Try your first prompt:
```
create a minimal techno track with driving kicks and rolling hi-hats
```

Happy live coding! 🎵


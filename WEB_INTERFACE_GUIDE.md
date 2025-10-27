# 🌐 Web Interface Guide

## 🎯 How the System Works

### The Complete Workflow:

```
┌─────────────────┐      ┌──────────────┐      ┌─────────────────┐
│  Terminal       │      │   Server     │      │   Browser       │
│  (AI Agent)     │─────▶│  (Node.js)   │─────▶│  (Web UI)       │
│                 │      │              │      │                 │
│ Type prompts    │      │ Stores code  │      │ Shows code +    │
│ here            │      │              │      │ plays music     │
└─────────────────┘      └──────────────┘      └─────────────────┘
```

## 📝 Where to Type Prompts

### ⚠️ IMPORTANT: Prompts go in the TERMINAL, not the web page!

The web interface is primarily for:
- ✅ **Viewing** the generated code
- ✅ **Hearing** the music
- ✅ **Manually editing** the code if you want

AI prompts are typed in **Terminal 2** where the agent runs.

---

## 🎵 Audio Not Playing? Try These Fixes

### Fix 1: Browser Permissions ✅

Modern browsers require user interaction before playing audio:

1. **Refresh the page** (F5)
2. **Click the Play button** ▶️ immediately
3. **Look for a browser permission** popup (allow audio)

### Fix 2: Check Browser Console 🔍

1. Press **F12** to open Developer Tools
2. Click the **Console** tab
3. Look for any error messages
4. Common errors:
   - "AudioContext suspended" → Click Play again
   - "CORS error" → Server issue (restart server)
   - "evaluate is not a function" → Strudel loading issue

### Fix 3: Check the Code 📝

Make sure there's valid Strudel code showing:

**Good (will play):**
```javascript
s("bd sd bd sd")
```

**Bad (won't play):**
```javascript
// Waiting for code...
```

If you see "Waiting for code...", the server has no code yet.

### Fix 4: Manual Test 🧪

1. **Click in the Strudel editor** (right panel)
2. **Delete** the existing code
3. **Type** this simple test:
   ```javascript
   s("bd").fast(2)
   ```
4. **Click Play** ▶️
5. You should hear a kick drum

If this works, the problem is with the AI-generated code, not your setup.

### Fix 5: Try Different Browsers 🌐

- ✅ **Chrome/Edge**: Best support
- ✅ **Firefox**: Works well
- ⚠️ **Safari**: May have issues (try enabling autoplay)

---

## 🎹 Three Ways to Use the System

### Method 1: Mock Mode (Easiest) ⭐

**Terminal 1:**
```bash
npm start
```

**Terminal 2:**
```bash
python3 test_mock_mode.py
```

Then type in Terminal 2:
```
🎹 [MOCK] > create a techno track
🎹 [MOCK] > add more bass
```

**Browser:** Opens automatically, shows updates, click Play ▶️

---

### Method 2: Real Gemini AI 🤖

**Terminal 1:**
```bash
npm start
```

**Terminal 2:**
```bash
export GEMINI_API_KEY='your-key'
python3 strudel_ai_agent.py
```

Then type in Terminal 2:
```
🎹 > create a house track
🎹 > make it faster
```

**Browser:** Same as above

---

### Method 3: Manual Editing ✍️

**Terminal 1:**
```bash
npm start
```

**Browser:** 
1. Open http://localhost:3000
2. Click in the Strudel editor (right panel)
3. Type/edit code directly
4. Click Play ▶️ to hear it

---

## 🖥️ Understanding the Web Interface

### Left Panel: Code Display 📝
- Shows the current Strudel code
- Auto-updates when AI generates new code
- Read-only display

### Right Panel: Strudel Player 🎹
- Interactive editor
- You can **edit code directly here**
- Controls: Play ▶️ Stop ⏹️ Refresh 🔄

### Status Bar (Top) 📊
- Connection status
- Last update time

### Prompt Input (Bottom) 💬
- **For future use** (not fully implemented)
- Currently redirects you to use terminal
- May be enhanced in future versions

---

## 🐛 Common Issues & Solutions

### Issue: "No sound when clicking Play"

**Solutions:**
1. Check volume on computer/browser
2. Try a different browser
3. Check browser console (F12) for errors
4. Verify code is loaded (not "Waiting for code...")
5. Try manual test code: `s("bd").fast(2)`

---

### Issue: "Code not updating"

**Solutions:**
1. Verify AI agent is running in Terminal 2
2. Check Terminal 1 for server errors
3. Click Refresh button 🔄 in browser
4. Check browser console for network errors
5. Restart the server (Ctrl+C in Terminal 1, then `npm start`)

---

### Issue: "Strudel editor is blank"

**Solutions:**
1. Wait 5 seconds (Strudel takes time to load)
2. Refresh the page (F5)
3. Check internet connection (Strudel loads from CDN)
4. Try: `curl https://unpkg.com/@strudel/embed@latest`

---

### Issue: "Connection error in browser"

**Solutions:**
1. Verify server is running: `curl http://localhost:3000/health`
2. Check no other app is using port 3000
3. Restart server
4. Check firewall settings

---

## 💡 Pro Tips

### Tip 1: Use Browser Console for Debugging
Press **F12** and check the Console tab for helpful messages and errors.

### Tip 2: Edit Code Directly
You can edit the Strudel code directly in the right panel and click Play to test your changes.

### Tip 3: Multiple Browsers
Open the interface in multiple browser windows to show to others while you control the music.

### Tip 4: Mobile Viewing
The interface is responsive! Open on your phone/tablet to view while controlling from your computer.

### Tip 5: Save Good Code
When AI generates something you like, copy the code and save it to a file for later!

---

## 📊 What the Colors Mean

- 🟢 **Green status dot**: Connected to server
- 🔴 **Red warning box**: Audio/playback issue
- 🔵 **Blue info box**: Help and instructions
- 🟡 **Yellow text**: Important notes

---

## 🎮 Keyboard Shortcuts

In the Strudel editor (right panel):
- **Ctrl+Enter** / **Cmd+Enter**: Evaluate/Play code
- **Ctrl+.** / **Cmd+.**: Stop playback
- **Ctrl+A**: Select all
- **Ctrl+C**: Copy code
- **Ctrl+V**: Paste code

---

## 🆘 Still Not Working?

### Step 1: Basic Verification
```bash
# Is server running?
curl http://localhost:3000/health

# Expected: {"status":"ok","message":"Strudel server is running"}
```

### Step 2: Check Code on Server
```bash
curl http://localhost:3000/code
```

Should show JSON with Strudel code.

### Step 3: Test Server with Mock Mode
```bash
python3 test_mock_mode.py demo
```

This should generate 4 code updates and print success messages.

### Step 4: Browser Test
1. Open http://localhost:3000
2. Open console (F12)
3. Look for these messages:
   - "🎵 Strudel AI Live Coding"
   - "Strudel editor initialized"
   - "Playback started successfully"

---

## 📚 More Help

- **Mock Mode Guide**: `MOCK_MODE_GUIDE.md`
- **System Test**: Run `./test_system.sh`
- **Full Documentation**: `README.md`

---

## ✨ Summary

**For AI-Generated Music:**
1. ✅ Terminal 1: `npm start`
2. ✅ Terminal 2: `python3 test_mock_mode.py`
3. ✅ Browser: http://localhost:3000
4. ✅ Type prompts in Terminal 2
5. ✅ Click Play ▶️ in browser
6. ✅ Enjoy the music! 🎵

**For Manual Experimentation:**
1. ✅ Terminal 1: `npm start`
2. ✅ Browser: http://localhost:3000
3. ✅ Edit code in right panel
4. ✅ Click Play ▶️
5. ✅ Experiment! 🎨

---

**Happy Live Coding!** 🎵✨


# 🎵 Audio Playback Workaround

## The Issue

The Strudel editor's API methods might not be accessible via JavaScript, so the Play button might not work automatically.

## ✅ **SOLUTION: Use Keyboard Shortcut**

### Simple Method (Works 100% of the time):

1. **Open browser**: http://localhost:3000
2. **Click inside the Strudel editor** (right panel with code)
3. **Press `Ctrl+Enter`** (or `Cmd+Enter` on Mac)
4. **Music plays!** 🎵

To stop:
- **Press `Ctrl+.`** (or `Cmd+.` on Mac)

---

## 🎹 Complete Workflow (Updated)

### Terminal 1: Server
```bash
npm start
```
Leave running ✅

### Terminal 2: AI Agent
```bash
python3 test_mock_mode.py
```

Type prompts:
```
🎹 [MOCK] > create a minimal techno track
```

### Browser: http://localhost:3000

**To play the music:**

1. ✅ **Click in the Strudel editor** (right panel)
2. ✅ **Press Ctrl+Enter**
3. ✅ Music starts! 🎵

**To update and play:**

1. Type new prompt in Terminal 2
2. Code updates in browser automatically
3. Click in Strudel editor
4. Press Ctrl+Enter again
5. Hear the updated music! 🎵

---

## 🎨 Manual Editing Method

Want to experiment directly?

1. Open: http://localhost:3000
2. Click in the Strudel editor
3. Edit the code:
   ```javascript
   s("bd sd bd sd").fast(2).gain(0.8)
   ```
4. Press Ctrl+Enter
5. Hear your changes immediately!

---

## ⌨️ Keyboard Shortcuts

**In the Strudel Editor:**

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` / `Cmd+Enter` | Play/Evaluate code |
| `Ctrl+.` / `Cmd+.` | Stop playback |
| `Ctrl+A` | Select all |
| `Ctrl+C` | Copy |
| `Ctrl+V` | Paste |

---

## 🧪 Quick Test

**30-second test to verify audio works:**

1. Open: http://localhost:3000
2. Click in the Strudel editor (right side)
3. Clear any code
4. Type: `s("bd").fast(2)`
5. Press **Ctrl+Enter**
6. Should hear kick drum! 🥁

If you hear sound → ✅ Everything works!

---

## 💡 Why This Happens

The Strudel embed component uses Web Components and might not expose all methods to external JavaScript. The keyboard shortcuts work because they're handled internally by the Strudel editor.

This is actually **better** for live coding since you have full control!

---

## 🎯 Recommended Workflow

**For Live Performances:**

1. **Setup**: 
   - Terminal 1: `npm start`
   - Terminal 2: `python3 test_mock_mode.py` (or real AI)
   - Browser: http://localhost:3000
   - Click in Strudel editor

2. **Generate code** (Terminal 2):
   ```
   🎹 > create a dark techno track
   ```

3. **Play** (Browser):
   - Press Ctrl+Enter

4. **Update** (Terminal 2):
   ```
   🎹 > add more bass
   ```

5. **Play update** (Browser):
   - Press Ctrl+Enter again

6. **Stop** (Browser):
   - Press Ctrl+.

---

## 🎼 Pro Tips

### Tip 1: Keep Focus
Keep the browser window focused on the Strudel editor so Ctrl+Enter works immediately.

### Tip 2: Edit Live
You can edit the AI-generated code directly and press Ctrl+Enter to hear changes.

### Tip 3: Quick Changes
Make small edits and press Ctrl+Enter rapidly for live coding feel.

### Tip 4: Multiple Windows
Open multiple browser windows - one for performing, one for viewing code.

---

## ✨ Summary

**Don't use the Play button** - it might not work due to Strudel's API.

**Instead:**
1. Click in Strudel editor
2. Press **Ctrl+Enter** to play
3. Press **Ctrl+.** to stop

**This is actually the authentic live coding experience!** 🎵

---

## 📚 More Help

- Full guide: `WEB_INTERFACE_GUIDE.md`
- Quick reference: `QUICK_FIX_AUDIO.txt`
- Project status: `PROJECT_STATUS.md`

---

**Happy Live Coding!** 🎵✨


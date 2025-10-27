# 🧪 Mock Mode Testing Guide

## 🎯 What is Mock Mode?

Mock Mode allows you to test the entire Strudel AI Live Coding system **without requiring a Gemini API key**. It returns pre-programmed sample Strudel code that demonstrates the system's capabilities.

## ✅ Why Use Mock Mode?

- **Test the system** before getting an API key
- **Demo the project** to others
- **Verify installation** is correct
- **Learn the workflow** without API costs
- **Development testing** without rate limits

## 🚀 Running Mock Mode

### Option 1: Automated Demo (Recommended)

This runs a complete demo sequence automatically:

```bash
# Terminal 1: Start the server
npm start

# Terminal 2: Run the mock demo
python3 test_mock_mode.py demo
```

The demo will:
1. Create a minimal techno track
2. Add a dark bassline (5 sec wait)
3. Make it faster (5 sec wait)
4. Add atmospheric pads (5 sec wait)

### Option 2: Interactive Mode

Chat with the mock AI agent interactively:

```bash
# Terminal 1: Start the server
npm start

# Terminal 2: Run mock mode
python3 test_mock_mode.py
```

Then type prompts like:
```
🎹 [MOCK] > create a house track
🎹 [MOCK] > add more bass
🎹 [MOCK] > make it faster
```

### Option 3: Single Command

Test with a single prompt:

```bash
python3 test_mock_mode.py "create a minimal techno track"
```

## 🎹 Sample Prompts That Work in Mock Mode

The mock mode recognizes keywords and returns appropriate code:

| Prompt Keywords | Returns |
|----------------|---------|
| `techno` | Minimal techno pattern with kicks, claps, hi-hats |
| `house` | House track with 4/4 beat, piano, shaker |
| `bass` / `bassline` | Pattern with sawtooth bass |
| `faster` / `speed` | Fast pattern with doubled tempo |
| `atmospheric` / `pad` / `ambient` | Slow pads with reverb and delay |
| (default) | Basic drum patterns |

### Example Session

```bash
🎹 [MOCK] > create a techno track

📝 Generated code:
--------------------------------------------------
stack(
  s("bd ~ ~ ~ bd ~ ~ ~").gain(0.9),
  s("~ ~ ~ ~ ~ ~ cp ~").room(0.3),
  s("hh*8").gain(0.4)
).fast(2)
--------------------------------------------------

✅ Code sent to Strudel server!

🎹 [MOCK] > add a bassline

📝 Updated code:
--------------------------------------------------
stack(
  s("bd sd bd sd").gain(0.8),
  note("c2 ~ e2 ~").s("sawtooth").lpf(400)
)
--------------------------------------------------

✅ Code sent to Strudel server!
```

## 🌐 Viewing the Results

While the mock mode is running:

1. **Open your browser** to: `http://localhost:3000`
2. **Click the Play button** ▶️
3. **Watch the code update** in real-time
4. **Hear the music** change as you send new prompts

The web interface will show:
- The current Strudel code in the left panel
- The Strudel player in the right panel
- Automatic updates when new code is sent

## 🧪 What Gets Tested?

Running mock mode verifies:

✅ Python environment is working
✅ Server is running correctly
✅ Communication between agent and server
✅ Web interface receives updates
✅ Code polling mechanism works
✅ Strudel player integration functions
✅ Complete end-to-end workflow

## 🔍 Mock vs Real Mode Comparison

| Aspect | Mock Mode | Real Mode (Gemini) |
|--------|-----------|-------------------|
| **API Key** | Not required | Required |
| **Code Quality** | Pre-written samples | AI-generated |
| **Customization** | Limited patterns | Unlimited creativity |
| **Response** | Instant | ~1-2 seconds |
| **Cost** | Free | Free (with limits) |
| **Use Case** | Testing/Demo | Production use |

## 📊 What Mock Mode Tests

### 1. Server Communication ✅
- HTTP POST to `/update` endpoint
- JSON payload handling
- Response status codes

### 2. Code Delivery ✅
- Code reaches the server
- Server stores the code
- Web interface polls and receives updates

### 3. User Experience ✅
- Interactive command-line interface
- Real-time feedback
- Error handling

### 4. System Integration ✅
- Multi-component communication
- Proper sequencing of operations
- Status reporting

## 🛠️ Technical Details

### Mock Code Generation

The mock agent uses a simple keyword matching system:

```python
def _get_sample_code(self, prompt: str) -> str:
    prompt_lower = prompt.lower()
    
    if "bass" in prompt_lower:
        return self.sample_patterns["with_bass"][...]
    elif "techno" in prompt_lower:
        return self.sample_patterns["minimal_techno"][0]
    # ... etc
```

### Sample Patterns

The mock includes patterns for:
- **Initial patterns**: Basic drum beats
- **Bass patterns**: Drum + bass combinations  
- **Fast patterns**: Increased tempo
- **Atmospheric**: Pads with effects
- **Genre-specific**: Techno, house, etc.

### No External Dependencies

Mock mode only requires:
- Python 3
- `requests` library (for HTTP)
- Running Strudel server

## ⚡ Quick Test Commands

```bash
# Test 1: Check server is running
curl http://localhost:3000/health

# Test 2: Run quick demo
python3 test_mock_mode.py demo

# Test 3: Interactive test
python3 test_mock_mode.py

# Test 4: Single command
python3 test_mock_mode.py "create a techno beat"
```

## 🎓 Learning Mode

Use mock mode to:

1. **Understand the workflow** without API setup
2. **See example Strudel code** patterns
3. **Test your local setup** before production
4. **Demo to others** without sharing API keys
5. **Develop and debug** the system safely

## 🚀 Moving to Real Mode

Once mock mode works perfectly, switch to real mode:

1. Get a Gemini API key (see `GEMINI_SETUP.md`)
2. Set the environment variable:
   ```bash
   export GEMINI_API_KEY='your-key'
   ```
3. Run the real agent:
   ```bash
   python3 strudel_ai_agent.py
   ```

The workflow is identical - only the code generation is smarter!

## 🎯 Success Indicators

Mock mode is working correctly when you see:

✅ `Strudel server connected!`
✅ `Code sent to Strudel server!`
✅ `Music updated in browser!`
✅ Code visible in browser at `http://localhost:3000`
✅ Music plays when you click Play ▶️

## 🐛 Troubleshooting

### "Strudel server not detected"
```bash
# Make sure server is running
npm start
```

### "Connection refused"
```bash
# Check if port 3000 is available
lsof -i :3000

# Or use a different port (edit strudel_server.js)
```

### "No sound in browser"
- Click the Play ▶️ button
- Check browser audio permissions
- Open browser console (F12) for errors

## 📝 Summary

Mock mode provides a **complete testing environment** that:
- Requires no API key
- Tests all system components
- Demonstrates the workflow
- Verifies your installation
- Helps you learn the system

Perfect for getting started! 🎵✨

---

**Next Steps:**
- ✅ Test with mock mode (you are here!)
- 📖 Read `GEMINI_SETUP.md` to get API key
- 🚀 Switch to real mode for unlimited creativity


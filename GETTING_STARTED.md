# 🚀 Getting Started with Strudel AI Live Coding

Welcome! This guide will get you up and running in 5 minutes.

## 📋 What You Need

- ✅ Python 3.8 or higher
- ✅ Node.js 16 or higher
- ✅ OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- ✅ A modern web browser

## ⚡ Quick Start (3 Steps)

### Step 1: Set Your API Key

```bash
export OPENAI_API_KEY='your-api-key-here'
```

💡 **Tip**: Add this to your `~/.bashrc` or `~/.zshrc` to make it permanent.

### Step 2: Install Dependencies

Run the automatic setup:
```bash
./quickstart.sh
```

Or manually:
```bash
pip install -r requirements.txt
npm install
```

### Step 3: Start the System

**Terminal 1** - Start the web server:
```bash
npm start
```

**Terminal 2** - Run the AI agent:
```bash
python3 strudel_ai_agent.py
```

**Browser** - Open [http://localhost:3000](http://localhost:3000)

## 🎹 Your First Live Coding Session

Once everything is running, you'll see:

```
🎵 Strudel AI Live Coding Agent - Interactive Mode
==================================================
✅ Strudel server connected!

Commands:
  - Type your music description to start or update
  - 'code' - Show current code
  - 'quit' or 'exit' - Exit the session

==================================================

🎹 > _
```

### Try This First Prompt:

```
create a minimal techno track with a driving kick drum and rolling hi-hats
```

The AI will:
1. ✨ Generate Strudel code
2. 📤 Send it to the server
3. 🎵 Music starts playing in your browser!

### Now Update It:

```
🎹 > add a dark bassline
```

The music updates while playing! 🎊

## 🎯 Example Session

Here's a complete example session:

```bash
🎹 > create a deep house track with warm pads and 4/4 kick

📝 Generated code:
--------------------------------------------------
stack(
  s("bd bd bd bd").gain(0.8),
  s("~ cp ~ cp").room(0.3),
  note("c3 e3 g3 b3").s("sawtooth").slow(2).lpf(600)
)
--------------------------------------------------
✅ Code sent to Strudel server!

🎹 > add some shaker percussion

📝 Updated code:
--------------------------------------------------
stack(
  s("bd bd bd bd").gain(0.8),
  s("~ cp ~ cp").room(0.3),
  s("shaker*8").gain(0.3),
  note("c3 e3 g3 b3").s("sawtooth").slow(2).lpf(600)
)
--------------------------------------------------
✅ Code sent to Strudel server!

🎹 > make it more funky

📝 Updated code:
--------------------------------------------------
stack(
  s("bd ~ bd ~ bd ~ bd ~").gain(0.8),
  s("~ cp ~ cp").room(0.3),
  s("shaker*8").gain(0.3),
  note("c2 ~ e2 ~ g2 ~ a2 ~").s("sawtooth").lpf(500)
)
--------------------------------------------------
✅ Code sent to Strudel server!
```

## 🎨 Genre Examples

### Techno
```
create a dark techno track with industrial sounds and heavy kicks
```

### House
```
make an uplifting house track with piano chords and classic 4/4 beat
```

### Ambient
```
generate an ambient soundscape with slow pads and gentle textures
```

### Drum & Bass
```
create a fast drum and bass pattern with complex breaks
```

### Experimental
```
make an experimental glitch pattern with random elements
```

## 🎛️ Web Interface

Your browser window shows:

- 📝 **Current Code Panel**: See the generated Strudel code
- 🎹 **Strudel Player**: Interactive music player
- ▶️ **Play Button**: Start/restart playback
- ⏹️ **Stop Button**: Stop the music
- 🔄 **Refresh Button**: Reload code from server

The interface automatically updates when you send new prompts!

## 🔍 Verify Your Setup

Run the test script:
```bash
./test_system.sh
```

You should see all green checkmarks ✅

## 📚 Next Steps

1. **Read the Usage Guide**: `USAGE_GUIDE.md` for advanced techniques
2. **Try Examples**: `python3 demo_examples.py list`
3. **Experiment**: Try different genres and styles
4. **Learn Strudel**: Understanding the output helps you give better prompts

## 🎵 Tips for Success

1. **Start Simple**: Begin with basic beats, add complexity gradually
2. **Be Specific**: Describe genre, instruments, and mood
3. **Iterate**: Make small changes to evolve your sound
4. **Listen**: Let each change play before making another
5. **Experiment**: Try unexpected combinations!

## 🆘 Common Issues

### No sound in browser?
- Click the Play button ▶️
- Check browser audio permissions
- Verify server is running (`npm start`)

### API errors?
- Check your API key is set: `echo $OPENAI_API_KEY`
- Verify you have credits: [OpenAI Dashboard](https://platform.openai.com/usage)

### Connection errors?
- Ensure server is running at `http://localhost:3000`
- Check no other app is using port 3000

### Code doesn't update?
- Verify both server and agent are running
- Check browser console for errors (F12)
- Click the Refresh button 🔄

## 💡 Interactive Commands

While in the AI agent:

- **Type any music description** → Generate/update code
- **`code`** → Show current code
- **`quit`** or **`exit`** → Exit the session
- **Ctrl+C** → Emergency exit

## 🎪 Demo Mode

Want to see it in action? Run a pre-built demo:

```bash
python3 demo_examples.py demo techno
```

Available demos: `techno`, `house`, `ambient`, `drum_and_bass`, `experimental`

## 🌟 You're Ready!

You now have a powerful AI music production system at your fingertips!

**What to try:**
- 🎹 Live performance with audience suggestions
- 🎼 Compositional experiments
- 🎓 Learning Strudel through AI examples
- 🎨 Sound design exploration

**Have fun creating music!** 🎵✨

---

**Need Help?**
- Check `README.md` for complete documentation
- Read `USAGE_GUIDE.md` for advanced techniques
- View `PROJECT_STRUCTURE.txt` for technical details

**Share Your Creations!** 🎉


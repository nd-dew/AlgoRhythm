# 🎵 Strudel AI Live Coding Agent

An AI-powered live coding system that generates and updates [Strudel](https://strudel.cc/) music code based on natural language prompts. Perfect for electronic music producers who want to experiment with AI-assisted composition and live performance.

## 🌟 Features

- **Natural Language to Code**: Describe your music in plain English, and the AI generates Strudel code
- **Live Updates**: Continuously modify your music by sending new prompts while it's playing
- **Genre-Aware**: Understands different electronic music genres (techno, house, ambient, etc.)
- **Interactive Mode**: Real-time conversation with the AI to evolve your music
- **Web Interface**: Beautiful browser-based interface to visualize and play your code
- **Automatic Playback**: Code updates are automatically reflected in the music

## 🎯 How It Works

1. **User Input**: Describe your desired music (genre, instruments, feel)
2. **AI Generation**: GPT-4 generates appropriate Strudel code
3. **Live Playback**: Code is sent to the Strudel player and plays automatically
4. **Continuous Updates**: Keep sending prompts to evolve the music in real-time

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- OpenAI API key

## 🚀 Installation

### 1. Clone or Download

```bash
cd /tmp
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Node.js Dependencies

```bash
npm install
```

### 4. Set Up OpenAI API Key

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or add it to your `~/.bashrc` or `~/.zshrc`:

```bash
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## 🎮 Usage

### Starting the System

The system consists of two components:

#### 1. Start the Strudel Server (Terminal 1)

```bash
npm start
```

This will start the web server at `http://localhost:3000`

#### 2. Open the Web Interface

Open your browser and navigate to:
```
http://localhost:3000
```

You should see the Strudel AI Live Coding interface.

#### 3. Run the AI Agent (Terminal 2)

**Interactive Mode** (Recommended):
```bash
python strudel_ai_agent.py
```

Then type your prompts interactively:
```
🎹 > create a dark techno track with heavy kicks and atmospheric pads
```

**Single Command Mode**:
```bash
python strudel_ai_agent.py "create a dark techno track with heavy kicks"
```

## 💡 Example Prompts

### Initial Generation

Start with descriptive prompts that include:
- **Genre**: "techno", "house", "ambient", "drum and bass"
- **Instruments**: "kicks", "snares", "hi-hats", "pads", "bass"
- **Feel**: "dark", "uplifting", "minimal", "atmospheric"

**Examples:**
```
create a minimal techno track with driving kicks and subtle hi-hats

make an uplifting house track with piano chords and claps

generate ambient music with slow pads and reverb

build a drum and bass pattern with fast breaks and deep bass
```

### Live Updates

Once music is playing, you can update it:

```
add more hi-hats

make it faster

add a melodic bassline

increase the reverb

make it more minimal

add a breakdown section
```

## 🎹 Strudel Syntax Reference

The AI generates code using Strudel's pattern language:

### Basic Patterns
```javascript
// Simple drum pattern
s("bd sd hh sd")

// Multiple layers with comma
s("bd bd, ~ cp ~ cp, hh*8")
```

### Common Samples
- `bd` - Bass drum / Kick
- `sd` - Snare drum
- `hh` - Hi-hat
- `cp` - Clap
- `oh` - Open hi-hat
- `ch` - Closed hi-hat

### Methods
```javascript
.fast(2)        // Double the speed
.slow(2)        // Half the speed
.gain(0.8)      // Volume (0-1)
.room(0.5)      // Reverb
.delay(0.3)     // Delay effect
.lpf(800)       // Low-pass filter
```

### Melodies
```javascript
note("c3 e3 g3 a3").s("sawtooth")
```

### Layering
```javascript
stack(
  s("bd sd bd sd"),
  s("hh*8"),
  note("c2 e2").s("sawtooth")
)
```

## 🎛️ Architecture

```
┌─────────────────────┐
│  User Input (CLI)   │
│  Natural Language   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  AI Agent (Python)  │
│  - GPT-4 API        │
│  - Prompt Engine    │
│  - Code Generation  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Strudel Server     │
│  (Node.js/Express)  │
│  - Code Storage     │
│  - HTTP API         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Web Interface      │
│  - Code Display     │
│  - Strudel Player   │
│  - Visual Feedback  │
└─────────────────────┘
```

## 📁 File Structure

```
.
├── strudel_ai_agent.py    # Main AI agent (Python)
├── strudel_server.js       # Web server (Node.js)
├── package.json            # Node.js dependencies
├── requirements.txt        # Python dependencies
├── public/
│   └── index.html         # Web interface
└── README.md              # This file
```

## 🔧 Configuration

### Changing the AI Model

Edit `strudel_ai_agent.py`:
```python
response = self.client.chat.completions.create(
    model="gpt-4",  # Change to "gpt-3.5-turbo" for faster/cheaper
    messages=messages,
    temperature=0.7,  # Adjust creativity (0-1)
    max_tokens=1000
)
```

### Changing the Server Port

Edit `strudel_server.js`:
```javascript
const PORT = 3000;  // Change to your preferred port
```

Then update the agent:
```python
self.server_url = "http://localhost:3000"  # Match the port
```

## 🎨 Tips for Best Results

1. **Be Specific**: Include genre, instruments, and mood in your prompts
2. **Iterative Updates**: Make small changes rather than complete rewrites
3. **Use Musical Terms**: The AI understands music production terminology
4. **Experiment**: Try different descriptions to discover new sounds
5. **Layer Gradually**: Start simple, then add complexity with updates

## 🐛 Troubleshooting

### "OpenAI API key not found"
Make sure you've set the environment variable:
```bash
export OPENAI_API_KEY='your-key-here'
```

### "Strudel server not detected"
Ensure the Node.js server is running in a separate terminal:
```bash
npm start
```

### Code generates but no sound
1. Check the web interface at `http://localhost:3000`
2. Click the "Play" button
3. Ensure your browser allows audio

### Connection errors
Make sure both the server (port 3000) and the AI agent are running.

## 🎓 Learning Resources

- [Strudel Documentation](https://strudel.cc/learn)
- [Strudel Tutorial](https://strudel.cc/tutorial)
- [Live Coding](https://toplap.org/)

## 🚀 Advanced Usage

### Batch Processing

Generate multiple variations:
```python
# Create a script to generate variations
variations = [
    "minimal techno",
    "add more complexity",
    "make it melodic",
    "add breaks"
]

for prompt in variations:
    agent.update_session(prompt)
    time.sleep(10)  # Let each play for 10 seconds
```

### Custom Prompts

Modify the system prompt in `strudel_ai_agent.py` to customize the AI's behavior for specific genres or styles.

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Contributions welcome! This is an experimental project perfect for:
- Adding new genres and styles
- Improving prompt engineering
- Enhancing the web interface
- Adding recording capabilities
- Creating preset libraries

## 🎵 Examples Gallery

### Dark Techno
```
Prompt: "create a dark techno track with heavy kicks and industrial sounds"
```

### Minimal House
```
Prompt: "make a minimal house track with subtle percussion and deep bass"
```

### Ambient Soundscape
```
Prompt: "generate an ambient soundscape with slow evolving pads"
```

### Breakbeat
```
Prompt: "create a breakbeat pattern with chopped drums and bass"
```

## 🌐 Live Performance

Use this system for live performances by:
1. Connecting audio output to PA system
2. Using the web interface on a large screen
3. Taking audience suggestions as prompts
4. Creating evolving sets through continuous updates

---

**Made with ❤️ for the live coding community**


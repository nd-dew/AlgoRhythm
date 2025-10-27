# 📖 Strudel AI Live Coding - Usage Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Writing Effective Prompts](#writing-effective-prompts)
3. [Genre-Specific Tips](#genre-specific-tips)
4. [Advanced Techniques](#advanced-techniques)
5. [Troubleshooting](#troubleshooting)

## Getting Started

### First Steps

1. **Start with a clear vision**: Think about the genre, mood, and key elements
2. **Be descriptive**: Include tempo, instruments, and feel
3. **Iterate gradually**: Make small changes to evolve your sound

### Your First Session

```bash
# Terminal 1: Start the server
npm start

# Terminal 2: Run the AI agent
python3 strudel_ai_agent.py
```

### Example First Prompts

#### Techno
```
create a minimal techno track with a strong kick drum at 130 BPM, 
rolling hi-hats, and a dark atmosphere
```

#### House
```
make a deep house track with warm pads, smooth bassline, 
and classic 4/4 beat with claps on 2 and 4
```

#### Ambient
```
generate an ambient soundscape with slowly evolving pads, 
gentle reverb, and a peaceful atmosphere
```

## Writing Effective Prompts

### Anatomy of a Good Prompt

A good prompt includes:

1. **Genre/Style**: What type of music?
2. **Key Elements**: What instruments/sounds?
3. **Characteristics**: Tempo, mood, energy level?

### Template

```
[ACTION] a [GENRE] track with [INSTRUMENTS] and [CHARACTERISTICS]
```

### Examples

✅ **Good Prompts:**
```
create a dark techno track with heavy kicks, metallic percussion, 
and industrial atmosphere

make a melodic house track with piano chords, smooth bass, 
and uplifting energy

generate an experimental ambient piece with glitchy textures, 
field recordings, and sparse rhythms
```

❌ **Bad Prompts:**
```
make music                    # Too vague
add stuff                     # Not specific
make it sound better          # Subjective, unclear
```

## Genre-Specific Tips

### 🎛️ Techno

**Key Elements:**
- Strong 4/4 kick drum
- Rolling hi-hats (often fast)
- Minimal, repetitive patterns
- Industrial/metallic sounds
- Dark atmosphere

**Example Evolution:**
```
1. create a minimal techno track with driving kick
2. add rolling hi-hats at double time
3. introduce a squelchy acid bassline
4. add metallic percussion hits
5. make it more hypnotic and repetitive
```

**Strudel Code Example:**
```javascript
stack(
  s("bd").gain(0.8),
  s("hh*8").gain(0.4),
  s("~ ~ sd ~").room(0.3)
).fast(2)
```

### 🏠 House

**Key Elements:**
- Four-on-the-floor kick
- Claps/snares on 2 and 4
- Smooth basslines
- Piano/organ chords
- Uplifting vibe

**Example Evolution:**
```
1. make a classic house track with 4/4 kick and claps
2. add warm piano chords
3. introduce a funky bassline
4. layer shaker and percussion
5. add a breakdown with strings
```

**Strudel Code Example:**
```javascript
stack(
  s("bd bd bd bd"),
  s("~ cp ~ cp"),
  note("c3 e3 g3 b3").s("piano").slow(2)
)
```

### 🌊 Ambient

**Key Elements:**
- Slow tempo or no clear tempo
- Evolving pads and textures
- Heavy reverb and delay
- Atmospheric sounds
- Minimal percussion

**Example Evolution:**
```
1. generate an ambient soundscape with soft pads
2. add gentle bell-like tones
3. increase the reverb and space
4. introduce a subtle drone
5. add occasional percussive textures
```

**Strudel Code Example:**
```javascript
stack(
  note("c3 e3 g3").s("sawtooth").lpf(500).slow(4),
  s("hh").gain(0.2).delay(0.5).slow(8)
).room(0.9)
```

### ⚡ Drum and Bass

**Key Elements:**
- Fast tempo (160-180 BPM)
- Complex breakbeats
- Deep sub-bass
- High energy
- Atmospheric pads

**Example Evolution:**
```
1. create a drum and bass pattern with fast breaks
2. add a rolling reese bass
3. layer atmospheric pads
4. add a melodic lead
5. make it more energetic with fills
```

**Strudel Code Example:**
```javascript
stack(
  s("bd sd bd sd").fast(2),
  s("hh*16").gain(0.3),
  note("c2").s("sawtooth").lpf(200)
).fast(2)
```

## Advanced Techniques

### Layering and Building

Start simple and add complexity:

```
1. create a minimal kick pattern
2. add hi-hats with varied rhythms
3. introduce a snare on the 2 and 4
4. layer a bassline
5. add melodic elements
6. introduce effects and variations
```

### Using Musical Terms

The AI understands production terminology:

- **Rhythm**: "syncopated", "polyrhythmic", "four-on-the-floor"
- **Effects**: "reverb", "delay", "distortion", "filter sweep"
- **Dynamics**: "crescendo", "breakdown", "build-up", "drop"
- **Texture**: "sparse", "dense", "layered", "minimal"

### Structural Changes

```
add a breakdown section
create a build-up
introduce a drop
make an intro section
add variation every 8 bars
```

### Effect Requests

```
add more reverb
increase the delay feedback
apply a low-pass filter
make it more distorted
add sidechain compression to the bass
```

### Tempo Modifications

```
make it faster
slow it down
double the hi-hat speed
half the tempo
make the bass play at quarter speed
```

## Interactive Session Workflow

### Method 1: Exploratory

1. Start with a basic prompt
2. Listen to the result
3. Identify what you like/dislike
4. Make specific requests to modify
5. Repeat until satisfied

### Method 2: Planned

1. Plan your track structure
2. Start with the foundation (kick, bass)
3. Add rhythmic elements (hats, percussion)
4. Layer melodic elements
5. Add effects and polish
6. Create variations

### Method 3: Conversation

Treat it like talking to a producer:

```
🎹 > create a techno track

[AI generates code]

🎹 > that's good, but can you make the kick more prominent?

[AI updates]

🎹 > perfect! now add some acid bassline

[AI updates]

🎹 > love it! let's add some atmospheric elements
```

## Tips for Live Performance

### Preparation

1. Test your prompts beforehand
2. Have a list of changes ready
3. Practice transitioning between styles
4. Know your emergency commands ("stop", "simplify")

### During Performance

1. Make gradual changes
2. Use musical terms the audience understands
3. Explain what you're doing
4. Save interesting results

### Emergency Commands

```
simplify the pattern
remove everything except kick and bass
make it more minimal
bring back the previous version
start over with just a basic beat
```

## Common Workflows

### Workflow 1: Genre Exploration

```bash
# Start with one genre
🎹 > create a house track with classic elements

# Gradually shift to another
🎹 > add some techno influences
🎹 > make it more minimal and hypnotic
🎹 > now we're in techno territory, add industrial sounds
```

### Workflow 2: Energy Management

```bash
# Build energy
🎹 > create a minimal beat
🎹 > add more percussion layers
🎹 > increase the tempo feeling
🎹 > add a high energy lead

# Drop energy
🎹 > remove the lead
🎹 > simplify to just kick and bass
🎹 > slow down the tempo
🎹 > add ambient elements
```

### Workflow 3: Sound Design Focus

```bash
🎹 > create a pattern with interesting textures
🎹 > add more glitchy elements
🎹 > introduce filtered noise
🎹 > make it more experimental
🎹 > add random variations
```

## Understanding Strudel Output

### Reading the Code

The AI generates Strudel code like:

```javascript
stack(
  s("bd sd bd sd").gain(0.8),      // Kick and snare pattern
  s("hh*8").gain(0.4).delay(0.2),  // Fast hi-hats with delay
  note("c3 e3").s("sawtooth")      // Bassline
).room(0.5)                         // Reverb on everything
```

### Mini-Notation Guide

- `bd sd` - Sequential sounds (bass drum, snare)
- `hh*8` - Repeat hi-hat 8 times
- `~` - Rest/silence
- `[bd sd]` - Choose randomly
- `bd:2` - Use variation 2 of bass drum
- `,` - Layer patterns

## Prompt Library

### Quick Fixes

```
make it louder/quieter
add/remove reverb
faster/slower
more/less minimal
darker/brighter sound
```

### Instrument Additions

```
add a bassline
introduce hi-hats
layer some claps
add a melodic lead
bring in some pads
```

### Mood Changes

```
make it more:
- aggressive
- smooth
- dark
- uplifting
- hypnotic
- energetic
- mellow
- intense
```

## Troubleshooting

### "Code doesn't sound good"

- Be more specific in your prompt
- Describe what's wrong ("too busy", "needs more bass")
- Try starting over with a clearer vision

### "Changes are too drastic"

- Request smaller modifications
- Use terms like "slightly", "subtle", "gentle"
- Reference specific elements to change

### "Not the genre I wanted"

- Be very explicit about genre
- Include specific genre characteristics
- Give examples of artists/tracks as reference
- Use genre-specific terminology

### "Too repetitive"

```
add some variation
introduce random elements
make it more dynamic
add fills and breaks
change the pattern every 4 bars
```

### "Too chaotic"

```
simplify the pattern
make it more minimal
reduce the number of elements
focus on the groove
make it more repetitive
```

## Best Practices

1. **Start Simple**: Begin with basic elements, add complexity gradually
2. **Be Patient**: Give each change time to evaluate
3. **Save Good Results**: Note down prompts that work well
4. **Experiment**: Try unexpected combinations
5. **Learn Strudel**: Understanding the output helps you give better prompts
6. **Context Matters**: The AI remembers previous changes
7. **Clear Communication**: Be specific about what you want

## Resources

- [Strudel Documentation](https://strudel.cc/)
- [Strudel Tutorial](https://strudel.cc/tutorial)
- [Live Coding Community](https://toplap.org/)

---

Happy live coding! 🎵


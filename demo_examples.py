#!/usr/bin/env python3
"""
Demo Examples for Strudel AI Live Coding
Shows various prompts and their expected outputs
"""

EXAMPLE_PROMPTS = {
    "techno": [
        "create a minimal techno track with driving kicks at 130 BPM",
        "add rolling hi-hats",
        "introduce a dark acidic bassline",
        "add industrial percussion elements",
        "make it more aggressive"
    ],
    
    "house": [
        "make an uplifting house track with piano chords and four-on-the-floor kick",
        "add claps on the 2 and 4",
        "layer some shaker percussion",
        "add a funky bassline",
        "increase the energy"
    ],
    
    "ambient": [
        "generate an ambient soundscape with slow evolving pads",
        "add subtle bell-like tones",
        "increase the reverb and space",
        "add a gentle rhythmic element",
        "make it more dreamy"
    ],
    
    "drum_and_bass": [
        "create a drum and bass pattern with fast breaks",
        "add a deep reese bass",
        "layer in some atmospheric pads",
        "add a melodic top line",
        "make it more energetic"
    ],
    
    "experimental": [
        "create an experimental glitch pattern with random elements",
        "add polyrhythmic percussion",
        "introduce pitched noise textures",
        "make it more chaotic",
        "add moments of silence"
    ]
}


def print_examples():
    """Print all example prompts"""
    print("🎵 Strudel AI Live Coding - Example Prompts\n")
    print("=" * 60)
    
    for genre, prompts in EXAMPLE_PROMPTS.items():
        print(f"\n📁 {genre.upper().replace('_', ' ')}")
        print("-" * 60)
        print("\nStart with:")
        print(f"  → {prompts[0]}")
        print("\nThen evolve with:")
        for i, prompt in enumerate(prompts[1:], 1):
            print(f"  {i}. {prompt}")
        print()


def run_demo(agent, genre="techno"):
    """Run a demo session with predefined prompts"""
    if genre not in EXAMPLE_PROMPTS:
        print(f"❌ Unknown genre: {genre}")
        print(f"Available genres: {', '.join(EXAMPLE_PROMPTS.keys())}")
        return
    
    prompts = EXAMPLE_PROMPTS[genre]
    
    print(f"\n🎵 Starting {genre.upper()} demo session")
    print("=" * 60)
    
    # Initial generation
    print("\n1️⃣ INITIAL GENERATION")
    agent.start_session(prompts[0])
    
    # Updates
    for i, prompt in enumerate(prompts[1:], 2):
        input(f"\n⏸️  Press Enter to apply update {i-1}/{len(prompts)-1}...")
        print(f"\n{i}️⃣ UPDATE: {prompt}")
        agent.update_session(prompt)
    
    print("\n✅ Demo complete!")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        print_examples()
    elif len(sys.argv) > 1 and sys.argv[1] == "demo":
        # Run demo mode
        from strudel_ai_agent import StrudelAIAgent
        import os
        
        if not os.getenv("GEMINI_API_KEY"):
            print("❌ Error: GEMINI_API_KEY not set")
            print("\nPlease set your Gemini API key:")
            print("  export GEMINI_API_KEY='your-api-key-here'")
            print("\nGet your API key at: https://makersuite.google.com/app/apikey")
            sys.exit(1)
        
        genre = sys.argv[2] if len(sys.argv) > 2 else "techno"
        agent = StrudelAIAgent()
        run_demo(agent, genre)
    else:
        print("Usage:")
        print("  python demo_examples.py list          # Show all examples")
        print("  python demo_examples.py demo [genre]  # Run demo (default: techno)")
        print("\nAvailable genres:", ", ".join(EXAMPLE_PROMPTS.keys()))


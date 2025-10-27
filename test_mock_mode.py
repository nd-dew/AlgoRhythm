#!/usr/bin/env python3
"""
Mock Mode Test for Strudel AI Live Coding
Tests the system without requiring a real Gemini API key
"""

import os
import time
import requests
from typing import Optional


class MockStrudelAIAgent:
    """Mock AI agent that returns sample Strudel code without API calls"""
    
    def __init__(self):
        """Initialize the mock agent"""
        self.current_code = ""
        self.server_url = "http://localhost:3000"
        self.update_count = 0
        
        # Sample Strudel code patterns for different scenarios
        self.sample_patterns = {
            "initial": [
                's("bd sd bd sd").gain(0.8)',
                'stack(\n  s("bd bd bd bd").gain(0.8),\n  s("~ cp ~ cp").room(0.3)\n)',
                's("bd ~ bd ~, ~ ~ cp ~, hh*8").room(0.4)',
            ],
            "with_bass": [
                'stack(\n  s("bd sd bd sd").gain(0.8),\n  note("c2 ~ e2 ~").s("sawtooth").lpf(400)\n)',
                'stack(\n  s("bd bd bd bd"),\n  s("~ cp ~ cp"),\n  note("c2 c2 e2 f2").s("sawtooth").slow(2).lpf(300)\n)',
            ],
            "faster": [
                's("bd sd bd sd").fast(2).gain(0.8)',
                'stack(\n  s("bd bd bd bd").fast(1.5),\n  s("~ cp ~ cp").fast(1.5),\n  s("hh*16").gain(0.3)\n)',
            ],
            "atmospheric": [
                'stack(\n  s("bd sd bd sd"),\n  note("c3 e3 g3 a3").s("sawtooth").slow(4).room(0.8).lpf(600)\n)',
                'stack(\n  s("bd ~ bd ~"),\n  note("c3 e3 g3").s("triangle").slow(8).room(0.9).delay(0.5)\n)',
            ],
            "minimal_techno": [
                'stack(\n  s("bd ~ ~ ~ bd ~ ~ ~").gain(0.9),\n  s("~ ~ ~ ~ ~ ~ cp ~").room(0.3),\n  s("hh*8").gain(0.4)\n).fast(2)',
            ],
            "house": [
                'stack(\n  s("bd bd bd bd").gain(0.8),\n  s("~ cp ~ cp").room(0.4),\n  note("c3 e3 g3 b3").s("piano").slow(2),\n  s("shaker*8").gain(0.3)\n)',
            ],
        }
    
    def _get_sample_code(self, prompt: str) -> str:
        """Return appropriate sample code based on prompt keywords"""
        prompt_lower = prompt.lower()
        
        # Detect prompt type and return appropriate code
        if "bass" in prompt_lower:
            return self.sample_patterns["with_bass"][self.update_count % 2]
        elif "faster" in prompt_lower or "speed" in prompt_lower:
            return self.sample_patterns["faster"][self.update_count % 2]
        elif "atmospheric" in prompt_lower or "pad" in prompt_lower or "ambient" in prompt_lower:
            return self.sample_patterns["atmospheric"][self.update_count % 2]
        elif "techno" in prompt_lower:
            return self.sample_patterns["minimal_techno"][0]
        elif "house" in prompt_lower:
            return self.sample_patterns["house"][0]
        else:
            # Default to initial patterns
            return self.sample_patterns["initial"][self.update_count % 3]
    
    def generate_code(self, user_input: str, is_update: bool = False) -> str:
        """Generate mock Strudel code"""
        print(f"\n🤖 [MOCK MODE] Generating code for: {user_input}")
        
        # Simulate API delay
        time.sleep(0.5)
        
        code = self._get_sample_code(user_input)
        self.update_count += 1
        
        return code
    
    def update_strudel(self, code: str) -> bool:
        """Send code to Strudel server for execution"""
        try:
            response = requests.post(
                f"{self.server_url}/update",
                json={"code": code},
                timeout=5
            )
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"Error updating Strudel: {e}")
            return False
    
    def check_server(self) -> bool:
        """Check if Strudel server is running"""
        try:
            response = requests.get(f"{self.server_url}/health", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def check_web_prompt(self) -> Optional[str]:
        """Check if there's a new prompt from the web interface"""
        try:
            response = requests.get(f"{self.server_url}/get-prompt", timeout=2)
            if response.status_code == 200:
                data = response.json()
                if data.get('hasPrompt'):
                    return data.get('prompt')
            return None
        except:
            return None
    
    def start_session(self, initial_prompt: str):
        """Start a new live coding session"""
        print("🎵 Strudel AI Live Coding Agent - MOCK MODE")
        print("=" * 50)
        print("⚠️  Running in MOCK MODE (no API key required)")
        print(f"\nInitial prompt: {initial_prompt}")
        print("\nGenerating initial code...")
        
        # Check if server is running
        if not self.check_server():
            print("\n⚠️  Warning: Strudel server not detected at http://localhost:3000")
            print("Please start the Strudel server with: npm start")
            print("Continuing in code generation mode...\n")
        
        # Generate initial code
        code = self.generate_code(initial_prompt, is_update=False)
        if code:
            self.current_code = code
            print(f"\n📝 Generated code:\n")
            print("-" * 50)
            print(code)
            print("-" * 50)
            
            # Try to send to server
            if self.update_strudel(code):
                print("\n✅ Code sent to Strudel server!")
                print("🎵 Check your browser at http://localhost:3000")
            
            return True
        else:
            print("\n❌ Failed to generate initial code")
            return False
    
    def update_session(self, update_prompt: str):
        """Update the current live coding session"""
        print(f"\n🔄 Update request: {update_prompt}")
        print("\nGenerating updated code...")
        
        code = self.generate_code(update_prompt, is_update=True)
        if code:
            self.current_code = code
            print(f"\n📝 Updated code:\n")
            print("-" * 50)
            print(code)
            print("-" * 50)
            
            # Try to send to server
            if self.update_strudel(code):
                print("\n✅ Code sent to Strudel server!")
                print("🎵 Music updated in browser!")
            
            return True
        else:
            print("\n❌ Failed to generate updated code")
            return False
    
    def run_interactive(self):
        """Run the agent in interactive mode (now supports web prompts!)"""
        import threading
        
        print("🎵 Strudel AI Live Coding Agent - MOCK MODE")
        print("=" * 50)
        print("⚠️  Running in MOCK MODE (no API key required)")
        
        # Check server
        if self.check_server():
            print("✅ Strudel server connected!")
            print("💬 You can send prompts from:")
            print("   - Terminal (type here)")
            print("   - Web interface (AI Prompt field in browser)")
        else:
            print("⚠️  Strudel server not detected (code generation only mode)")
        
        print("\nCommands:")
        print("  - Type your music description to start or update")
        print("  - 'code' - Show current code")
        print("  - 'quit' or 'exit' - Exit the session")
        print("\n" + "=" * 50)
        
        has_initial_code = False
        running = True
        
        def check_web_prompts():
            """Background thread to check for web prompts"""
            nonlocal has_initial_code
            while running:
                try:
                    web_prompt = self.check_web_prompt()
                    if web_prompt:
                        print(f"\n💬 [WEB PROMPT] Received: {web_prompt}")
                        print("🤖 Processing...", end="", flush=True)
                        
                        # Process web prompt
                        if not has_initial_code:
                            success = self.start_session(web_prompt)
                            if success:
                                has_initial_code = True
                        else:
                            self.update_session(web_prompt)
                        
                        # Show prompt again for terminal input
                        print("\n🎹 [MOCK] > ", end="", flush=True)
                    
                    time.sleep(0.5)  # Check every 0.5 seconds
                except Exception as e:
                    # Silently continue on errors
                    time.sleep(1)
        
        # Start background thread for web prompts
        web_thread = threading.Thread(target=check_web_prompts, daemon=True)
        web_thread.start()
        
        while True:
            try:
                user_input = input("\n🎹 [MOCK] > ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Thanks for testing in mock mode!")
                    running = False
                    break
                
                if user_input.lower() == 'code':
                    if self.current_code:
                        print("\n📝 Current code:")
                        print("-" * 50)
                        print(self.current_code)
                        print("-" * 50)
                    else:
                        print("\n❌ No code generated yet")
                    continue
                
                # Generate or update code
                if not has_initial_code:
                    success = self.start_session(user_input)
                    if success:
                        has_initial_code = True
                else:
                    self.update_session(user_input)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for testing in mock mode!")
                running = False
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")


def run_demo_sequence(agent):
    """Run a pre-programmed demo sequence"""
    print("\n🎪 Running Demo Sequence...")
    print("=" * 50)
    
    sequence = [
        ("create a minimal techno track", 5),
        ("add a dark bassline", 5),
        ("make it faster", 5),
        ("add atmospheric pads", 5),
    ]
    
    # Initial
    agent.start_session(sequence[0][0])
    time.sleep(sequence[0][1])
    
    # Updates
    for prompt, wait in sequence[1:]:
        print(f"\n⏸️  Waiting {wait} seconds before next update...")
        time.sleep(wait)
        agent.update_session(prompt)
    
    print("\n\n✅ Demo sequence complete!")
    print("The music should be playing in your browser at http://localhost:3000")


def main():
    """Main entry point"""
    import sys
    
    print("\n╔════════════════════════════════════════════════╗")
    print("║   🎵 STRUDEL AI - MOCK MODE TEST              ║")
    print("║   No API key required!                         ║")
    print("╚════════════════════════════════════════════════╝\n")
    
    agent = MockStrudelAIAgent()
    
    # Check if demo mode requested
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        run_demo_sequence(agent)
    elif len(sys.argv) > 1:
        # Single command mode
        initial_prompt = " ".join(sys.argv[1:])
        agent.start_session(initial_prompt)
        print("\n💡 Tip: Run without arguments for interactive mode")
    else:
        # Interactive mode
        agent.run_interactive()


if __name__ == "__main__":
    main()


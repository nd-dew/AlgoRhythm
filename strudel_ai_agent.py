#!/usr/bin/env python3
"""
Strudel AI Live Coding Agent
An AI-powered live coding system for Strudel music generation
"""

import os
import json
import time
import requests
from typing import Dict, List, Optional
import google.generativeai as genai


class StrudelAIAgent:
    """AI agent for generating and updating Strudel live code"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the AI agent with Gemini API"""
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY environment variable.")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        
        # Initialize the model with appropriate settings
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 2048,
        }
        
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )
        
        self.current_code = ""
        self.conversation_history = []
        self.server_url = "http://localhost:3000"
        self.chat_session = None
        
    def _build_system_prompt(self) -> str:
        """Build the system prompt for Strudel code generation"""
        return """You are an expert electronic music producer and Strudel live coder. 
Strudel is a pattern-based live coding environment for making music in the browser.

Key Strudel concepts:
- Use functions like sound(), note(), s() for samples/synths
- Chain methods with .method() syntax
- Pattern mini-notation: "bd sd hh sd" plays bass drum, snare, hi-hat, snare
- Use .fast(n), .slow(n) for tempo changes
- Use .gain(n) for volume (0-1)
- Use .room(n), .delay(n), .lpf(freq) for effects
- Use stack() to layer patterns
- Common samples: bd (kick), sd (snare), hh (hi-hat), cp (clap)
- Synths: sawtooth, square, triangle
- Use note("c3 e3 g3") for melodies
- Use .struct() to apply rhythmic structure

IMPORTANT: Only output valid Strudel code, nothing else. No explanations, no markdown, just the code.
If updating existing code, provide the complete updated version.

Example patterns:
- Techno: s("bd sd bd sd").fast(2).gain(0.8)
- House: s("bd ~ ~ ~ bd ~ ~ ~, ~ cp ~ cp").room(0.5)
- Ambient: note("c3 e3 g3 a3").slow(2).s("sawtooth").lpf(800)
"""

    def _build_user_prompt(self, user_input: str, is_update: bool = False) -> str:
        """Build the user prompt for code generation"""
        if is_update:
            return f"""Current Strudel code:
{self.current_code}

User wants to update: {user_input}

Generate the complete updated Strudel code."""
        else:
            return f"""Generate Strudel code for: {user_input}

Include appropriate sounds, rhythms, and effects based on the description."""

    def generate_code(self, user_input: str, is_update: bool = False) -> str:
        """Generate Strudel code using AI"""
        try:
            # Build the prompt
            system_prompt = self._build_system_prompt()
            user_prompt = self._build_user_prompt(user_input, is_update)
            
            # Initialize chat session if this is the first message
            if self.chat_session is None:
                self.chat_session = self.model.start_chat(history=[])
            
            # Create the full prompt with system instructions
            full_prompt = f"{system_prompt}\n\n{user_prompt}"
            
            # Generate response
            response = self.chat_session.send_message(full_prompt)
            code = response.text.strip()
            
            # Clean up the code (remove markdown if present)
            if code.startswith("```"):
                lines = code.split("\n")
                # Remove first and last lines (markdown markers)
                if len(lines) > 2:
                    # Also remove language identifier if present
                    if lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines[-1].startswith("```"):
                        lines = lines[:-1]
                    code = "\n".join(lines)
            
            # Remove any trailing markdown
            if code.endswith("```"):
                code = code[:-3].strip()
            
            # Update conversation history for reference
            self.conversation_history.append({"role": "user", "content": user_prompt})
            self.conversation_history.append({"role": "assistant", "content": code})
            
            return code
            
        except Exception as e:
            print(f"Error generating code: {e}")
            print(f"Error details: {type(e).__name__}")
            return None

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

    def start_session(self, initial_prompt: str):
        """Start a new live coding session"""
        print("🎵 Strudel AI Live Coding Agent")
        print("=" * 50)
        print(f"\nInitial prompt: {initial_prompt}")
        print("\nGenerating initial code...")
        
        # Check if server is running
        if not self.check_server():
            print("\n⚠️  Warning: Strudel server not detected at http://localhost:3000")
            print("Please start the Strudel server with: node strudel_server.js")
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
            
            return True
        else:
            print("\n❌ Failed to generate updated code")
            return False

    def run_interactive(self):
        """Run the agent in interactive mode"""
        print("🎵 Strudel AI Live Coding Agent - Interactive Mode")
        print("=" * 50)
        
        # Check server
        if self.check_server():
            print("✅ Strudel server connected!")
        else:
            print("⚠️  Strudel server not detected (code generation only mode)")
        
        print("\nCommands:")
        print("  - Type your music description to start or update")
        print("  - 'code' - Show current code")
        print("  - 'quit' or 'exit' - Exit the session")
        print("\n" + "=" * 50)
        
        has_initial_code = False
        
        while True:
            try:
                user_input = input("\n🎹 > ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Thanks for live coding!")
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
                print("\n\n👋 Thanks for live coding!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")


def main():
    """Main entry point"""
    import sys
    
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("\nPlease set your Gemini API key:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        print("\nGet your API key at: https://makersuite.google.com/app/apikey")
        sys.exit(1)
    
    try:
        agent = StrudelAIAgent()
        
        # Check if initial prompt provided as argument
        if len(sys.argv) > 1:
            initial_prompt = " ".join(sys.argv[1:])
            agent.start_session(initial_prompt)
            print("\n💡 Tip: Run without arguments for interactive mode")
        else:
            agent.run_interactive()
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


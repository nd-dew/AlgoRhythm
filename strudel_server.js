/**
 * Strudel Server
 * Node.js server to handle Strudel code execution and live updates
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Store current code
let currentCode = `// Welcome to Strudel AI Live Coding
// Waiting for AI to generate code...

s("bd sd").fast(2)`;

// Store prompts from web interface
let promptQueue = [];
let currentPrompt = null;

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'ok', message: 'Strudel server is running' });
});

// Get current code
app.get('/code', (req, res) => {
    res.json({ code: currentCode });
});

// Update code endpoint
app.post('/update', (req, res) => {
    const { code } = req.body;
    
    if (!code) {
        return res.status(400).json({ error: 'Code is required' });
    }
    
    currentCode = code;
    console.log('\n🎵 Code updated:');
    console.log('-'.repeat(50));
    console.log(code);
    console.log('-'.repeat(50));
    
    res.json({ 
        success: true, 
        message: 'Code updated successfully',
        code: currentCode
    });
});

// Submit prompt from web interface
app.post('/prompt', (req, res) => {
    const { prompt } = req.body;
    
    if (!prompt || prompt.trim() === '') {
        return res.status(400).json({ error: 'Prompt is required' });
    }
    
    promptQueue.push({
        prompt: prompt.trim(),
        timestamp: new Date().toISOString()
    });
    
    console.log(`\n💬 New prompt received from web: "${prompt.trim()}"`);
    console.log(`📊 Queue length: ${promptQueue.length}`);
    
    res.json({ 
        success: true, 
        message: 'Prompt received',
        queueLength: promptQueue.length
    });
});

// Get next prompt (for Python agent to poll)
app.get('/get-prompt', (req, res) => {
    if (promptQueue.length > 0) {
        currentPrompt = promptQueue.shift();
        console.log(`\n📤 Sending prompt to agent: "${currentPrompt.prompt}"`);
        res.json({ 
            hasPrompt: true,
            prompt: currentPrompt.prompt,
            timestamp: currentPrompt.timestamp
        });
    } else {
        res.json({ 
            hasPrompt: false 
        });
    }
});

// Serve the main HTML page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start server
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════════╗
║   🎵 Strudel Server Running                   ║
║   http://localhost:${PORT}                        ║
╚════════════════════════════════════════════════╝

Endpoints:
  GET  /health      - Health check
  GET  /code        - Get current code
  POST /update      - Update code
  POST /prompt      - Submit AI prompt (from web)
  GET  /get-prompt  - Get next prompt (for AI agent)
  GET  /            - Web interface

Open http://localhost:${PORT} in your browser to see the live coding interface!
You can now send prompts from the web interface! 🎉
    `);
});


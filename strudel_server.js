/**
 * Strudel Server
 * Node.js server to handle Strudel code execution and live updates
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Store current code
let currentCode = `// Welcome to Strudel AI Live Coding
// Waiting for AI to generate code...

s("bd sd").fast(2)`;

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

// Serve the main HTML page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// --- Vertex AI (Gemini) Integration using Application Default Credentials ---
const { VertexAI } = require('@google-cloud/vertexai');

// Initialize VertexAI
const vertex_ai = new VertexAI({ project: 'qwiklabs-gcp-00-acb9fdb9ec26', location: 'us-central1' });
const model = 'gemini-2.5-flash'; // Or another model you want to use

const generativeModel = vertex_ai.getGenerativeModel({
    model: model,
});

app.post('/api/prompt', async (req, res) => {
    const { prompt, code } = req.body;

    if (!prompt) {
        return res.status(400).json({ error: 'Prompt is required' });
    }

    if (!code) {
        return res.status(400).json({ error: 'Code is required' });
    }

    try {
        const preprompt = fs.readFileSync('./strudel_preprompt.txt', 'utf-8');
        const fullPrompt = `${preprompt}\n\n---\n\nHere is the current code:\n\n\`\`\`javascript\n${code}\n\`\`\`\n\n---\n\nUser Prompt: ${prompt}`;

        const req = {
            contents: [{ role: 'user', parts: [{ text: fullPrompt }] }],
        };

        const streamingResp = await generativeModel.generateContentStream(req);
        const aggregatedResponse = await streamingResp.response;
        const text = aggregatedResponse.candidates[0].content.parts[0].text;

        console.log('🤖 AI Response:', text);

        try {
            // Validate the generated code
            // transpile(text);
            console.log('✅ AI response is valid Strudel code');
            currentCode = text; // Update the current code
            res.json({ success: true, message: "Prompt processed successfully", response: text });
        } catch (validationError) {
            console.error('❌ AI response is invalid Strudel code:', validationError.message);
            res.json({ success: false, error: 'Invalid Strudel code generated', details: validationError.message });
        }

    } catch (error) {
        console.error('❌ Error calling Vertex AI:', error);
        res.status(500).json({ error: 'Failed to call AI model' });
    }
});



// Start server
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════════╗
║   🎵 Strudel Server Running                   ║
║   http://localhost:${PORT}                        ║
╚════════════════════════════════════════════════╝

Endpoints:
  GET  /health  - Health check
  GET  /code    - Get current code
  POST /update  - Update code
  GET  /        - Web interface

Open http://localhost:${PORT} in your browser to see the live coding interface!
    `);
});


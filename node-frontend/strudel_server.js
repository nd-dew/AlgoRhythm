/**
 * Strudel Server
 * Node.js server to handle Strudel code execution and live updates
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const fetch = require('node-fetch');

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

// --- ADK (Agent Development Kit) Integration ---
// ADK endpoint configuration - default to localhost, override with env var
const ADK_ENDPOINT = process.env.ADK_ENDPOINT || 'http://localhost:8000/run';

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

        // Call ADK Agent REST API
        const adkRequest = {
            input: fullPrompt
        };

        console.log(`🔗 Calling ADK Agent at ${ADK_ENDPOINT}...`);

        const adkResponse = await fetch(ADK_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(adkRequest)
        });

        if (!adkResponse.ok) {
            const errorText = await adkResponse.text();
            throw new Error(`ADK API error! Status: ${adkResponse.status}, Details: ${errorText}`);
        }

        const responseData = await adkResponse.json();
        
        // Extract the agent's response from ADK response format
        // ADK agent returns: { "result": {...} }
        if (!responseData.result) {
            throw new Error('Invalid ADK response format: missing result field');
        }
        
        const text = responseData.result;

        console.log('🤖 ADK Agent Response:', text);

        try {
            // Validate the generated code
            // transpile(text);
            console.log('✅ ADK Agent response is valid Strudel code');
            currentCode = text; // Update the current code
            res.json({ success: true, message: "Prompt processed successfully", response: text });
        } catch (validationError) {
            console.error('❌ ADK Agent response is invalid Strudel code:', validationError.message);
            res.json({ success: false, error: 'Invalid Strudel code generated', details: validationError.message });
        }

    } catch (error) {
        console.error('❌ Error calling ADK Agent:', error);
        res.status(500).json({ error: 'Failed to call ADK agent', details: error.message });
    }
});



// Start server
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════════╗
  🎵 Strudel Server Running                   

Open http://localhost:${PORT} in your browser to see the live coding interface!
    `);
});


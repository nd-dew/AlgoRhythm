let strudelEditor;
        let isPlaying = false;
        let pollInterval;

        // Initialize Strudel editor
        window.addEventListener('DOMContentLoaded', () => {
            strudelEditor = document.getElementById('strudel-editor');

            // Wait for Strudel to fully load - check multiple times
            let checkCount = 0;
            const maxChecks = 10;
            
            const checkStrudelReady = () => {
                checkCount++;
                if (strudelEditor) {
                    // Check if shadow root is available
                    if (strudelEditor.shadowRoot) {
                        console.log('✅ Shadow root found!');
                        const cmEditor = strudelEditor.shadowRoot.querySelector('.cm-editor');
                        console.log('🔍 CodeMirror editor found:', !!cmEditor);
                        if (cmEditor) {
                            console.log('🔍 CM View available:', !!(cmEditor._cm || cmEditor.cmView));
                        }

                        return;
                    } else if (checkCount < maxChecks) {
                        // Shadow root not ready yet, check again
                        console.log('⏳ Shadow root not ready, checking again in 500ms...');
                        setTimeout(checkStrudelReady, 500);
                    }
                }
            };
            
            // Start checking after a short delay
            setTimeout(checkStrudelReady, 1000);
        });

        let lastCode = '';  // Track last code to detect changes

        async function updateCode(code) {
            // visually flash AI updates
            const container = document.getElementById('strudel-container');
            container.style.animation = 'flash 1s ease';
            setTimeout(() => {
                container.style.animation = '';
            }, 1000);

            // update the editor code and optionally play
            if (strudelEditor && strudelEditor.editor) {
                strudelEditor.editor.setCode(code);
            }

            setTimeout(() => {
                playCode();
            }, 200);
        }

        function playCode() {
            strudelEditor.editor.evaluate();
                isPlaying = true;
        }

        function stopCode() {
            strudelEditor.editor.stop();
        }

        async function sendPrompt() {
            const input = document.getElementById('prompt-input');
            const sendButton = document.getElementById('send-button');
            const prompt = input.value.trim();

            if (!prompt) {
                alert("Please enter a prompt first.");
                return;
            }

            input.value = '';

            // get current code from the editor
            let currentCode = strudelEditor.editor.code;

            if (!currentCode.trim()) {
                currentCode = "There is no code yet. Please start a new piece of music.";
            }

            sendButton.classList.add('loading');
            sendButton.disabled = true;
            input.disabled = true;

            try {
                const response = await fetch('/api/prompt', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt, code: currentCode })
                });
                const data = await response.json();

                if (data.success && data.response) {
                    await updateCode(data.response);
                } else {
                    console.error('Failed to process prompt:', data.error || data);
                    alert('AI failed to generate response. Check console for details.');
                }
            } catch (err) {
                console.error('Error sending prompt:', err);
                alert('Failed to connect to backend.');
            } finally {
                sendButton.classList.remove('loading');
                sendButton.disabled = false;
                input.disabled = false;
                input.focus();
            }
        }

        function handlePromptKeypress(event) {
            if (event.key === 'Enter') {
                sendPrompt();
            }
        }
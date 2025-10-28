import re

def clean_code_response(text):
    """Remove markdown code blocks and comment-only lines from the response"""
    # Remove markdown code blocks
    text = re.sub(r'```javascript\s*\n', '', text)
    text = re.sub(r'```js\s*\n', '', text)
    text = re.sub(r'\n```', '', text)
    text = re.sub(r'^```\s*', '', text)
    text = re.sub(r'```\s*$', '', text)
    
    # Remove comment-only lines
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith('//')]
    
    return '\n'.join(cleaned_lines).strip()

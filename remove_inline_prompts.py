import re

with open('template.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove SAMPLE_PROMPTS array definition
# Pattern: from "const SAMPLE_PROMPTS = [" to the matching "];"
pattern = r'const SAMPLE_PROMPTS = \[.*?\n        \];'
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed inline SAMPLE_PROMPTS from template.html")
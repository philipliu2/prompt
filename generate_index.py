import json

def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

# Read template
with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Read localStorage data
with open('localstorage.getitem.md', 'r', encoding='utf-8') as f:
    prompts = json.load(f)

print(f"Loaded {len(prompts)} prompts")

# Generate JavaScript array string
lines = []
for p in prompts:
    parts = []
    parts.append(f"id: {p.get('id', 0)}")
    parts.append(f'title: "{esc(p.get("title", ""))}"')
    parts.append(f'category: "{esc(p.get("category", ""))}"')
    parts.append(f'imageType: "{esc(p.get("imageType", ""))}"')
    parts.append(f'image: "{esc(p.get("image", ""))}"')
    parts.append(f"imageWidth: {p.get('imageWidth', 800)}")
    parts.append(f"imageHeight: {p.get('imageHeight', 600)}")
    parts.append(f'source: "{esc(p.get("source", ""))}"')
    parts.append(f'industry: "{esc(p.get("industry", ""))}"')
    parts.append(f'clickRate: "{p.get("clickRate", "")}"')
    parts.append(f"rating: {p.get('rating', 0)}")
    parts.append(f"likes: {p.get('likes', 0)}")
    parts.append(f"likedByMe: {'true' if p.get('likedByMe') else 'false'}")
    parts.append(f'tags: {json.dumps(p.get("tags", []))}')
    parts.append(f'text: "{esc(p.get("text", ""))}"')
    parts.append(f'textOptimized: "{esc(p.get("textOptimized", ""))}"')
    if 'createdAt' in p:
        parts.append(f"createdAt: {p['createdAt']}")

    lines.append('{ ' + ', '.join(parts) + ' }')

arr_str = 'const SAMPLE_PROMPTS = [\n            ' + ',\n            '.join(lines) + '\n        ];'

print(f"Array string length: {len(arr_str)}")

# Find and replace SAMPLE_PROMPTS in template
start_marker = 'const SAMPLE_PROMPTS = ['
end_marker = '];'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx) + len(end_marker)

print(f"Replacing from {start_idx} to {end_idx}")

new_html = html[:start_idx] + arr_str + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done! Written index.html")
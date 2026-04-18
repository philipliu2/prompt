import json

with open('localstorage.getitem.md', 'r', encoding='utf-8') as f:
    prompts = json.load(f)

def esc(s):
    return str(s).replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')

lines = []
for p in prompts:
    parts = []
    parts.append(f'id: {p.get("id", 0)}')
    parts.append(f'title: "{esc(p.get("title", ""))}"')
    parts.append(f'category: "{esc(p.get("category", ""))}"')
    parts.append(f'imageType: "{esc(p.get("imageType", ""))}"')
    parts.append(f'image: "{esc(p.get("image", ""))}"')
    parts.append(f'imageWidth: {p.get("imageWidth", 800)}')
    parts.append(f'imageHeight: {p.get("imageHeight", 600)}')
    parts.append(f'source: "{esc(p.get("source", ""))}"')
    parts.append(f'industry: "{esc(p.get("industry", ""))}"')
    parts.append(f'clickRate: "{esc(p.get("clickRate", ""))}"')
    parts.append(f'rating: {p.get("rating", 0)}')
    parts.append(f'likes: {p.get("likes", 0)}')
    parts.append(f'likedByMe: {"true" if p.get("likedByMe") else "false"}')
    parts.append(f'tags: {json.dumps(p.get("tags", []))}')
    parts.append(f'text: "{esc(p.get("text", ""))}"')
    parts.append(f'textOptimized: "{esc(p.get("textOptimized", ""))}"')
    if 'createdAt' in p:
        parts.append(f'createdAt: {p["createdAt"]}')
    lines.append('{ ' + ', '.join(parts) + ' }')

arr_str = 'const SAMPLE_PROMPTS = [\n            ' + ',\n            '.join(lines) + '\n        ];'

with open('prompts.js', 'w', encoding='utf-8') as f:
    f.write(arr_str)

print(f'Created prompts.js with {len(prompts)} prompts, {len(arr_str)} chars')
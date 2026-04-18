import json
import re

with open('template.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('prompts_data.json', 'r', encoding='utf-8') as f:
    prompts = json.load(f)

lines = []
for p in prompts:
    obj_str = '{ '
    obj_str += 'id: ' + str(p.get('id', 0)) + ', '
    title = p.get('title', '').replace('\\', '\\\\').replace('"', '\\"')
    obj_str += 'title: "' + title + '", '
    category = p.get('category', '').replace('\\', '\\\\').replace('"', '\\"')
    obj_str += 'category: "' + category + '", '
    imageType = p.get('imageType', '').replace('\\', '\\\\').replace('"', '\\"')
    obj_str += 'imageType: "' + imageType + '", '
    image = p.get('image', '').replace('\\', '\\\\').replace('"', '\\"')
    obj_str += 'image: "' + image + '", '
    obj_str += 'imageWidth: ' + str(p.get('imageWidth', 800)) + ', '
    obj_str += 'imageHeight: ' + str(p.get('imageHeight', 600)) + ', '
    source = p.get('source', '').replace('\\', '\\\\').replace('"', '\\"')
    obj_str += 'source: "' + source + '", '
    industry = p.get('industry', '').replace('\\', '\\\\').replace('"', '\\"')
    obj_str += 'industry: "' + industry + '", '
    obj_str += 'clickRate: "' + str(p.get('clickRate', '')) + '", '
    obj_str += 'rating: ' + str(p.get('rating', 0)) + ', '
    obj_str += 'likes: ' + str(p.get('likes', 0)) + ', '
    obj_str += 'likedByMe: ' + ('true' if p.get('likedByMe') else 'false') + ', '
    obj_str += 'tags: ' + json.dumps(p.get('tags', [])) + ', '
    text = p.get('text', '').replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    obj_str += 'text: "' + text + '", '
    textOpt = p.get('textOptimized', '').replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    obj_str += 'textOptimized: "' + textOpt + '"'
    if 'createdAt' in p:
        obj_str += ', createdAt: ' + str(p['createdAt'])
    obj_str += ' }'
    lines.append(obj_str)

arr_str = 'const SAMPLE_PROMPTS = [' + ',\\n            '.join(lines) + '];'

# Replace using string find/replace instead of regex
start_marker = 'const SAMPLE_PROMPTS = ['
end_marker = '];'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx) + len(end_marker)

new_html = html[:start_idx] + arr_str + html[end_idx:]

with open('index_fixed.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Done! Array length:', len(arr_str))
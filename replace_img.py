import re

files = [
    'd:/INDIA/wildlife.html',
    'd:/INDIA/personalities.html',
    'd:/INDIA/spiritual.html',
    'd:/INDIA/arts-crafts.html',
    'd:/INDIA/smart-cities.html',
    'd:/INDIA/learn.html',
    'd:/INDIA/data-india.html',
    'd:/INDIA/premium.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        alt = ''
        cls = ''
        m_alt = re.search(r'alt="([^"]*)"', match.group(0))
        if m_alt: alt = m_alt.group(1)
        
        m_cls = re.search(r'class="([^"]*)"', match.group(0))
        if m_cls: cls = m_cls.group(1)
        
        return f'<div class="animated-placeholder {cls}">{alt}</div>'

    content = re.sub(r'<img[^>]*unsplash\.com[^>]*>', replacer, content)

    # Replace background images
    content = re.sub(r'url\(\'https://images\.unsplash\.com[^\)]*\'\)', 'linear-gradient(-45deg, #FF9933, #138808, #000080)', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

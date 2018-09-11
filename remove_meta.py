#!/usr/bin/python3

import re
from pathlib import Path
result = list(Path('root').rglob('*.html'))

#pattern = '<aside id="meta-2" class="widget widget_meta">.*(?s)</aside>'
pattern = '(?s)<span class="comments-link">.*?</span>'
regex = re.compile(pattern)

for item in result:
    item = str(item)
    with open(item, 'r') as f:
        content = f.read()
    search = regex.search(content)
    while search:
        print('found pattern in {}'.format(item))
        section = content[search.start():search.end()]
        content = content.replace(section,'')
        search = regex.search(content)
    with open(item, 'w') as f:
        f.write(content)

print('done')

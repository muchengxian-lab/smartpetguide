import re

filepath = r'C:\Users\Administrator\smartpetguide\src\pages\guides\[slug].astro'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

terms = [
    ('automatic feeder', '<dfn>automatic feeder</dfn>'),
    ('automatic feeders', '<dfn>automatic feeders</dfn>'),
    ('smart feeder', '<dfn>smart feeder</dfn>'),
    ('self-cleaning litter box', '<dfn>self-cleaning litter box</dfn>'),
    ('self-cleaning litter boxes', '<dfn>self-cleaning litter boxes</dfn>'),
    ('automatic litter box', '<dfn>automatic litter box</dfn>'),
    ('automatic litter boxes', '<dfn>automatic litter boxes</dfn>'),
    ('cat water fountain', '<dfn>cat water fountain</dfn>'),
    ('cat fountain', '<dfn>cat fountain</dfn>'),
    ('stainless steel fountain', '<dfn>stainless steel fountain</dfn>'),
    ('pet camera', '<dfn>pet camera</dfn>'),
    ('pet cameras', '<dfn>pet cameras</dfn>'),
    ('GPS tracker', '<dfn>GPS tracker</dfn>'),
    ('GPS trackers', '<dfn>GPS trackers</dfn>'),
    ('water fountain', '<dfn>water fountain</dfn>'),
    ('smart fountain', '<dfn>smart fountain</dfn>'),
]

count = 0
lines = content.split('\n')
new_lines = []

for line in lines:
    if 'body:' in line and not '<dfn>' in line:
        modified = line
        for term, replacement in terms:
            if term in modified:
                modified = modified.replace(term, replacement, 1)
                count += 1
                break
        new_lines.append(modified)
    else:
        new_lines.append(line)

content = '\n'.join(new_lines)
print(f'Added <dfn> to {count} section bodies')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')

import re

with open('login.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('green in login:', 'green' in c.lower())

match = re.search(r'<button type="submit".*?</button>', c, re.DOTALL)
if match:
    print('Submit Button:', match.group(0))

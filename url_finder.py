import re
import pyperclip

text = pyperclip.paste()

url_pattern = re.compile(r'https?://[a-zA-Z0-9._/=?&\-;]+')
url_list = url_pattern.findall(text)

for url in url_list:
    print(url)

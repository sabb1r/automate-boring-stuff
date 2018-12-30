import re
import pyperclip

phone_pattern = re.compile(r'''
                                (\+88|88)?  # Country code of BD
                                (0\d{10})   # Mobile No.
                            ''', re.VERBOSE)
email_pattern = re.compile(r'''
                                [a-z0-9-_.]+ # User Account Name
                                @
                                [a-z0-9-_.]+ # Domain name
                                \.\w+        # TLD
                            ''', re.VERBOSE)

text = pyperclip.paste()

phone = [x[1] for x in phone_pattern.findall(text)]
email = email_pattern.findall(text)

output = '\n'.join(phone) + '\n' + '\n'.join(email)

pyperclip.copy(output)
print('Data copied to clipboard')
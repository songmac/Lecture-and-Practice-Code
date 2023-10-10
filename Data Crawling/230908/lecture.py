import re

numbers = """
010-2334-3234
02-302-3033
010-1321-4043
02-01-32
33-3303-3033
016-444-3042
""" 

results = re.finditer("[0-9]{3}-[0-9]{3,4}-[0-9]{4}", numbers)

for result in results:
    print(result.group())

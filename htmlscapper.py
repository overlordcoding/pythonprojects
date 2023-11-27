import requests as re
print("""
𝓟𝓸𝓻𝓽 𝓡𝓾𝓹𝓽𝓾𝓻𝓮 𝓢𝓬𝓪𝓷𝓷𝓮𝓻 𝓯𝓻𝓮𝓮 𝓮𝓭𝓲𝓽𝓲𝓸𝓷
""")
variable1 = input('Enter the url: ')
response = re.get(variable1)
html = response.text

print(html)
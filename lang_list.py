import json

booknames = {
    'akjv': [],
    'almeida': [],
    'japkougo': []
}

assets = ['akjv', 'almeida', 'japkougo']

for lang in assets:
    with open(f"./assets/{lang}.json", 'r') as file:
        data = json.load(file)

    books = data['books']
    for book in books:
        name = book['name']
        booknames[lang].append(name)

with open("booknames.json", 'w') as file:
    file.write(json.dumps(booknames))

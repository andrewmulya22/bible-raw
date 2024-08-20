# Example of reading JSON data in Python
import os
import json

# Set the directory to the current project directory
# Gets the directory of the current script
current_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'japkougo')
print(current_directory)

# Load JSON data from a file
with open('./assets/japkougo.json', 'r') as file:
    data = json.load(file)

# Print the loaded data
books = data['books']
for book in books:
    bookname = book['name']
    book_directory = os.path.join(current_directory, bookname)
    os.makedirs(book_directory, exist_ok=True)
    os.chdir(book_directory)

    chapters = book['chapters']
    for chapter in chapters:
        chapterno = chapter['chapter']
        chapter_directory = os.path.join(book_directory, str(chapterno))
        os.makedirs(chapter_directory, exist_ok=True)
        os.chdir(chapter_directory)

        verses = chapter['verses']
        for verse in verses:
            verseno = str(verse['verse'])
            with open(f"{verseno}.txt", 'w') as file:
                file.write(verse["text"])

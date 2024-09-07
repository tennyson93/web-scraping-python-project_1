## UPDATED README.md FILE
- Jefferson updated the README file.
to fix the issue of writing files  we move the "with open("output.txt", 'w', newline='', encoding='utf-8') as file:" block outside the loop, so that the file is opened once and then used to write the dat for each country.
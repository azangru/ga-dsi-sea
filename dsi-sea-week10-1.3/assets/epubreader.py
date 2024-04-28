import ebooklib
from ebooklib import epub
import re

class epub():
    def parse(self, file):
        book = epub.read_epub(file)
        content = []
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content += [re.sub(r'<[^>]*>', '', item.get_body_content())]

        new_file = file.replace(".epub",".txt")
        print new_file
        target = open(new_file, 'w')
        target.write(' '.join(content))
        target.close()

        return new_file
quantity_pages = 100
quantity_lines = 50
quantity_symbols = 25
storage_symbol = 4 #размер одного символа в байтах
mesto_na_diskete = 1.44 * 1024 * 1024 #место на дискете в байтах
weight_one_book = quantity_pages * quantity_lines * quantity_symbols *storage_symbol #вес одной книги в байтах

quantity_books = mesto_na_diskete // weight_one_book

print("Количество книг, помещающихся на дискету:", quantity_books)

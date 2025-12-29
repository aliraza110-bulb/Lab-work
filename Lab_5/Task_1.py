book_codes = ["FIC10521HAR", "BIO20753OXF", "SCI30584PEN"]

for book_codes in book_codes:
    book_category=book_codes[0:3]
    print("Book Category",book_category)
    Shelf_no=book_codes[3:5]
    print("Shelf number",Shelf_no)
    Book_number=book_codes[5:8]
    print("Book number",Book_number)
    print("-"*15)
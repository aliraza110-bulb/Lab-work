books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}

copy=books.copy()
print("The copy of books\n",books)

for title,prices in books.items():
    print("\nTitle",title,"\nPrices",prices)

total_price=sum(books.values())
print("\nTotal Price",total_price)

if "1984" in books:
    sold_book=books.pop("1984")
    print("\nTitle","1984","price",sold_book,"Removed From inventory\n")

print("\n\t\t\t------Updated Inventory------")
for title,prices in books.items():
    print("\nThe Updated Inventory Is","\nTitle",title,"\nPrices",prices)
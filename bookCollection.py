collectionOfBooks = ["The Goldfinch", "The Patrick Melrose Novels", "The Secret History"]
print("Enter the name of the book: ")
bookToBeChecked = input()

for book in collectionOfBooks:
  if book == bookToBeChecked:
    print("Yes, I do have that book!")
    break
else:
  print("Sorry, I don't have that book.")
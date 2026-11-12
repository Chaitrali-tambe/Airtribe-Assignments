from models import Book, Magazine, DVD, Member

# Creating items
book1 = Book("Python 101", 1, "A. Rao")
magazine1 = Magazine("NEXT_GEN TECH", 2, 142)
dvd1 = DVD("Inception", 3, 148)

#Creating members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items= 1)


print("--- Borrowing Tests ---")
try:
    alice.borrow(book1)
    print("Alice Borrowed: ", book1.describe())
    bob.borrow(book1)
except ValueError as e:
    print("Could not borrow", e)



try:
    bob.borrow(magazine1)
    dvd2 = DVD("Iterstellar", 4, 169)
    bob.borrow(dvd2)
except ValueError as e:
    print("Could not borrow:", e)

print()
print("--- Polymorphism (Late fees for 3 days) ---")
items =[book1, magazine1, dvd1]

for item in items:
    print(item.describe(), "--> Late Fee for 3 Days: Rs. ",item.late_fee(3))

print()
print("-- Class Attribute Check ---")
print("Total items created", Book.total_items)




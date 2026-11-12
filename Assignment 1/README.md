# Library Manager Project Reflection

1. **Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**
LibraryItem serves as a blueprint template that defines shared properties for all library items while preventing direct instantiation of generic items. If the DVD class forgets to implement the abstract method `late_fee()`, Python will raise a TypeError when attempting to instantiate a DVD object.

2. **What happens when you read item.__available from outside the class, and why do we use is_available() instead?**
Accessing `item.__available` from outside the class raises an `AttributeError` because Python performs name mangling on double-underscore private attributes to restrict external access. We use the public getter method `is_available()` to safely inspect the private state while keeping encapsulation intact.

3. **What is the difference between LibraryItem.total_items and self.title?**
`LibraryItem.total_items` is a class attribute shared across all instances of `LibraryItem` and its children, tracking the total number of items created globally. In contrast, `self.title` is an instance attribute unique to each individual object created from a class.

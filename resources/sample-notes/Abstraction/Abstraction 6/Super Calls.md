**Technical points in this video:**

- the **super** keyword is used to refer to a class's superclass.  
- Calling just **super()** calls the constructor in the superclass
- Calling **super.someMethod()** calls the superclass's implementation of someMethod.
- We can use calls to super from within the subclass's implementation of a method to extend the behaviour of the superclass's method without overwriting it completely.  So subclass.someMethod could, at some point, call super.someMethod() which would mean that someMethod was augmenting the implementation of someMethod as opposed to replacing it entirely.

You can download the Java project with accompanies this video [here](https://github.students.cs.ubc.ca/CPSC210/TPD-Lecture-Starters). The specific project which accompanies this video is **IntegerSetInterface2**.


# Augment the behavior of methods in a subclass by using the keyword 'super'
![[Pasted image 20250202221832.png]]

- we don't want to limit our premium customers to just caviar and cashews
- we want to fight the duplication, but we also want to method call the og
- so we can just say super.serveSnacks(); and it will call the original's serveSnacks as well!
- java knows the superclass of private plane is airplane!
- can also do this inside of constructors

# Another example - Chatty Integer Set
![[Pasted image 20250202222155.png]]
- everytime we insert, it says something chatty
![[Pasted image 20250202222407.png]]

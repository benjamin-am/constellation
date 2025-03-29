In this video we'll look at the first topic of this module: Types. 

**Technical points in this video:**

- A **Type** represents an abstraction in programming languages (even programming languages that don't look like they have types -- they do, but you might not see them)
- In Java, there are many options for how to capture Types: **Classes**, **Interfaces** and **Abstract Classes.** 
- All these types can be used to declare variables: you can declare objects to be of an interface type, of an abstract class type, or of a regular class type.
- Only regular Classes can be used to instantiate objects (you cannot call "new" on an interface or an abstract class)
![[Pasted image 20250202154216.png]]
# Review
- data abstractions have two parts
- specification
- internal implementation (hidden from outside world)
- java classes represent our data abstractions

# Java classes also allow us to define a type!
- what we are doing when we make a new java class - a new type

# Type is something you see when you declare a new variable

# Java provides
- int
- boolean
- etc all the primitives lol

if we were stuck with just declaring int and bool, it'd take us forever to do anything. So we use Java classes to define new types!
`IntegerSet mySet;`
- declare a mySet variable of type IntegerSet

So java allows us to define new types that you can use to declare variables

Java also allows us to create an object
an object is what we get when we say
` '= new IntegerSet();`
So on one side we have the declaration (left side, IntegerSet mySet)
then on the other side we have the object instantiation

![[Pasted image 20250202154612.png]]
- there are other options for types in Java as well!
# Interface
- also allows you to show the specification of a data abstraction
- no implementation allowed
- also no constructor obvs

# Abstract class
- lets you define a type, can declare a variable, specify, and allows you to provide implementation details, but you can't instantiate i
![[Pasted image 20250202154730.png]]


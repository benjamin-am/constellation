- A **class** is a kind of type in Java, and it can be used to extend other classes. (A class can also extend Abstract Classes, and implement Interfaces, as we will get into in a bit)
- An extends relationship looks like this: ![](https://edge.edx.org/asset-v1:UBC+CPSC210+all+type@asset+block/extends-relationship-1.png)
- Inheritance means that everything in a subclass gets everything from the superclass "for free". That means that we can call all superclass methods on any subclass (but not the reverse!). 
- Public fields and methods are visible to the subclass, as are fields and methods with protected visibility.  As usual, private fields and methods are visible only within the class in which they are declared, and are therefore not visible to subclasses.
- Java looks in the instantiated type of the object to find an implementation for a method, and if it doesn't find one, it looks up the hierarchy.

# Object Orientation lets us subtype off of regular classes as well
- we can have types of birds and types of airplanes
	- PrivatePlane
	- Hawk
- and these Extend these classes!
- non-dotted line
- big open triangle
- when you declare a class is a subclass of a regular class, you can `public class PrivatePlane extends Airplane`
![[Pasted image 20250202185011.png]]
- this is Subclassing
- PrivatePlane is a subclass of Airplane
![[Pasted image 20250202185034.png]]
- lets look more closely at this relationship
- we have a strong extends arrow
- PrivatePlane extends Airplane (is a subclass of)
- PrivatePlane actually has no implementation
	- even with nothing implemented inside this java file
- but PrivatePlane has methods!
	- it gets all of its superclasses's methods for free!
	- this is inheritance
# Inheritance
![[Pasted image 20250202190029.png]]
- ALL FOR FREE
- because Airplane is a superclass
- keeps looking up the inheritance hierarchy until it finds the method that is called!
![[Pasted image 20250202190116.png]]
- inherited a copy of every single one of theses methods
 
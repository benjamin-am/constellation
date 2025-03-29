**Technical points in this video:**

- Interfaces can be used to _declare_ variables
- Interfaces contain signatures of methods, but no implementations (just a semicolon after the parameter list). They are just a _listing_ of methods that all implementing types must fulfil. 
- Classes (Abstract or Regular) can both **implement** Interfaces
- To obtain an object _declared to be_ of an Interface type, you must instantiate a class that implements the interface.  
- **Inte**rfaceName** thingy = new ClassName();** where **ClassName implements InterfaceName {...}**

**The IMPLEMENTS relationship looks like this in a Unified Modelling Language (UML) class diagram:**
![[Pasted image 20250202154935.png]]
```java
Flyer noFlyer = new Flyer(); //this will not work!  
                             //can't instantiate an interface!
                             
Flyer myFlyer = new Bird(); //for this to work,  
                            // Bird must implement Flyer

public class Bird implements Flyer { }
```

# Interfaces
- no implementation allowed
- signatures only!
- give a list of public methods that the data abstraction will have

## Flyer interface example
- has all these operations
	- takeoff()
	- land()
	- fly()
- all we would do to define these operations
- `public void land();`
- `public void fly();`
- you get the point
- there would be NO curly braces, 0 implementation

## Interfaces are simply a listing of methods that a data abstraction should have

each of the operations in an interfaces have their own specifications
- looks like normal class

We will draw our classes using UML
- model classes with no details

# UML
- draw a box with a title area
	- in title put name of the type
- if it's an interface, indicate as so
- inside the box we put all the important operations
- drawings are for the viewer, so don't just list everything

# Once we have interface setup
- we can define variables with type Flyer!
- but we have NO `new Flyer();`
	- no interface can create an object
	- only regular classes can create objects

# relationship between interfaces and regular classes
- subtype relationships :O
- what we want to do, is declare variables of a certain type, and then be able to instantiate them as an object
- we have to introduce a subtype for flyer, that provides the implementations!
- we want to make a Java class that implements flyer!
`public class Bird implements Flyer`
- now we can instantiate Flyers as Birds!
- in order for this to work, bird needs to implement ALL the operations from Flyer in bird.
- and bird gets to make these methods however they want!
	- takeoff would be jump
	- fly would be flap
- in this relationship, Flyer is supertype, Bird is the subtype
- subtypes are always substitutable for their supertypes
	- aka you can use a Bird to represent a Flyer
- we can have many different subtypes!
`public class Airplane implements Flyer`
- now we have an airplane subtype!
- an implementation of an airplane would look super different from a bird
![[Pasted image 20250202160708.png]]

![[Pasted image 20250202160835.png]]
- some interfaces declare no methods?
![[Pasted image 20250202160854.png]]
![[Pasted image 20250202160938.png]]

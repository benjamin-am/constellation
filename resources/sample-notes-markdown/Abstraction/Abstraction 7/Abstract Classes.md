Follow along in the **Flyer2** project from the GitHub repository. You can download the repository [here](https://github.com/UBCx-Software-Construction/TPD-lecture-starters).

**Technical points in this video:**

- An **Abstract Class** sits in between a regular class and an Interface.  It is like a class, in that it can specify behaviour and data. It is like an interface, in that it can have abstract methods (these are not implemented, and just have a semicolon instead of { }) and cannot be instantiated
- Abstract methods are declared as: **abstract _visibility_ _returnType_ methodName(Parameter p);**
- Abstract classes are great for capturing **generic concepts** that have default behaviour and data, but which should not be made into objects.  For instance, it would be unusual to want to instantiate a generic "Animal" (you would instantiate "Dog" or "Cat" subtypes instead), but Animal itself might have a great deal of behaviour and data that all subtypes should inherit.
- _Technical point not mentioned in the video If an abstract class implements an interface, the abstract class does not need all the methods from the interface to be present -- but all the non-abstract subclasses of the abstract class would need to implement the interface in full._

## ****Difference Between Abstract Class and Interface****

|Points|Abstract Class|Interface|
|---|---|---|
|Definition|Cannot be instantiated; contains both abstract (without implementation) and concrete methods (with implementation)|Specifies a set of methods a class must implement; methods are abstract by default.|
|Implementation Method|Can have both implemented and abstract methods.|Methods are abstract by default; Java 8, can have default and static methods.|
|Inheritance|class can inherit from only one abstract class.|A class can implement multiple interfaces.|
|Access Modifiers|Methods and properties can have any access modifier (public, protected, private).|Methods and properties are implicitly public.|
|Variables|Can have member variables (final, non-final, static, non-static).|Variables are implicitly public, static, and final (constants).|

# Sits Between a Reg Class and Interface
- cannot instantiate it
- can have methods and fields inside of an abstract class


# Bird class
- methods with full implementation
	- has takeOff()
	- has land()
- methods with no implementation
	- fly()
	- we have to write abstract in its declaration!
	- similar to interface
- then we can subclass off of Bird
	- Hawk
	- HummingBird
	- both inherit takeOff and land
	- HAVE to implement the fly() method
![[Pasted image 20250202223934.png]]
the abstract class itself CANNOT be instantiated
`Bird b = new Hummingbird();`
CANNOT `Bird b = new Bird()` 
![[Pasted image 20250202224024.png]]
- Abstract classes are very useful for capturing generic types of things
- we use them for categories of things
	- have some fields, some private data, and default behaviour
	- but then can be used to supply subclasses
![[Pasted image 20250202224121.png]]

![[Pasted image 20250202224209.png]]
- remember subclasses need to implement fly
https://learning.edge.edx.org/course/course-v1:UBC+CPSC210+all/block-v1:UBC+CPSC210+all+type@sequential+block@7102cdfb327e45ae991f2a3bcc8a6afb/block-v1:UBC+CPSC210+all+type@vertical+block@8f2abdffe5a94229ae983af4cafd8e53
![[Pasted image 20250202224439.png]]
![[Pasted image 20250202225031.png]]

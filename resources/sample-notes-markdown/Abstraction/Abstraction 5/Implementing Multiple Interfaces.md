In this video we'll implement our FlyerInterface in IntelliJ. We start with a new IntelliJ project, but the completed project can be found in the Type Hierarchies, Polymorphism and Dispatch (TPD) lectures repository on the [GitHub](https://github.students.cs.ubc.ca/CPSC210/TPD-Lecture-Starters).

**Technical points in this video:**

- Classes can implement multiple interfaces, which means that they must provide the implementations for all the methods of all the interfaces implemented.
- **public class Classname implements Interface1, Interface2, ... {**
    

**// all methods for Interface1** 

**// all methods for Interface2  
}**

- _Note: if two implemented interfaces have a method of the same name this is no big deal: just implement one method with that name, however is appropriate for the class!

![[Pasted image 20250202171913.png]]
- imagine we also have a cafe interface
- we want our airplane to feel like a flying cafe.

![[Pasted image 20250202173144.png]]
- now airplane implements cafe
- we can declare all these methods on an airplane
- if we declare something to be a cafe we can call serveDrinks and serveSnacks

# You don't actually need public keyword in interface
- all interfaces have methods that are ONLY public

![[Pasted image 20250202173434.png]]
![[Pasted image 20250202173850.png]]
- now we can call methods on these classes
![[Pasted image 20250202173906.png]]
- bird can fly, land, takeOff, and all the other object methods that all objects get

![[Pasted image 20250202173927.png]]
cafePlane is missing airplane methods? :O
- only serveDrinks and serveSnacks
- since it is declared as a cafe, can only called the declared methods of an object

![[Pasted image 20250202174143.png]]
- same with as parameter - can only call cafe methods on c. It's the declared type
- even if they cafe is something substitutable, we can only use the methods in the parameter definition

![[Pasted image 20250202174237.png]]
- all the methods are available for cafe and flyer!

![[Pasted image 20250202174355.png]]
- bird is not the same class or subclass of cafe
![[Pasted image 20250202174407.png]]
- airplane IS a subclass of cafe/type of cafe

![[Pasted image 20250202174441.png]]
- lunchService's parameter is cafe. and Flyer is not a subclass of Cafe.
- Flyer is NOT substitutable for Cafe
	- java doesn't care that it was instantiated to be an airplane. Wants to match against declared types.
	- java cares a little bit - asks if you want to cast

![[Pasted image 20250202174537.png]]
- force java to accept the parameter based on its instantiated type - but we ignore this feature for now

![[Pasted image 20250202174856.png]]

![[Pasted image 20250202174833.png]]
- already has it from Dog, so doesn't need to implement
![[Pasted image 20250202174849.png]]

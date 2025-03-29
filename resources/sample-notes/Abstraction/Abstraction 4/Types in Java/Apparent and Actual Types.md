**Technical points in this video:**

- When you **declare** a variable (SomeType var), you are setting its **apparent type** to be the declared type.
- When you **instantiate** an object (var = new SomeClass() ) you are setting its **actual type** to be the instantiated type.
- The declared type determines what the object can do, while the instantiated actual type determines how the object will behave (more on this later)

![[Pasted image 20250202161103.png]]
![[Pasted image 20250202161352.png]]
- types are used to declare variables
- no implementation for the interfaces tho
- what do we do with these? they have no implementation?!
	- we instantiate them with subtypes!
![[Pasted image 20250202161526.png]]
- need some terminology to keep this straight
- when we say a flyer is a flyer
	- it's the declared type/apparent type
- apparently to java, this type is of type Flyer
	- it's what it is used to see if you can call methods on it
- and then with the other type, it is the instantiated type
	- we call this the actual type
	- the actual type is how the variable will actually behave
![[Pasted image 20250202161642.png]]
![[Pasted image 20250202161736.png]]

**Technical points in this video:**

- A parameter is a local variable declaration, so a parameter declaration sets the **apparent type** of the variable it is declaring. 
- When passing an argument into a method, the argument must have a declared type of the same type, or a subtype of the parameter's type.

![[Pasted image 20250202161834.png]]
- when passing parameters the thing that really matters is substitutability
- that means that if you have a parameter that's declared to be a particular type, you can pass in any subtype of that type.
![[Pasted image 20250202162027.png]]
- consider the above example
	- both are subtypes of Flyer
- therefore both can be passed to touchAndGo
- both will behave differently, since they have their own implementations of the methods
- we are allowed to call land and takeoff on flyer, because we listed it in the interface. But the actual type of f is used to run the method!
- touchAndGo will behave differently depending on if you pass a bird or airplane
	- this is subtype polymorphism
- ![[Pasted image 20250202162530.png]]
- subtype polymorphism
	- just means that an object has the ability to take on different froms depending on how it's instantiated.
	- f can behave like a bird or an airplane since they are both substitutable subtypes for a flyer
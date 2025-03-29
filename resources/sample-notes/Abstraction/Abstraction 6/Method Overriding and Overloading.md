**Technical points in this video:**

- a subclass can supply its own implementation for a method that also exists in the superclass.  This is called **method overriding**.
- Deciding which method to call (which implementation to use) is called **method dispatch.**
- Java's **method dispatch starts at the  instantiated/actual type**, meaning that it first looks in the instantiated type for the implementation, and then looks up the hierarchy until it finds an implementation.  

![](https://edge.edx.org/asset-v1:UBC+CPSC210+all+type@asset+block/apparent-actual-dispatch-methods-2.jpg)

- **Method overloading** means that there are two methods of the same name, but with different parameter lists (only the types of the parameters matter).  The parameter lists are used to distinguish which method to call.  

**void myMethod** **(Boolean b, int i) {...}**  (_AKA: myMethod-boolean-int_) is a different method than    
**void myMethod(Boolean b) {...}**  (_AKA myMethod-boolean_) Because their names are not actually the same.


# Overriding
- provide new implementations for methods, that will replace the implementations of the superclass methods

## Airplane example
- serveSnacks
	- serve chips
	- serve peanuts
- PrivatePlane serveSnacks @Override!
	- serve caviar
	- serve cashews
- it will look inside Actual type first
- then it will look up the hierarchy
- STARTS AT ACTUAL WORKS UP

Having the method in both is called Method Overriding
- because the private plane method totally overrides the airplane's serveSnacks method
- act of deciding which method to call by looking in actual then lookng up the hierarchy is called method dispatch
![[Pasted image 20250202221004.png]]
- if pp had not had a fly method inside of it, then we wouldn't be able to call fly on pp.
- we know which method we're allowed to call based on declared type
- but the implementation is based on the actual type
- left determines what is available
- right determines which implementation of the methods

# Method Overriding and Method Overloading are DIFFERENT
- two methods with almost the exact same name in the same class
- two fly methods
	- one has a parameter
- so method overloading is when you have multiple of the same method name, but differing parameters
- first one is technically called fly_void, the other is called fly_dir because it takes a direction
![[Pasted image 20250202221223.png]]
- so technically they are two different methods, with two different names to Java
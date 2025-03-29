**Technical points in this video:**

- **mutability** means that we can set the value of an object and it will remain changed. We saw this with variables earlier in this course.
- The **MODIFIES** clause indicates whether a method, or any method it calls, mutates any object.  
- If a method mutates its own object, we indicate that it **MODIFIES:** _**this**._
- If a method mutates another object, we indicate that it modifies that other object.
- If **A.a()** calls **B.b()**, and **B.b()** specifies that it modifies **_this_**, then **A.a()** would specify that it modifies **B**. 
- If nothing is modified in a method, or any method it calls, then we do not include the MODIFIES clause in the specification.
- Modifies clause only accounts for non-local changes.

# Mutability
- values can change
- and they can stay changed
- fundamental difference between object and functional
- functional
	- insert method
		- list (1, 2)
		- add 3 to list
		- what you would get is a brand new third list!
		- (1, 2, 3) concatenation of the lists
	- ![[Pasted image 20250116205920.png]]
	- 
- object oriented 
	- have a list with two elements
	- pass them into insert with a third element
	- instead of a brand new list, with brand new name
	- you modify the original list, and add the 3
	- the value is actually changing in place
	- ![[Pasted image 20250116205927.png]]
- this is visible in a simple situation like the assignment operator
- x = 1
	- put 1 into a spot with the symbol x
	- x = 2
	- change the VALUE 
- now x relates to 2.
- this is mutability it is fundamental on how modifies affects data abstractions
![[Pasted image 20250116210002.png]]

# How to specify modifies
- asks us to consider whether a method is making any changes to a data abstraction object
- lets recall deposit
```java
public double deposit(double amt) {
	balance = balance + amt;
	return balance;
}
```
this deposit method is visible to public
inside the private is the balance

so when we call deposit, we pass in an amount (5)
- passed to parameter to deposit
- deposit changes the balance, by the amount of parameter
- if we called again, then deposit would update balance again
![[Pasted image 20250116210201.png]]
- we see that d or some variable
- we see d change!
- we don't care what happens what happens in the private 
- the implementation is the placeholder
- all we think about is the public, visible interface
![[Pasted image 20250116210313.png]]

- all we consider is what the caller of the method should have to consider when it's calling that method, just like with the requires clause
- this deposit method will change something about the Account object
- to signify that, we write a modifies clause!
```java
// MODIFIES: this
```
![[Pasted image 20250116210437.png]]
- and we don't get any more specific
- this refers to the object or the data abstraction that we are writing the method for
- just say this, don't want to refer to the private details
	- not the business for those outside the data abstraction
- remain general at this stage. 
- this method is a mutator on account

# One more thing - if it changes other data abstractions
```java
// MODIFIES: this
public double deposit(double amt, List<Integer> deposits) {
	deposits.add(amt);
}
```
- what happens here if we make a call, what will happen is we'll have a list, and the number 5 will be added to list
- if we make another call, the number 3 will be passed...
- this deposits list persists outside of the scope of this method
- we'll also include this in modifies list
![[Pasted image 20250116210727.png]]

**Technical points in this video:**

- Only use the clauses that are needed.  If you have "nothing" written after one of the clauses, erase it entirely.

# How to write specifications
- this is the signature of the method :O
- ![[Pasted image 20250117102454.png]]
	- public method
		- other classes can call it
	- void return type
		- method runs, complete work, doesn't return anything back
	- name
	- parameter list
		- parameter type is important!
		- name of parameter is arbitrary choice
	- now lets remember parts of our specification
REQUIRES
- it takes an integer
- must be an integer
- no real requirements other than that it is an integer
- this method doesn't require anything!
- since the type takes care of the requires since the compiler would complain if it wasn't an integer
- so we don't need it
MODIFIES
- now lets think about our modifies clause
- this method mutate something in this data abstraction or another?
- an integer is a data abstraction!
	- this doesn't modify it though
- but this method DOES change the integer set, it adds a new integer
- recall, in BSL we make a new set
- in Java, we modify
- we write `MODIFIES: this`
EFFECTS
- we know basic behaviour - it inserts a number into the integer set
- we don't want to write the DETAILS
- we just want how the effects of this method will be viewed from the outside world
- `EFFECTS: inserts num if not already in the set. If num is there, does nothing`

![[Pasted image 20250117103131.png]]
- erase requires line

# EDX Questions
![[Pasted image 20250117103236.png]]
![[Pasted image 20250117103318.png]]
![[Pasted image 20250117103342.png]]
![[Pasted image 20250117103351.png]]

![[Pasted image 20250117103924.png]]

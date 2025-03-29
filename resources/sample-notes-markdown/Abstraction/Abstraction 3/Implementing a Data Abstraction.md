We're finally ready for the final step of designing a data abstraction: Implementing.

**Technical points in this video:**

- Implementing involves determining _how_ the data abstraction provides its external (public) operations
- To implement a data abstraction a developer needs to determine the right data structure for the **internal representation of the data**.  
- Typically internal data that is a collection will be held in some kind of **collection object** (or multiple collections). All collections let you add and remove elements, lets you check the size of the collection, and let you check whether an element is in the collection (contains).  
- Different implementations of collections have different underlying properties.  For instance, **Sets** do not allow duplicate elements but elements are not stored in insertion order, while **Lists** preserve insertion order but do allow duplicates. Which collection to choose depends on the requirements of the data abstraction.

# Implementing
![[Pasted image 20250121122241.png]]
- now we've
	- written specification
	- considered usage scenarios
	- written test cases that exercise our specification
	- written tests from those test cases
	- watched the tests fail (good)
- now we can implement our code until tests pass!
- now we have to figure out the internal representation of our data abstraction
	- what do we insert?
	- what do we check contains?
	- whats the size?
- think about options to internally represent our data

![[Pasted image 20250121122433.png]]
- what are the fields?
- something called a Collection in java
- a collection has several operations
	- store data
	- add contains remove size
	- related to what we need to implement
- there are lists 
- there are sets
![[Pasted image 20250121122516.png]]
- lists have
	- arraylist
	- linkedlist
- sets have
	- hashset
	- tree set
![[Pasted image 20250121122533.png]]
- for now we use arraylist!
In this video, we're going to take another look at our IntegerSet from the Data Abstraction module, and make some updates. To follow along, you can download the completed program from the end of Data Abstraction [here.](https://github.com/UBCx-Software-Construction/TPD-lecture-starters)

**Technical points in this video:**

- Sometimes after you have implemented a class, you might realise you want another version of that same abstraction. A good approach is to extract an interface from that class, and then implement a second class that implements that same interface. 
- IntelliJ will help extract an interface with the **Refactor->Extract->Interface** option.
- A HashSet is quicker for searching for items in its collection than an ArrayList, so if you need speedy searching over large amounts of data, a HashSet is a better choice.
- **@Override** annotations are helpful because they will complain if you have not typed in a supertype's method signature correctly. They are not needed for compilation/running the code, however.

# IntegerSet
- why is IntegerSet test running slow?
	- maybe the way we opted to store our data abstraction isn't the best, and we chose something that adds data slowly!
- slow data structure
- arraylist 
	- fast for inserting things, it's REALLY slow at finding a specific element, worst case has to look through the entire list
	- so in our test loop everytime we have to search, for 50k, takes a while


![[Pasted image 20250202163104.png]]
- sets are a LOT faster than searching than lists are
- we don't want to change our current integerset, we want to be able to have two different versions. One that is slower but easier to move through sequentially, then one that is good for having lots of elements

# How can we abstract AWAY duplication
- we are going to extract an interface

![[Pasted image 20250202164952.png]]
- rename the original class like this
	- also rename tests, want tests to test the implementations
- then, rightclick, ReFactor, extract interface!
	- extract all of the methods that are in the original implementation to be specified in the interface
- we always want to declare the name of a variable as the MOST general abstraction
	- then we instantiate the implementation we want to use
	- this is actually a design principle called **dependency inversion**
![[Pasted image 20250202165237.png]]
- now we want our high volume integer set implementation
![[Pasted image 20250202165257.png]]
- now decide what our internal representation should be
- ![[Pasted image 20250202165330.png]]
- make it a collection
	- because so, it comes with Add, remove, contains, and size methods
- because we are sneakily using hashset, the checking behaviour comes for free, it will not add duplicates since it is a set
![[Pasted image 20250202165427.png]]
 

# The @Override annotation 
- overide indicates its a method that is overriding the method that appears in the supertype
- annotations come in handy, if you ever accidentally change the signature of the method
	- lets you know not overriding properly

![[Pasted image 20250202165847.png]]





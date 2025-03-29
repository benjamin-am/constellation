In this video, we introduce the method we use for designing Data Abstractions, and then identify the information we will be representing in our Data Abstraction.

This method is analogous to the design methods you learned in the How to Code courses. You will notice many things that are similar to what you learned in How to Code, and also some that are different.

As you work through the module, you should pay attention to these differences and similarities. Drawing connections to what you already know will not only help you absorb the material in this module, but also help you see how you could apply elements of the design method from How to Code to any language. As you work through the module, there will be some questions to complete to help you make these connections. 

**Technical points in this video:**

- There are four phases in our design approach (often applied in a circular way): **specification** of public interface, **usage** scenarios, **test** specification, and finally **implementation**. 
- **Specification** means determining exactly what the public operations should be, and what they should expect/assume when called (REQUIRES), what they change (MODIFIES) and what they produce (EFFECTS).
- **Usage scenarios** means looking at all the ways that your abstraction will be used -- this will perhaps motivate new operations, which will then need to be specified
- **Test specification** means writing a thorough and rigorous test suite for every operation prior to implementation
- **Implementation** involves deciding on an internal representation of the data in the abstraction, and then implementing the public and supporting private methods to make it work.  The tests should all pass when the implementation is done.

# Four Phase Design Process
1. Specify
	- what will the public view be for our abstraction
	- what is visible
	- which methods are operations does our abstraction provide
2. Use our data abstraction
	1. Think about all the situations which other classes are using our data abstraction
	2. think aobut those so we have correct specification
3. Test
	1. look at each methods we have designed, and imagine all the scenarios in which we use them
	2. and then we test those scenarios
	3. test before implementing!
4. implement the data abstraction
![[Pasted image 20250117101541.png]]

# Example of Data Abstraction
- integer set
	- what is it?
	- a set of integers
	- any number of integers
	- no duplicates
	- no decimal
- lets imagine a data abstraction of an integer set, we design it
Draws circle intensively lol
- what would we want to provide to public
	- insert
	- remove
- what would be private?

We have to figure out exactly what those methods will do
how we specify each operation in our data abstraction, big three questions
1. preconditions for correctness
	1. what set up do we need before method can run properly
	2. REQUIRES
2. what does it change?
	1. what does it change in our data abstraction
	2. MODIFIES
4. what does the method do?
	1. EFFECTS
![[Pasted image 20250117102128.png]]

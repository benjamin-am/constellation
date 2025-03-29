You can download the Java project with accompanies this video [here](https://github.students.cs.ubc.ca/CPSC210/TPD-Lecture-Starters). The specific project which accompanies this video is **IntegerSetInterface3**.

Remember when we copy and pasted high volume and lowvolume integer set classes

![[Pasted image 20250202225124.png]]
- a ton of shitty duplication
- instead, just make an abstract integersettest
![[Pasted image 20250202225210.png]]
- use abstraction to avoid duplication
- it's always our solution when we spot duplication
- don't want to instantiate that class
- can't instantiate a generic integer set
	- use an abstract class to capture the duplication at the level of abstraction of the IntegerSet
![[Pasted image 20250202225319.png]]
- the only difference is TestInsertHighVolumneTest() 
	- how to achieve variation
		- either make it an abstract method (implementation lives in subclass)
			- wouldn't live in abstract class but would live in both subclasses
		- or leave it in the abstract superclass
		- and then override it in the high volume integer set chest class
	- we chose override option, arbitrary, but it's because the lowerVolumne insert is less special and should stay in the more generic class - it is more likely to be similar to other subclasses
		- probably one we'd use as a test if we made new implementations of an integerset
![[Pasted image 20250202225604.png]]
![[Pasted image 20250202225627.png]]
![[Pasted image 20250202225638.png]]
- we should NOT have had the setup in the abstract
	- we want them to have their own implemtations
- should erase setup OR make it abstract

## DO NOT DECLARE A FIELD AGAIN IN A SUBCLASS
- leads to horror and confusion!!!
- makes a second field, there will be null pointers
- ![[Pasted image 20250202225958.png]]
![[Pasted image 20250202230025.png]]

- DELETE
![[Pasted image 20250202230143.png]]

![[Pasted image 20250202230217.png]]



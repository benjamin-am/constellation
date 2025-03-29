**Technical points in this video:**

- We design tests that test a specific scenario -- these are called **test cases**
- A **test suite** is the collection of test cases that, together, thoroughly (though not 100% exhaustively -- that's impossible for all but the most trivial cases) test the data abstraction.
- Create a test case for everything happening in the effects clause, and create a test case for _each combination_ of inputs and outputs.  
- Create tests such that each branch of your method is followed (this is loosely related to **branch coverage**, though at this stage we are just checking branches generally, since we do not yet have an implementation against which to design a test case with proper branch coverage) 
- Write test cases to test the edges of ranges (**boundary checking**) to check for typos in range checks or conditional statements.
- Test case should be named after the method they are testing, and also after the scenario they are testing to help you keep track of what you have tested. (Test`<method name><scenario description>`)
- Test cases always specify the inputs, and the expected outcome

# Lets think about the effects clause
![[Pasted image 20250119175406.png]]
- how does this method operate in the perspective of the outside world
Start
- is # in set
	- true: 
		- do nothing
	- false:
		- insert number into the set
We get the basic flow of the method down
- we need to test both pathways of the method
- the true and the false, so we know they are both working

# First Test!
- Test insert notAlreadyThere
- this test will insert a number that is not already in the set
- then we decide the outcome of what the test will be
- outcome: Number appears in the set

# Now we want to test the other pathway
- number is already in the set!
- TestInsert alreadyThere
	- tests insert number already in set
- outcome: Number appears in the set only ONCE
	- notion that number appears only one time
![[Pasted image 20250119175845.png]]

![[Pasted image 20250119175856.png]]
- what if we had a more complicated scenario for inputs?
- testing one of each of the scenarios isn't enough

to rigorously test programs with boundaries such as inequalities, you would WANT to use test cases at the boundaries themselves, in case you fuck up < and <=
- we end up with 5 tests

![[Pasted image 20250119180157.png]]
- now that we know that these are all the test cases we'd like to see, how would they become test cases

![[Pasted image 20250119180413.png]]
- remember, be specific about boundary test cases
![[Pasted image 20250119180443.png]]
then we continue for the 0 case, then we continue for the positive boundaries!

# EDX Questions
```java
public class HouseHunter {  
      
    //MODIFIES: this  
    //EFFECTS:  adds the house to the list of houses to visit    
    public void addInterestingHouse(House h){  
    }  
  
    //MODIFIES: this  
    //EFFECTS:  returns the most recently added house    //          and takes it off the list of houses to visit;  
    //          returns null if there are no more houses to visit    
    public House getNextHouseToVisit(){  
        return new House();  
    }  
  
}
```
![[Pasted image 20250119180630.png]]
![[Pasted image 20250119180800.png]]

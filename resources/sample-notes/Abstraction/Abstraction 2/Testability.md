**Technical points in this video:**

- JUnit is a mechanism for black box testing: testing abstractions from the _outside_
- Sometimes it is necessary to provide additional methods that are specifically designed to facilitate testing. Otherwise, we may not be able to check enough details of the outcome of our tests to be confident we have tested our data abstraction.
- These methods need a specification just like all others -- but they will likely _not_ need a modifies clause, because they are inspection methods, not mutators.

![[Pasted image 20250119204659.png]]
- JUnit is basically an outside caller into the abstraction
- only sees the public interface of the abstraction
	- no private

# This is black box testing
- from JUnit's perspective, our abstraction is a black box
- what we do is provide public methods to JUnits
- what methods help us with our testing?
- contains method
	- check if number is in method already
- size method
	- test if it is in set once
- these methods are just for sake of testability!
- how would we specify them

# Specification of new methods
- contains
	- returns a boolean so we can use contains in our assert true, false,...
- size
	- returns Integer
- neither of them require or modify anything!
- effects for contains
	- returns true if number is in set
- effects for size
	- returns size of the set

![[Pasted image 20250119205219.png]]
# EDX Questions
You want to write some tests for a class that represents a rock show. It has the following fields:
Bands is a list of the bands playing, venue is the name of the venue, and there are fields for the maximum capacity of the venue, and the current size of the audience. 

Imagine the class has various methods that one might need to manage a rock show.

```java
public class RockShow {  
    private ArrayList<String> bands;  
    private String venue;  
    private int maxAudienceSize;  
    private int audienceSize;  
}
```
  
Explanation

We need methods that let us access the fields in the RockShow class to make it testable.
![[Pasted image 20250119205407.png]]
# # **HouseHunter Testability**

Recall the HouseHunter class's methods:
```java
//MODIFIES: this  
//EFFECTS:  adds the house to the list of houses to visit  
public void addInterestingHouse(House h){ }  
  
//EFFECTS:  returns the most recently added house  
//          and takes it off the list of houses to visit;  
//          returns null if there are no more houses to visit  
public House getNextHouseToVisit(){ return new House(); }
```
![[Pasted image 20250119205513.png]]

What method or methods would you need to add (if any) given this test case:

      `Test case: Get the only house to visit Outcome:   The house should be the expected house, there should be no more houses to visit`
    

(pick the smallest number of methods! You don't want to bloat your abstraction unnecessarily!)
![[Pasted image 20250119205601.png]]

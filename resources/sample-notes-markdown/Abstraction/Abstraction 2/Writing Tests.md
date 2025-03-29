**Technical points in this video:**

- For each test case, we write a method in our Test class, and annotate it with **@Test.**
- We write the set up code for each test, and put it in the set up method, and annotate that method with @BeforeEach 
- Then we write comments to indicate the 3 parts of the test: (1) check that the set up is correct, (2) call the method to test, (3) check that the outcomes were expected. Write these comments as specifically as possible for what you are testing.
- **Checking the setup** involves checking that the work expected by the method has not already been done. Sometimes this can be intuited, but typos creep into code, and especially if more than one person is collaborating, behaviour can suddenly pop up anywhere.  Best to check that the set up is clean.
- **Calling the method to test** is straightforward. Sometimes this is integrated into the next stage, if you are directly checking the output of the method.  Other people like to save the output of a method, and then check it one a separate line of code. That might make it easier for troubleshooting later.
- **Checking the expected outcome** involves looking at the outputs of the method and writing conditions or assertions that will fail if the outcome is not correct.
- Remember: A test will pass unless you make it fail, so having a passing test isn't a great accomplishment.  You should have a _correctly_ passing test!

You can follow along in the **IntegerSetTestStarter** project from the GitHub repository [here](https://github.students.cs.ubc.ca/CPSC210/DataAbstractionLectureStarters).

Note that there are some important differences between jUnit 4 (as seen in the video) and jUnit 5 (which we are using in class this term).  There are also differences between IntelliJ and VSCode.  However, you should be able to follow along if you keep the following points in mind:

- the project that you clone from GitHub has already been configured to include the jUnit library
- you will need to use different import statements when working with jUnit 5, specifically:

```
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
```

- test classes and test methods in jUnit 5 do not have to be declared `public` (in other words, you can omit the `public` keyword from class and method declarations)

If you have difficulty following along, don't worry - we'll be demonstrating how to work with jUnit 5 and VSCode during the Abstraction 2 Lecture Lab in class.


# Writing Tests
![[Pasted image 20250119211649.png]]
Lets write todo test comments!
![[Pasted image 20250119211823.png]]
![[Pasted image 20250119211851.png]]
- have to add Junit to import list (why it's red)
three things to do in first test
- check is not already in set
- insert number into set
- check number is in set once
![[Pasted image 20250119211953.png]]

testInsertAlreadyThere()
- use same test as one, but then try to insert again
- check that the number is in set once, make sure it wasn't inserted a second time!
## Redundancy isn't bad
![[Pasted image 20250119212120.png]]
- thats why we do insert again!

# Implementation of tests
- need to set the tests up
- we should set up a test field
- then initialise that field in a method that we tag with the before annotation
```java
IntegerSet testSet;

@Before
public void setup() {
	testSet = new IntegerSet();
}
```
- now we have our initialized integerSet test
- now lets fill in the details

# Using assert to check something
`assertEquals(testSet.size(), 0)`
`assertFalse(testSet.contains(3))`
- check the initial if the set meets conditions
- then test if insert works
- then assert that the set has changed!
![[Pasted image 20250119212634.png]]

# If JUnit gets to end of a test method without failing, it counts as a pass!
- so if you have a blank test method, it will pass lol

![[Pasted image 20250119212739.png]]
![[Pasted image 20250119212753.png]]
- assertion error
![[Pasted image 20250119212809.png]]
- we click through and see that we failed in check that number is in the set once
- that means we made it all the way through setup, assertEquals, and assertFalse!
![[Pasted image 20250119212851.png]]
- these ran fine

![[Pasted image 20250119212902.png]]
- since insert does nothing, we fail!

## Test 2
![[Pasted image 20250119213010.png]]
- fails at same point
- we copy and pasted code wtf

# Reduce duplication
- get rid of copy pasting and typo errors
- so lets refactor and introduce helper methods
- then we know how the helper method works

![[Pasted image 20250119213327.png]]
- made a helper
![[Pasted image 20250119213405.png]]
- tests fail with helper!

# Importance of @Before
![[Pasted image 20250119213429.png]]
- does good things, runs in order

# Remove //TODO when done and comments
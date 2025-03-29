**Technical points in this video:**

- The third stage of a test is checking that the executed method produced the expected results.
- Conditions can be used to check values or states of an object to check that it has been modified correctly -- and if it has not, the **Fail** keyword can force the test to fail.
- **AssertTrue, AssertFalse** and **AssertEquals** can also be used to check the state of objects and values. If any of these fail, the test fails.

# How does JUnit decide pass/fail test?
```java
if (t.isFacingLeft()) {

} else {  
    fail("truck facing the wrong way");  
}  
  
assertTrue(t.isFacingLeft());
```
- recall we have t due to @Before
- isFacingLeft() is a method we'd have to write before our test
- fail makes our test fail
- instead of any of the code above, we can use Assert! We don't need above at all!

# Above code is bad, JUNIT IS GOAT

# Assert statements
- Assert Equals, True, False!
```java
assertTrue(t.isFacingLeft());
```
- if assertTrue fails, then execution stops at this line, and JUnit will report a test failure on this line.
- big library of JUnit assertion statements
https://junit.org/junit5/docs/5.0.1/api/org/junit/jupiter/api/Assertions.html
![[Pasted image 20250119203726.png]]


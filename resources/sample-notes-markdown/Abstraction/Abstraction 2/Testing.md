After specifying our data abstraction, and considering use cases, it's time to write a set of tests for it. The next few videos will talk about considering test cases, making your data abstraction testable, and creating a test suite using JUnit. 

**Technical points from this video:**

- **Test driven design** (typically a part of **agile software development**) involves writing tests right after writing your specifications, then implementing your code until the tests all pass.
- Tests are a more comprehensive way of checking the conformance of your implementation to its intended specification.

# Write tests before Implementation!
- we write specification first
- now we write our test cases
- test cases are a great way to actually encode the specification 
- the specification is just comments, so tests encode it
- the tests should capture the meaning and semantics of our specification

# Combo of design methodologies
- agile and TDD

# What we do
- write tests
- run tests
- FAIL
	- since no implementation is done yet lol
	- methods are all stubs
- then we implement abstraction
- until tests pass
![[Pasted image 20250119175155.png]]
- when all tests pass, we've implemented the method


In the next few videos, we introduce you to JUnit, Java's unit testing framework. Here we are using JUnit4. You will also be exposed to JUnit 5, in the debugging video in the next unit. Note that either JUnit4 or JUnit5 can be used in this course, and there are only very slight differences between the two. 

**Technical points in this video:**

- Name test classes "Test" and then the name of the class you are testing
- JUnit looks for the **@Test** annotation to identify methods to call as tests
- Each test is basically structured: **(1) set up**, **(2) call** the method to test, **(3) check** that the expected outcomes occurred.
- Pull duplicated lines of set up declaration code into fields.
- **@Before** (JUnit 4) or **@BeforeEach** (JUnit 5) lets you annotate a set up method that will be run before each test method. The annotated method does not need to be called from within the test methods -- it runs automatically.
- Pull all duplicated lines of set up behaviour into that @Before/@BeforeEach method.


![[Pasted image 20250119192639.png]]
- computer looks for main method
- main method is entry point for class
- JUnit looks for test methods

# JUnit class
![[Pasted image 20250119202327.png]]
- looks mostly like a regular class
- classes usually always has test in them
- say name of abstraction you're testing
- this is just a naming convention, nothing behind the scenes
- test methods correspond to what method they are testing
	- naming convention, can be called anything
- the real power with JUnit is annotations!

# Annotations
- @Test
	- tells JUnit that this method contains testing information
- then inside body of method we write all of our test code, like check-expect
- JUnit will run the test method
	- looks for @Test
- use @Test above the test methods

![[Pasted image 20250119202600.png]]
- builds this list
- these methods are just methods
- can use fields and helper methods

## In Drive test
- make a truck
	- Truck t = new Truck()
- sets up the abstraction we want to test
- t.drive()

## in park test
- make a truck
- then it'll definitely call the truck's park method!

![[Pasted image 20250119202752.png]]
- since these lines are duplicated, we can take a look at how to remove this duplication
- we can say the Truck t = new Truck(); as one field at the top of the class
	- so we don't declare a new truck for each method
- basically find repeated code, then make a field out of it!

# Solving the duplication issue
- pull the duplicated code into it's own method
- `public void setup() {t = new Truck()};`
- now we have the setup() method!
- we can replace the duplicated code with the call to setup
- but now we're just calling setup...
- in JUnit we can use @Before/@BeforeEach!
	- this runs before we run any test!

# @Before
- calls before every single test method (without specifying it)
- lets you setup an environment before a test for the most part
- its a method that will run!
- we call it setup in class, but all that matters is @Before
![[Pasted image 20250119203147.png]]
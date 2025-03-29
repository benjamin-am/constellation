This is the final debugging video in the course. Once again we'll take a look at our HairSalon, but now we've added tests! We'll explore how tests can help us find bugs, and how we can identify bugs within our tests. If you haven't downloaded the lecture starters for this module from GitHub yet, you can [download the starter HairSalon4Starter here.](https://github.students.cs.ubc.ca/CPSC210/DataAbstractionLectureStarters) 

**Technical points in this video:**

- Breakpoints can be set in tests, just like in "regular" code. Sometimes it is helpful to pull calls to methods into their own line of code, rather than placing them inside assert statements, so that you can more easily isolate them for breakpoints.
- To see where a test is failing, click the link that takes you to the failing line of code.
- A problem with the branching in complicated conditional statements often causes bugs in code.
- If a test is failing when you believe it should be passing (or the reverse), you may be asserting the wrong thing. Typos often creep into assert statements.
- Remember to properly structure your test so that it is setup - call method - check outputs.  If you mix these up, the logic of the test may not be well formed, and the test may pass or fail when it should not.
![[Pasted image 20250119214518.png]]
- set a break point at the point the test is failing, given by java output

![[Pasted image 20250119215244.png]]
- setup

![[Pasted image 20250119215253.png]]
- what our test does
![[Pasted image 20250119215343.png]]
- failing that elisa is no longer booked
	- possible code is wrong
	- possible test is wrong
![[Pasted image 20250119215410.png]]
- we see that booking 15 is our standin customer, so why is it failing?
- go to method
![[Pasted image 20250119215446.png]]
- stepover, we go to the next branch!
- and again...
- but we return true! WHAT THE FUCK?!
- method is broken!

![[Pasted image 20250119215518.png]]
- our flow chart shows this method is broken!
![[Pasted image 20250119215548.png]]
-  fix method
- test passes
	- it helped us find a bug we didn't find before :)


# Running code is great way to see presence of behaviour
- not good to exercise all the different situations under which that behaviour is run
- why we thoroughly test our code

# Another failing test
![[Pasted image 20250119215722.png]]
- wait... why would we assertFalse here?
- our test is doing the wrong thing! Should assertTrue
- now our test passes!

# Now lets look at a long, passing test
- it should fail :O
![[Pasted image 20250119215825.png]]
- this test is written horribly
- what is it doing?
- making a ton of customers
- put breakpoint at end to see all the steps in the test
![[Pasted image 20250119220000.png]]
- wtf this is all wrong
- all in wrong spots
- why is test passing

## We've mixed the three stages
![[Pasted image 20250119220040.png]]
- mixed setting up, invoking the tested behavior, and checking the results
- what we want to test is set up the entire test, then invoke the entire test, then verify the behaviour
- this test should be making a lot of different bookings all at once
- then check all at once that they are verified
![[Pasted image 20250119220203.png]]
- rework
![[Pasted image 20250119220214.png]]
- now it fails
- in makeNewBooking add is broken
![[Pasted image 20250119220309.png]]
- should've been set
- ![[Pasted image 20250119220324.png]]
Now that we fixed that method, it works!

# All tests pass!
- but we're not done
- now we want to inject bugs into code, to see if tests fail lol

# INJECT BUGS!
- change random stuff
- then check tests!
- if all tests pass BAD - you need more tests
- systematically break all your code, and make sure tests break
- you want your tests to find bugs

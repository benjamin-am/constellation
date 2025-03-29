**Technical points in this video:**

- Thinking through usage scenarios involves considering all the situations in which another class would make use of the data abstraction we are creating.  We want to think through not just the operations that are available, but the order in which they will be called.  This, in turn, helps us make sure we have all the methods we need.

- To sketch out usage scenarios, create a main function (IntelliJ shortcut: psvm) either in a new class, or an existing class (typically we make a new class for this purpose).
- Into that main function, place calls to the data abstraction in all the arrangements and combinations you can think might be valid.  Think through every situation in which the data abstraction will likely be used, and make a little usage scenario for that combination. These scenarios do not have to be as exhaustive as the test scenarios we will do in the next part.  Instead they should capture the spirit of the usage of the data abstraction.
- In doing this you might find you want to add new functionality to the data abstraction -- go back, add it, and remember to fully specify it while doing so!

Follow along in the **IntegerSetStarter** project from the GitHub repository. Click [here](https://github.students.cs.ubc.ca/CPSC210/DataAbstractionLectureStarters) to download the project.

# Go through usage scenarios
- how it will be called from outside world

## Everytime we have UI stuff, make a UI package
- put everything for use in PSVM

# Consider how the Data Abstraction will be used
- think about how users will use the insert method
- think about how users will use remove method
- things going in
- things getting removed

![[Pasted image 20250119173819.png]]
- because we have stub implementations for IntegerSet, we can run the code lol
	- but nothing happens

![[Pasted image 20250119173923.png]]
![[Pasted image 20250119174005.png]]



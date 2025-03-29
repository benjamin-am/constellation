If you've been following along up to now, your own version of `IntegerSet` should be the same as, if not very similar to the project you can download by clicking on this [link](https://github.students.cs.ubc.ca/CPSC210/DataAbstractionLectureStarters) from GitHub. The **IntegerSet** project accompanies this video.

**Technical points in this video:**

- To implement the data abstraction, implement each of the methods, taking as much advantage of the operations provided by the internal representation(s) as possible.
- Remember to make the internal representation of the data _private_ because we don't want open access to the internal data.
- Implement the data abstraction until all the tests pass.

![[Pasted image 20250121122753.png]]
- we are using ArrayList
- she calls it internalArray
	- even though it is a set lol
	- we know its actually an array
	- the arraylist has a lot of the same methods we are providing in our integerset, so we want to be clear!

## Constructor
```java
public IntegerSet() {
	internalArray = new ArrayList<Integer>();
}
```
![[Pasted image 20250121122944.png]]

## insert
- we can tell from effects that this is a conditional statement, so we will need an if statement for our implementation
```java
public void insert(Integer num) {
	if(!internalArray.contains) ...
}
```
![[Pasted image 20250121123035.png]]
- we aren't using OUR contains method, we are using the ArrayList one
- this isn't cheating, using the right data abstraction to implement your own is good programming

```java
public void insert(Integer num) {
	if(!internalArray.contains(num)) {
		internalArray.add(num)
	}
}
```
![[Pasted image 20250121123158.png]]
- tests still failing???
- WE HAVEN'T IMPLEMENTED SIZE :O

## Size
```java
public int size() {
	return internalArray.size();
}
```
- remember everytime you make a change, run your tests

## contains
```java
public boolean contains (Integer num) {
	return internalArray.contains(num);
}
```
- finally all insert tests are passing!
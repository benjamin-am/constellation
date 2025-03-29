**Technical points in this video:**

- Subclasses can introduce their own methods to augment (or extend!) their behaviour
- Behaviour specified in the subclass is not available to variables declared to be of the superclass type.
- Java looks in the declared (apparent) type of an object to see what methods are available to that object (it doesn't matter how the object is instantiated). IntelliJ will show a drop-down list of available methods.

You can download the accompanying Java project by clicking [here](https://github.com/UBCx-Software-Construction/TPD-lecture-starters) to download from GitHub. Open the **FlyerStarter** project to follow along with this video.

# We can also extend the behaviour!
- add new behaviour
- also add fields and things
- ![[Pasted image 20250202192328.png]]
	- additional method inside private plane not in airplane
- so if we declare something to be a PrivatePlane (and instanstiate), then we can call bringWarmTowels method!

![[Pasted image 20250202192411.png]]
- if you have declared something to be an airplane, it won't have access to this new method

`Airplane luxPlane = new PrivatePlane();`
- we CANNOT say luxPlane.bringWarmTowels
- because it looks inside the declared type, and look UP the hierarchy, and will NOT see it
![[Pasted image 20250202192517.png]]
- so we can extend the class by adding things, but we have to actually declare our objects to be of this type if we want access to those methods

# Inside the editor
- doesn't care that its empty. Just steals Airplane implentation
![[Pasted image 20250202192631.png]]
- only currently has airplane methods
![[Pasted image 20250202192647.png]]
![[Pasted image 20250202192708.png]]
- now we can see bringWarmTowels();
![[Pasted image 20250202192731.png]]
- everything is happy!

`public void luxuryTakeoff(PrivatePlane p) {}`
- what can you do?
	- everything inside an airplane
	- and everything in a private plane
![[Pasted image 20250202192855.png]]
- can you pass it a planie?
	- no - it's just an airplane!
![[Pasted image 20250202192928.png]]
- REMINDER you cannot substitute a superclass for a subclass, we can only do the reverse
![[Pasted image 20250202192950.png]]
![[Pasted image 20250202193022.png]]
- planie can do all the airplane stuff, but it cannot bring warm towels
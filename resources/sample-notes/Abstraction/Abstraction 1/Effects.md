- The **EFFECTS** clause indicates the purpose of the method -- describing the work that the method does.  
- For public methods, this clause only describes publicly visible effects -- implementation details are not described.
- Effects clauses for private methods have more flexibility in their level of detail, but typically also only indicate "publicly" visible effects -- however these might mention internal details of the class implementation more freely than the specification for public methods (because a _developer_ of the class is reading these specifications, not a _user_ of a class).

# What
- it helps you explain what a method does to the outside world

![[Pasted image 20250116182944.png]]
- this looks like we're talking about implementation detail here
	- we do talk about work accomplished
	- but we only talk about publicly visible work
	- not how
	- but that this is returned
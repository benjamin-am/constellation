You've probably become used to seeing the `public` and `private` keywords before methods and fields. But what do they mean? In this video we take a detailed look at the this idea of visibility. Be sure to have your `SimpleDrawingPlayer` open in IntelliJ to follow along. 

**Technical points in this video:**

- In order to support the principle of **information hiding** -- one of the keys to abstraction in design, Java provides different levels of **visibility** for fields and methods.
- **Public** fields and methods are visible to all other classes -- these constitute the visible interface of an abstraction -- the way the class is seen and used by the outside.  They are the visible tip of the iceberg.  
- **Private** fields and methods are only available within the class itself -- these constitute the invisible implementation of the abstraction. The private implementation is the rest of the iceberg - the parts that aren't visible from the outside. 
- Deciding what should be public or private is a design decision. Typically anything internal to the implementation is private, and accessors and users of that implementation is available publicly.

# Visibility
- all we see from the outside is the visible interface
- imagine an iceberg
	- above water is visible interface
	- below is hidden (inside the abstraction)
		- this is called the invisible implementation
![[Pasted image 20250116180553.png]]
- visible implementation
	- public
- invisible implementation
	- private
- there is a third one, but not looking at it yet

interface with a small i
big I interface is a keyword in Java, we'll get to later
![[Pasted image 20250116180657.png]]
- public interface with a single abstraction

# Example - Pizza Place abstraction
- within it has
- public abstraction
	- order
		- private implementation to make the pizza
		- all the things are done
	- then the pizza is returned back to you
	- you don't care about the implementation as long as you're provided with a good pizza
![[Pasted image 20250116180839.png]]

# Shape example
![[Pasted image 20250116180852.png]]
- unlocked indicates public, locked indicates private
- constructors are usually ALWAYS public. Because you want to construct the object outside the class
![[Pasted image 20250116180938.png]]
![[Pasted image 20250116180948.png]]
- getters and setters are also public

After getters and setters, there is more public methods

Anytime you see the dot notation, you know that one class is using the visible interface of another class
![[Pasted image 20250116181046.png]]
- midisynth.play()
- using the public method from midiSynth

![[Pasted image 20250116181125.png]]
- a private class that we hide

# When understanding a class
- first look at public
	- this tells us how the abstraction is used and seen by outside world
- but if we want under the hood, we look for the stuff the public methods themselves use, and often, they are internal private methods

# Getters and Setters
- public methods that give access to private data
- ![[Pasted image 20250116181254.png]]
- we want to hide the private data because they're really open to change
- hide them beneath public interface
- doesn't matter from outside how we implement what is going on

![[Pasted image 20250116181344.png]]
- boolean usually called is not get
- how we get the private data

![[Pasted image 20250116181427.png]]
- set the private data

# Why do we need it?
- propagation of changes
	- debugging
	- change decisions
- anytime one class uses another class, if a method changes you'll have to change the caller as well
- want to limit the points at which other clients are reliant on the data abstraction
- ![[Pasted image 20250116181542.png]]
- what's floating publicly, changes very little
- you design so public stays relatively stable

# EDX Questions
The public interface of a class contains information about what actions or information can be used by others (it's not necessarily that the class is global, which would mean accessible from anywhere). However, that doesn't main the entirety of a class needs to be public. A class can still have a public interface, but hide its private implementation. Therefore, not all methods and fields should be public.

![[Pasted image 20250116181705.png]]
Your public interface will not change much, but your private implementations may change a lot as you refactor your system. If clients of your code (other classes, other developers, or even future you) relied on implementations of your class, they could find themselves constantly having to rewrite their own code when yours changes as well. Information security is a different problem from information hiding, which deals with data. Distictions between public and private methods probably won't help you understand the class more than just looking at it would.


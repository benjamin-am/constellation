https://learning.edge.edx.org/course/course-v1:UBC+CPSC210+all/block-v1:UBC+CPSC210+all+type@sequential+block@2c6c8b9d8467407280533c94f1dd2029/block-v1:UBC+CPSC210+all+type@vertical+block@a711820e15164786ac5b137af8127575
# Requires
- speicifies which values of the operations parameters the operation is defined
- specifies any constraints on the data object 
- You may also consider the lack of a REQUIRES clause to mean there are no constraints on the use of an operation.
# Modifies
- states what input values are modified by an operation
- does not describe how values are modified; part of the role of the effects clause
- if change to input value persists after the operation, we say that the operation has a side effect
- A constructor ALWAYS modifies a data object through sheer act of creating and initializing it. It is a matter of convention that we do not list this as being modified by a constructor
- For convenience, we will consider an absent MODIFIES clause as a specification that the operation does not modify any values (except in the case of a constructor where we assume that `this` is modified).
# Effects
- specify what outputs are produced by operation and how any input values modified are altered

# Specification for animal data abstraction
We can now provide a more complete specification for the `Animal` data abstraction for the Aquarium feeding system. As described earlier, you can assume missing REQUIRES and MODIFIES clauses specify that there are no constraints on the running the operations or that no modifications to input values occur.
```java
// An animal at the aquarium.
class Animal {

   // Construct an animal.
   // Requires: acceptableFoodToEat is not an empty list
   // Effects: this updated with acceptableFoodToEat
   Animal(List<Food> acceptableFoodToEat) {...}
   
   // What can this animal eat?
   // Effects: returns a non-empty list of food
   List<Food> getAcceptableFoodToEat() {...}

   // When should the animal eat next?
   // Effects: returns a date (including time) in the future
   Date nextTimeToFeed() {...}

   // Remember what the animal last ate
   // Requires: foodEaten is not an empty list
   // Modifies: this
   // Effects: this updated with foodEaten
   void recordLastFeeding(List<FeedingRecord> foodEaten) {...}
}
```
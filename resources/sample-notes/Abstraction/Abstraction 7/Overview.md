This [slide deck](https://edge.edx.org/asset-v1:UBC+CPSC210+all+type@asset+block/Poly-Type-Dispatch.pdf) contains a summary of important concepts covered in this module.

Abstract classes are an abstraction for housing generic behaviour and data.

Classes can extend abstract classes.  

If a class extends an abstract class it inherits all the regular methods from it, 

**but must implement all the abstract methods.** 

Only regular classes can be instantiated -- that means that **abstract classes do not have to implement all methods** in an interface they implement, or abstract class they extend. Regular classes will need to provide an implementation to anything undefined.

Over**LOADING** means having two methods with the same name, but with _different parameter lists_.  These are considered two totally different methods by Java. If you have:

**public void printSomething(String something)**

java sees: **printSomething_String**

**public void printSomething(int something)**

java sees: **printSomething_int**

Two totally differently named methods!

Note: Return type doesn’t get taken into account in naming, Java will complain if you only change the return type.
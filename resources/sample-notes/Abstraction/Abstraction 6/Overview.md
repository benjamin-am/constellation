Classes can **EXTEND** other classes -- If class A extends class B, it gets (inherits) all the behaviour of class B, and can also add to it. 

Classes can **OVERRIDE** behaviour in their superclasses, by re-defining the method with using the same name and signature.

As with interfaces, the methods that can be called is determined by the apparent(declared) type, and the method implementation used is provided by the actual(instantiated) type. If there is no implementation in the instantiated type, then Java will look up the class hierarchy for a definition.

So for:

C c = new D(); //can only call methods in C, and implementations come from D or a supertype of D.

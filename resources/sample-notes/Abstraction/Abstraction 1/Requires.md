**Technical points in this video:**

- a **REQUIRES** specification of a method indicates the _preconditions_ of running that method. 
- typically we do not include trivial preconditions (such as the parameter must be non-null), but instead focus on conditions of correct running of the method. 
- If a method can be called regardless of the state of the program, then no REQUIRES clause is needed.

# Give hints to caller of method to say there is a precondition that has to be satisfied

# When?
![[Pasted image 20250116182410.png]]
- we obviously don't want amt to be negative, or else it TAKES money from amount
- so we want to tell caller that this amount should never be less than 0
- // Requires: amt >= 0
- this way the caller knows, if it sends in an amount that doesn't apply to specification, then anything can happen
- no guarantees are made

![[Pasted image 20250116182512.png]]
- can't divide by 0
- // REQUIRES: y != 0

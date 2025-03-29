When we talk about testing in Software Construction, we often use the terms "Black Box" and "White Box" to refer to two different types of testing. 

Briefly, Black Box Testing is a way of testing software without knowing any of the internal structure or implementation details of the system being tested. In this case, we are interested in testing the functionality of the software.

On the other hand, White Box Testing is a way of testing software that actually tests the internal structure and implementation details of the system. In this case, we are no longer interested in testing the functionality of the software -- rather, we want to test the actual details of implementation. There are other types of testing, but in this course we will mainly focus on Black Box testing to support our test-driven development process (i.e. testing before implementation).

In the IntegerSet example seen in the previous videos, we don't have any implementation details yet. Any tests we write at this point would be Black Box tests.

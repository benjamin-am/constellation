```java
Consider the following four tests:

@Test  
public void testOne() {  
    assertFalse(true);  
    assertTrue(true);  
}  
  
@Test  
public void testTwo() {  
    assertFalse(false);  
    assertTrue(true);  
}  
  
@Test  
public void testThree() {  
    if (!("two wrongs" == "right")) {  
        fail();  
    }  
}  
  
@Test  
public void testFour() {  
    assertEquals(true == false, 5 == 6);  
}
```
![[Pasted image 20250119204348.png]]Consider the following three tests. You can assume StuffToTest is a class that has three int fields: n1, n2 and n3. 
```java
@Test  
public void aTest() {  
    StuffToTest stt;  
    stt = new StuffToTest();  
    stt.setN1(5);  
    stt.setN2(7);  
    stt.setN3(5);  
    assertFalse(stt.getN1() == stt.getN2());  
    assertFalse(stt.getN2() == stt.getN3());  
    assertTrue(stt.getN1() == stt.getN3());  
}  
  
@Test  
public void anotherTest() {  
    StuffToTest stt;  
    stt = new StuffToTest();  
    stt.setN1(5);  
    stt.setN2(6);  
    stt.setN3(7);  
    assertFalse(stt.getN1() == stt.getN2());  
    assertFalse(stt.getN2() == stt.getN3());  
    assertFalse(stt.getN1() == stt.getN3());  
}  
  
@Test  
public void oneMoreTest() {  
    StuffToTest stt;  
    stt = new StuffToTest();  
    stt.setN1(5);  
    stt.setN2(5);  
    stt.setN3(5);  
    assertTrue(stt.getN1() == stt.getN2());  
    assertTrue(stt.getN2() == stt.getN3());  
    assertTrue(stt.getN1() == stt.getN3());  
}

```
![[Pasted image 20250119204408.png]]
We can eliminate the first line of each test by creating a field at the top of the class. There are also several lines of code that could be collected into a setup method.


# Suppose you've decided to add a field at the top of your class: `StuffToTest stt;`, and now you want to make a setup method tagged with `@BeforeEach`.

Which lines from `aTest` should be moved into the setup method?
![[Pasted image 20250119204428.png]]

![[Pasted image 20250119204610.png]]
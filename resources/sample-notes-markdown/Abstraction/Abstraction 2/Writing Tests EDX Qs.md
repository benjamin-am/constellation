The RockShow class from the previous question has a method called admit one as shown below: 

// MODIFIES: This  
// EFFECTS: if the audienceSize is less than the maxAudienceSize, increment  
//          the audienceSize by one and return true. Otherwise return false.  
public boolean admitOne() {  
    if (audienceSize <= maxAudienceSize) {  
        audienceSize++;  
        return true;  
    } else {  
        return false;  
    }  
}

You want to write a set of tests for this method. You've already set up a test class and completed the setup method as follows: 

public class RockShowTest {  
    private RockShow rockShow;  
  
    @Before  
    public void setup() {  
        rockShow = new RockShow();  
        rockShow.bookBand("The Weakerthans");  
        rockShow.bookBand("AndyShauf");  
        rockShow.setVenue("The Commodore");  
        rockShow.setMaxAudienceSize(1000);  
        rockShow.setAudienceSize(999);  
    }  
}

![[Pasted image 20250119213712.png]]
- it checks <=
![[Pasted image 20250119213730.png]]
![[Pasted image 20250119213748.png]]

# Second
### HouseHunter - write some tests

Recall the HouseHunter methods:

//MODIFIES: this  
//EFFECTS:  adds the house to the list of houses to visit  
public void addInterestingHouse(House h){ }  
  
//EFFECTS:  returns the most recently added house  
//          and takes it off the list of houses to visit  
//          returns null if there is no house to visit  
public House getNextHouseToVisit(){ return new House(); }

You have implemented this test method:

//TODO: make sure two houses are successfully added  
@Test  
public void testAddTwoHouses(){  
    // setup the test  
    HouseHunter hh = new HouseHunter();  
    House h1 = new House();  
    House h2 = new House();  
  
    // call the method to test  
    hh.addInterestingHouse(h1);  
    hh.addInterestingHouse(h2);  
  
    // check the outcome  
    House gh1 = hh.getNextHouseToVisit();  
    House gh2 = hh.getNextHouseToVisit();  
  
    if (gh1 == null) { fail(); }  
    if (gh2 == null) { fail(); }  
  
    assertEquals(h1, hh.getNextHouseToVisit());  
    assertEquals(h1, hh.getNextHouseToVisit());  
    assertNull(hh.getNextHouseToVisit());  
    assertEquals(h2, hh.getNextHouseToVisit());  
    assertEquals(h1, hh.getNextHouseToVisit());  
}

Your test is just not working and you suspect you have some unnecessary parts.  Below, select the lines of code that should stay
![[Pasted image 20250119214019.png]]

# Junit annotations
![[Pasted image 20250119214057.png]]

# jUnit test methods
![[Pasted image 20250119214153.png]]

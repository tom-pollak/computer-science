import static org.junit.Assert.*;

import org.junit.Test;

public class TestQuestion_1_iii {

	@Test
	/**
	 * Test if the method getUser returns the correct user when given a 
	 * valid ID.
	 */
	public void testGetUser() {
		// Test is worth 2 marks
		SocialNetwork network = new SocialNetwork("CS");
		network.createUser("u01", "Lilian");
		network.createUser("u02", "Jeremy");
		
		assertEquals(new User("u01", "Lilian"), network.getUser("u01"));
		assertEquals(new User("u02", "Jeremy"), network.getUser("u02"));
	}


	@Test(expected = IllegalArgumentException.class)
	/**
	 * Test if the method getUser throws an IllegalArgumentException if an 
	 * invalid id is given in the parameter, that is the id does not exist
	 * in this network.
	 */
	public void testGetUserError() {
		// Test is worth 2 marks
		SocialNetwork network = new SocialNetwork("CS");
		network.createUser("u01", "Lilian");
		network.createUser("u02", "Jeremy");
		
		network.getUser("u03"); // This must throw an exception as user does not exist.
	}

}

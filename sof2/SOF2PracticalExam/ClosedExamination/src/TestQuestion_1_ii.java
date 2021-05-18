import static org.junit.Assert.*;

import org.junit.Test;

public class TestQuestion_1_ii {

	@Test
	/**
	 * Test if the method createUser create correctly a user
	 */
	public void testCreateUser() {
		// Test is worth 3 marks
		SocialNetwork network = new SocialNetwork("CS");
		User p1 = network.createUser("u01", "Lilian");
		User p2 = network.createUser("u02", "Will");
		
		assertNotNull(p1);
		assertNotNull(p2);		
		assertEquals("u01", p1.id);
		assertEquals("u02", p2.id);
		assertEquals("Lilian", p1.name);
		assertEquals("Will", p2.name);
		assertTrue(p1.connections.isEmpty());
		assertTrue(p2.connections.isEmpty());				
	}

	@Test
	/**
	 * Test if the method createUser adds a newly created user ot the map of users.
	 */
	public void testCreateUserInNetwork() {
		// Test is worth 3 marks
		SocialNetwork network = new SocialNetwork("CS");
		network.createUser("u01", "Lilian");
		network.createUser("u02", "Will");

		assertTrue(network.users.size() == 2);
		assertTrue(network.users.containsValue(new User("u01", "Lilian")));
		assertTrue(network.users.containsValue(new User("u02", "Will")));
		assertTrue(network.users.containsKey("u01"));
		assertTrue(network.users.containsKey("u02"));
	}


	@Test(expected = IllegalArgumentException.class)
	/**
	 * Test if the method createUser throws an IllegalArgumentException when 
	 * trying to create a user with an existing ID.
	 */
	public void testCreateUserErrorId() {
		// Test is worth 4 marks 
		SocialNetwork network = new SocialNetwork("CS");
		network.createUser("u01", "Lilian");  // this should be fine
		network.createUser("u02", "Lilian");  // this should be fine
		network.createUser("u01", "Dimitar"); //This should throw an exception
	}

}

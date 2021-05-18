import static org.junit.Assert.*;

import org.junit.Test;

public class TestQuestion_1_iv {

	@Test
	/**
	 * Test if the method addRelationship creates the connection properly 
	 * between two users when given valid ids. In particlar checks that
	 * the conection is bi-directional.
	 */
	public void testAddRelationship() {
		// Test is worth 4 marks
		SocialNetwork network = new SocialNetwork("CS");
		User p1 = network.createUser("u01", "Lilian");
		User p2 = network.createUser("u02", "Will");
		User p3 = network.createUser("u03", "Alan");

		assertTrue(network.addRelationship("u01", "u02"));		
		assertTrue("you must add the user2 to the user1's connections.", 
				p1.connections.contains("u02"));		
		assertTrue("you must add the user1 to the user2's connections.", 
				p2.connections.contains("u01"));
		
		assertTrue(network.addRelationship("u01", "u03"));		
		assertTrue("you must add the user3 to the user1's connections.", 
				p1.connections.contains("u03"));		
		assertTrue("you must add the user1 to the user3's connections.", 
				p3.connections.contains("u01"));
		
	}
	
	@Test
	/**
	 * Test if the method addRelationship returns false if the relationship 
	 * already exists.
	 */
	public void testAddExisitingRelationship() {
		// Test is worth 4 marks
		SocialNetwork network = new SocialNetwork("CS");
		User p1 = network.createUser("u01", "Lilian");
		User p2 = network.createUser("u02", "Will");
		network.addRelationship("u01", "u02");
		assertFalse("Should return false as the relationship already exists.", network.addRelationship("u01", "u02"));		
		assertFalse("Should return false as the relationship already exists.", network.addRelationship("u02", "u01"));		
	}
	
	@Test
	/**
	 * Test if addRelationship throws an IllegalArgumentException if one of the
	 * ids is invalid (that is is not in the network). In addition, it cheks 
	 * that if a connection fails, the user connection is not modified by the
	 * operation.
	 */
	public void testAddInvalidCollaborator() {
		// Test is worth 3 marks
		SocialNetwork network = new SocialNetwork("CS");
		User u1 = network.createUser("u01", "Lilian");
		User u2 = network.createUser("u02", "Alan");

		boolean testFailed = false;
		try{
			network.addRelationship("u02", "u03");	
		}catch(IllegalArgumentException e){
			assertTrue("If addRelationship fails, the users must not be modified.",
						u2.getConnections().isEmpty());
			// Code is working fine
		}catch(Exception e){
			// The code should have thrown an IllegalArgumentException
			testFailed = true;
		}
		try{
			network.addRelationship("u03", "u01");	
		}catch(IllegalArgumentException e){
			assertTrue("If addRelationship fails, the users must not be modified.",
						u1.getConnections().isEmpty());
			// Code is working fine
		}catch(Exception e){
			// The code should have thrown an IllegalArgumentException
			testFailed = true;
		}
		try{
			network.addRelationship("u02", null);	
		}catch(IllegalArgumentException e){
			assertTrue("If addRelationship fails, the users must not be modified.",
						u2.getConnections().isEmpty());
			// Code is working fine
		}catch(Exception e){
			// The code should have thrown an IllegalArgumentException
			testFailed = true;
		}
		try{
			network.addRelationship(null, "u01");	
		}catch(IllegalArgumentException e){
			assertTrue("If addRelationship fails, the users must not be modified.",
						u1.getConnections().isEmpty());
			// Code is working fine
		}catch(Exception e){
			// The code should have thrown an IllegalArgumentException
			testFailed = true;
		}

		if(testFailed){
			fail();
		} 
	}
	
}

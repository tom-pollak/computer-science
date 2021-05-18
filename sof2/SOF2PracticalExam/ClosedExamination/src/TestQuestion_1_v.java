import static org.junit.Assert.*;

import org.junit.Test;

public class TestQuestion_1_v {

	@Test
	/**
	 * Test if the method closeness computes the correct value for a given 
	 * valid user.
	 */
	public void testCloseness() {
		SocialNetwork network = new SocialNetwork("CS");
		// you can find a representation of the graph in the network_sample.jpg file
		network.createUser("uA", "A");
		network.createUser("uB", "B");
		network.createUser("uC", "C");
		network.createUser("uD", "D");
		network.createUser("uE", "E");
		network.createUser("uF", "F");
		network.addRelationship("uA", "uB");
		network.addRelationship("uA", "uC");
		network.addRelationship("uA", "uD");
		network.addRelationship("uA", "uE");
		network.addRelationship("uC", "uB");
		network.addRelationship("uC", "uD");
		network.addRelationship("uF", "uE");

		// The distances between A and the other nodes are: B=1, C=1, D=1, E=1, F=2
		// N-1 = 5 therefore the closeness for A is 5/6
		assertEquals(5.0/6.0, network.closeness("uA"),0.000001);
		
		// The distances between F and the other nodes are: A=2, B=3, C=3, D=3, E=1
		// N-1 = 5 therefore the closeness for F is 5/12
		assertEquals(5.0/12.0, network.closeness("uF"),0.000001);
	}


	@Test(expected = IllegalArgumentException.class)
	/**
	 * Test if the method closeness throws an llegalArgumentException when an
	 * invalid used ID is given. Note also, the test fails if the method throws
	 * an IllegalArgumentException when given a vali user ID. In this test, we
	 * are not checking for the correct value, only if the method throws an
	 * exception when required.
	 */
	public void testInvalidUser() {
		SocialNetwork network = new SocialNetwork("CS");
		// you can find a representation of the graph in the network_sample.jpg file
		network.createUser("uA", "A");
		network.createUser("uB", "B");
		network.createUser("uC", "C");
		network.createUser("uD", "D");
		network.createUser("uE", "E");
		network.createUser("uF", "F");
		network.addRelationship("uA", "uB");
		network.addRelationship("uA", "uC");
		network.addRelationship("uA", "uD");
		network.addRelationship("uA", "uE");
		network.addRelationship("uC", "uB");
		network.addRelationship("uC", "uD");
		network.addRelationship("uF", "uE");

		try{
			network.closeness("uA");
		} catch( IllegalArgumentException e){
			// This should not have thrown an exception as user "uA" exists. 
			// Therefore the test fails. We DO NOT care if the computation of
			// the closeness value for this user is correct or not.
			fail();
		}
		
		// The following statement must throw an IllegalArgumentException as 
		// user "uG" does not exist.
		network.closeness("uG"); 
	}

}


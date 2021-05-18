import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Map;

import org.junit.Test;

public class TestQuestion_1_i {
    @Test
	/**
	 * Test if the constructor sets the name of the social network correctly
	 */
	public void testSocialNetworkName() {
		SocialNetwork network = new SocialNetwork("CS");		
        assertEquals("CS", network.name);
	}

	
	@Test
	/**
	 * Test if the constructor sets the users as an empty Map.
	 */
	public void testSocialNetworkUsers() {
		SocialNetwork network = new SocialNetwork("CS");		
        assertTrue(network.users instanceof Map);
        assertTrue(network.users.isEmpty());
	}
	

}

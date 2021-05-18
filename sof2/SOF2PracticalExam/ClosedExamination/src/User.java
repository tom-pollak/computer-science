import java.util.HashSet;
import java.util.Set;

public class User {
	String id; // The unique identifier of a user
	String name; // The name of the user (may not be unique)
	Set<String> connections; // Set of connection for a user. It contains the ids of users from a network
							 // having a connection with him/her.

	/**
	 * Construct an instance of User.
	 * 
	 * @param id
	 *            the unique identifier of the user
	 * @param name
	 *            the name of the user
	 */
	public User(String id, String name) {
		this.id = id;
		this.name = name;
		this.connections = new HashSet<>();
	}

	/**
	 * Return the unique identifier of the user instance.
	 * 
	 * @return the unique identifier of the user instance.
	 */
	public String getId() {
		return id;
	}

	/**
	 * Return the name of the user.
	 * 
	 * @return the name of the user.
	 */
	public String getName() {
		return name;
	}

	/**
	 * Returns the set of connection of the user, i.e. the set of user unique
	 * identifier with whom the user has a connection.
	 * 
	 * @return the set of unique identifier from user with whom he/she has a
	 *         connection.
	 */
	public Set<String> getConnections() {
		return connections;
	}

	/**
	 * Add a connection to the user's circle. Return true if the operation is
	 * successful, false otherwise (if the user already part of his/her circle of
	 * connection).
	 * 
	 * @param userId
	 *            the user'id to be added to this instance set of connections.
	 * @return true if the operation is successful, false otherwise (e.g. userId
	 *         already in the set of connections).
	 */
	public boolean addConnection(String userId) {
		if (!connections.contains(userId)) {
			connections.add(userId);
			return true;
		} else {
			return false;
		}
	}

	/**
	 * Remove a connection to the user's circle. Return true if the operation is
	 * successful, false otherwise (if the user is not part of his/her circle of
	 * connections).
	 * 
	 * @param userId
	 *            the user'id to be removed from this instance set of connections.
	 * @return true if the operation is successful, false otherwise (e.g. userId
	 *         is not in the set of connections).
	 */
	public boolean removeConnection(String userId) {
		return connections.remove(userId);
	}

	@Override
	public boolean equals(Object other) {
		if (this == other) {
			return true;
		}
		if (other instanceof User) {
			User otherUser = (User) other;
			return (otherUser.id.equals(this.id) && otherUser.name.equals(this.name));
		} else {
			return false;
		}
	}

}

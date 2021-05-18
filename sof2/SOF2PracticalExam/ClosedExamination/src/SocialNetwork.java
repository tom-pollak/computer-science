import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

/** @author Tom Pollak */
public class SocialNetwork {
  /**
   * This is a program for simulating a social network: it can create new users and as establish
   * relationships between users
   *
   * <p>Can calculate the normalised closeness centrality of any users in the network
   *
   * @param name name of the social network
   */
  String name;

  Map<String, User> users;

  public SocialNetwork(String name) {
    this.name = name;
    users = new HashMap<String, User>();
  }

  /**
   * Method to create a user
   *
   * @param id users unique ID
   * @param username users username on the network
   * @return User object
   * @throws IllegalArgumentException if a user with the ID from param already exists
   */
  public User createUser(String id, String username) {
    if (users.get(id) != null) {
      throw new IllegalArgumentException("User with id: " + id + " already exists!");
    }
    User user = new User(id, username);
    users.put(id, user);
    return user;
  }
  /**
   * Get a user using their unique ID
   *
   * @param id users ID
   * @return User object
   * @throws IllegalArgumentException if user with "id" does not exist
   */
  public User getUser(String id) {
    User user = users.get(id);
    if (user == null) {
      throw new IllegalArgumentException("User with id: " + id + " does not exist!");
    }
    return user;
  }

  /**
   * Adds a relationship between the two users in the social network
   *
   * @param userOneID ID of a user to add relationship
   * @param userTwoID ID of the other user to add relationship
   * @return boolean: whether the operation was successful
   * @throws IllegalArgumentException if either or both IDs were not linked to a user
   */
  public boolean addRelationship(String userOneID, String UserTwoID) {
    User userOne = getUser(userOneID);
    User userTwo = getUser(UserTwoID);
    // Uses && to evaluate both statements even if the first is false
    return userOne.addConnection(UserTwoID) && userTwo.addConnection(userOneID);
  }

  /**
   * Calculates normalised closeness centrality of a user in the network: The average number of
   * relationships between the specified user and all other users in the network
   *
   * @param userID users ID
   * @return double: average number of relationships with every other user
   * @throws IllegalArgumentException if userID is not linked to a user
   */
  public double closeness(String userID) {
    double totalDistance = 0;
    double currentDistance;
    User rootUser = getUser(userID);
    Set<Entry<String, User>> userSet = users.entrySet();
    Map<User, Boolean> visited = new HashMap<User, Boolean>();
    LinkedList<User> queue = new LinkedList<User>();
    LinkedList<Double> distQueue = new LinkedList<Double>();
    visited.put(rootUser, true);
    queue.add(rootUser);
    distQueue.add(0.0);

    while (queue.size() != 0) {
      User user = queue.poll();
      currentDistance = distQueue.poll();
      totalDistance += currentDistance;
      Iterator<String> i = user.getConnections().iterator();
      while (i.hasNext()) {
        String nextUserID = i.next();
        User nextUser = getUser(nextUserID);
        if (visited.get(nextUser) == null) {
          visited.put(nextUser, true);
          queue.add(nextUser);
          distQueue.add(currentDistance + 1.0);
        }
      }
    }
    return (userSet.size() - 1) / totalDistance;
  }
}

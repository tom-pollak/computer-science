package algebra;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.io.BufferedWriter;
import java.io.FileWriter;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestRule;
import org.junit.rules.TestWatcher;
import org.junit.rules.Timeout;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;

public class VectorTest {

	@Test
	public void testVector() {
		double[] data = {3,4,5};
		Vector v = new Vector(data);

		assertEquals(data.length, v.vector.length);

		for(int i = 0; i < data.length; i++){
			assertEquals(data[i], v.vector[i], 0.0000000001);
		}
		data[0] = 0;
		assertFalse(data[0] == v.vector[0]);
	}

	@Test
	public void testScalarProduct(){
		double[] data = {3,4,5,4};
		double scalar = 2.0;
		Vector v = new Vector(data);
		Vector v2 = v.scalarProduct(scalar);

		// Check that the resulting vector v2 is correct
		for(int i = 0; i < v2.vector.length; i++){
			assertEquals(data[i]*scalar, v2.vector[i], 0.0000000001);
		}

		// Check that the original vector v is not modified
		for(int i = 0; i < v.vector.length; i++){
			assertEquals(data[i], v.vector[i], 0.0000000001);
		}
	}

	@Test(expected = InvalidDimensionException.class)
	public void testGet(){
		double[] data = {3,4,5,4};
		Vector v = new Vector(data);
		for(int i = 0; i < v.vector.length; i++){
			assertEquals(data[i], v.get(i), 0.00000001);
		}
		double n = v.get(5);
	}

	@Test(expected = InvalidDimensionException.class)
	public void testGetError(){
		double[] data = {3,4,5,4};
		Vector v = new Vector(data);
		for(int i = 0; i < v.vector.length; i++){
			assertEquals(data[i], v.get(i), 0.00000001);
		}
		double n = v.get(-2);
	}

	@Test
	public void testAdd()throws IncompatibleDimensionException{
		double[] data = {1,2,3,4}, data1 = {5,6,7,8};
		Vector v = new Vector(data);
		Vector v2 = new Vector(data1);
		Vector v3 = v.add(v2);
		for(int i = 0; i < v.vector.length; i++){
			assertEquals(data[i] + data1[i], v3.vector[i], 0.00000001);
		}
		for(int i = 0; i < v.vector.length; i++){
			assertEquals(data[i], v.vector[i], 0.00000001);
		}
		for(int i = 0; i < v.vector.length; i++){
			assertEquals(data1[i], v2.vector[i], 0.00000001);
		}
	}

	@Test(expected = IncompatibleDimensionException.class)
	public void testAddError() throws IncompatibleDimensionException{
		Vector v = new Vector(new double[]{1,2,3,4});
		Vector v2 = new Vector(new double[]{5,6,7});
		v2 = v2.add(v);
	}
}

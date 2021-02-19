public class Rectangle extends Shape {

	private double width, length;

	public Rectangle(double width, double length, String color, boolean filled) {
		super(color, filled);
		this.width = width;
		this.length = length;
	}

	public Rectangle(double width, double length) {
		super();
		this.width = width;
		this.length = length;
	}

	public Rectangle() {
		this(1, 1);
	}

	public double getWidth() {
		return width;
	}

	public double getLength() {
		return length;
	}

	public void setWidth(double width) {
		this.width = width;
	}

	public void setLength(double length) {
		this.length = length;
	}

	public double getArea() {
		return width * length;
	}

	public double getPerimeter() {
		return 2 * width + 2 * length;
	}

	@Override
	public String toString() {
		return "A Rectangle with width=" + width + " and length=" + length + ", which is a subclass of "
				+ super.toString();
	}

}

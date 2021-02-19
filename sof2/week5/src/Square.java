public class Square extends Rectangle {
	private double side;

	public Square(double side, String color, boolean filled) {
		super(side, side, color, filled);
		this.side = side;
	}

	public double getSide() {
		return side;
	}

	public void setSide(double side) {
		this.side = side;
	}

	@Override
	public void setWidth(double side) {
		setLength(side);
		setWidth(side);
	}

	@Override
	public void setLength(double side) {
		setLength(side);
		setWidth(side);
	}

	@Override
	public String toString() {
		return "A Square with side=" + side + ", which is a subclass of " + super.toString();
	}

	public static void main(String[] args) {
		Square s = new Square(4, "red", true);
		System.out.println(s);
	}
}


public class IntegerComparable implements Comparable<IntegerComparable>{
	private int number;
	
	public IntegerComparable(int number) {
		super();
		this.number = number;
	}

	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}

	@Override
	public int compareTo(IntegerComparable another) {
		if(this.getNumber() < another.getNumber()) {
	        return -1;
	    } else if (this.getNumber() > another.getNumber()) {
	        return 1;
	    } else {
	        return 0;
	    }
	}
}

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		int[] array1 = {1,3,5,7};
//		int[] array2 = {2,4,6,8};
//		int[] array3 = {0,10,20,30};
//		
//		List<Integer> list = Arrays.stream(array1).boxed().collect(Collectors.toList());
//		List<Integer> list2 = Arrays.stream(array2).boxed().collect(Collectors.toList());
//		List<Integer> list3 = Arrays.stream(array3).boxed().collect(Collectors.toList());
//		

		List<Comparable> integerComparableList1 = new ArrayList<Comparable>();
		
		integerComparableList1.add(new IntegerComparable(1));
		integerComparableList1.add(new IntegerComparable(3));
		integerComparableList1.add(new IntegerComparable(5));
		integerComparableList1.add(new IntegerComparable(7));
		
		List<Comparable> integerComparableList2 = new ArrayList<Comparable>();
		
		integerComparableList2.add(new IntegerComparable(2));
		integerComparableList2.add(new IntegerComparable(4));
		integerComparableList2.add(new IntegerComparable(6));
		integerComparableList2.add(new IntegerComparable(8));
		
		List<Comparable> integerComparableList3 = new ArrayList<Comparable>();
		
		integerComparableList3.add(new IntegerComparable(0));
		integerComparableList3.add(new IntegerComparable(10));
		integerComparableList3.add(new IntegerComparable(20));
		integerComparableList3.add(new IntegerComparable(30));

		List<Iterator<Comparable>> iteratorList = new ArrayList<Iterator<Comparable>>();
		
		iteratorList.add(integerComparableList1.iterator());
		iteratorList.add(integerComparableList2.iterator());
		iteratorList.add(integerComparableList3.iterator());
		SequenceIterator seqIterator = new SequenceIterator(iteratorList);
		
		
		while (seqIterator.hasNext()) {
			System.out.println(((IntegerComparable) seqIterator.next()).getNumber() );
		}
		

	}

}

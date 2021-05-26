import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class SequenceIterator {
	
	List<Iterator<Comparable>> inputCollection;
	List<Comparable> workList = new ArrayList<Comparable>();
	
	Iterator<Comparable> mainIterator;
	
	@SuppressWarnings("unchecked")
	public SequenceIterator(Collection<Iterator<Comparable>> inputs) {
		this.inputCollection = (List<Iterator<Comparable>>) inputs;
		
		Iterator<Iterator<Comparable>> auxIterator = this.inputCollection.iterator();
        while (auxIterator.hasNext()) {
           Iterator<Comparable> auxIterable = auxIterator.next();
           
           while (auxIterable.hasNext()) {
        	   this.workList.add(auxIterable.next());
           }
        }
		
        Collections.sort(this.workList);
        
        this.mainIterator = this.workList.iterator(); 
	}

	public boolean hasNext() {
		return this.mainIterator.hasNext();
	}

	public Comparable next() {
		return this.mainIterator.next();
	}
}
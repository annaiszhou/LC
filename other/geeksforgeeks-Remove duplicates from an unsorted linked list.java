/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* The structure of linked list is the following
class Node
{
    int data;
    Node next;
    Node(int d) {data = d; next = null; }
}
*/
class GfG
{
    Node removeDuplicates(Node head)
    {
    	if (head == null) {
    		return head;
    	}
    	Node cur = head;
    	while (cur != null) {
    		Node check = cur;
    		while (check.next != null) {
    			if (check.next.data == cur.data) {
    				check.next = check.next.next;
    			}else {
    				check = check.next;
    			}
    		}
    		cur = cur.next;
    	}
    	return head;
    }
}

#Execution Time:0.21
#space: O(n^2)
#time: O(1)

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* The structure of linked list is the following
class Node
{
    int data;
    Node next;
    Node(int d) {data = d; next = null; }
}
*/
class GfG
{
    Node removeDuplicates(Node head)
    {
    	if (head == null) {
    		return head;
    	}
    	Node cur == head;
    	HashMap<Interger,Boolean> hash = new HashMap<Interger,Boolean>();
    	hash.put(cur.data,true);
    	while (cur.next != null) {
    		if (hash.containskey(cur.next.data)) {
    			cur.next = cur.next.next;
    		} else {
    			hash.put(cur.next.val,true);
    			cur = cur.next;
    		}
    	}
    	return head;
    }
}

#time: O(n)
#space: O(n)

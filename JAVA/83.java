/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    	if (head == null || head.next == null) {
    		return head;
    	}
    	ListNode cur = head;
    	while (cur != null) {
    		while (cur.next !=null && cur.val == cur.next.val) {
    			cur.next = cur.next.next;
    		}
    		cur = cur.next;
    	}
        return head;
    }
}

#Runtime: 1 ms
#Your runtime beats 26.97 % of java submissions.
#space: O(1)
#time: O(n)
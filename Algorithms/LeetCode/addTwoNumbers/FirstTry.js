/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function reverse2(array){
    let newarray = []
    for (let i = array.length-1; i >= 0; i--){
        newarray.push(array[i])
    }
    return newarray
}
 var addTwoNumbers = function(l1, l2) {
    console.log(l1,l2)
    let l1Num = l1;
    l1Num = reverse2(l1Num);
    console.log(l1Num);
    l1Num = Number(l1Num.join(""))
    let l2Num = l2;
    l2Num = reverse2(l2Num);
    l2Num = Number(l2Num.join(""))
    let sum = l1Num + l2Num
    sum = sum.toString();
    sum = sum.split("")
    sum = reverse2(sum);
    returnSum = []
    for (el of sum){
        returnSum.push(Number(el));
    }
    console.log(returnSum)
    return returnSum
};

addTwoNumbers([2,4,3],[5,6,4])
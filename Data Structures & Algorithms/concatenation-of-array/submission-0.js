class Solution {
    getConcatenation(nums) {
        let n = nums.length;
        let arr=new Array(2*n);
        for(let i=0;i<n;i++){
         arr[i]=arr[i+n]=nums[i]
        }
       return arr;
    }
}
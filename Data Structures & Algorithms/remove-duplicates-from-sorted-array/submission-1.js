class Solution {
    removeDuplicates(nums){
    let k=1; 
        for(let n=1; n < nums.length;n++){
            if(nums[n]!=nums[n-1]){
                nums[k++]=nums[n];
         
            }
        }
        return k;
    }
}
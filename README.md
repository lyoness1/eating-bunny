# eating-bunny

Input: An N x M matrix of a gardent. Each cell contains an integer representing the number of carrots in that part of the garden. 
Output: The number of carrots Mr. Bunny eats before falling asleep. 

Mr. Bunny starts in the center of the garden. 
If there are more than one center cell, Mr. Bunny starts in the cell with the largest number of carrorts. 
There will never be a tie for the highest number of carrots in a center cell. 
Mr. Bunny eats all of the carrots in his cell, then looks left, right, up, and down for more carrots. 
Mr. Bunny always moves to the adjacent cell with the highest carrot count. 
If there are no adjacent cells with carrots, Mr. Bunny falls asleep. 

<h2><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array">153. Find Minimum in Rotated Sorted Array</a></h2><h3>Medium</h3><hr><p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n) time</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>
<h3>Solution</h3>
<p>[a,b,c,d,e,f...] find min but we know as its rotated, if the min is less then the right side pointer, we know that the left sub list is of no use so now we increment l to mid+1 to find the min in the right sub list</p>
<p>But is the left sub list is sorted, the mid will be greater than the left pointer so in this case we make the right pointer to mid pointer (remember not the mid because if we do so, in smaller sub lists, we can loose the track and can go directly to the left sublist when we are searching in right sublist (happens when there are 2 elements left in the list) thus at the end of the loop we can return l or r as both will point to the minimum which is also the reason for putting condition l(<)r in while loop so that l donot cross r</p>
<h3>Example</h3>
<p>[3,4,5,1,2]</p>
<p>l=3</p>
<p>m=5</p>
<p>r=2 now m(>)2 so we use the right sublist so l=m+1</p>
<p>l,m,r = 1,1,2</p>
<p>m(<)2 but if we do r=m-1, l=1 but r=5 and m=4 which won't give the right answer </p>
<p>Thus now r=m so l,m,r=1 which returns the func as now l is not less than r anymore</p>

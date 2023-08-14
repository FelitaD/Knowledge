
[[Bubble Sort]]
[[Selection Sort]]
[[Insertion Sort]]

- **[[Divide and Conquer]] sorts**
[[Merge Sort]]
[[Quick Sort]]

- **Stability**
	- Stable: preserve order of similar cards
		- Merge sort
		- Insertion sort
		- Bubble sort
	- Unstable
		- Quick sort
		- Selection sort

## Quick sort

Quick Sort is another Divide and Conquer sorting algorithm (the other one discussed in this visualization page is [Merge Sort](https://visualgo.net/en/sorting?slide=11)).
We will see that this deterministic, non randomized version of Quick Sort can have bad time complexity of O(**N**2) on adversary input before continuing with the [randomized](https://visualgo.net/en/sorting?slide=13) and usable version later.

Divide step: Choose an item **p** (known as the pivot)  
Then partition the items of **a[i..j]** into three parts: **a[i..m-1]**, **a[m]**, and **a[m+1..j]**.
**a[i..m-1]** (possibly empty) contains items that are smaller than (or equal to) **p**
**a[m] = p**, i.e., index **m** is the correct position for **p** in the sorted order of array **a**
**a[m+1..j]** (possibly empty) contains items that are greater than (or equal to) **p**
Then, recursively sort the two parts.
Conquer step: Don't be surprised... We do nothing :O!

Initially, both **S1** and **S2** regions are empty, i.e., all items excluding the designated pivot **p** are in the unknown region.
Then, for each item **a[k]** in the unknown region, we compare **a[k]** with **p** and decide one of the three cases:
1. If **a[k]** > **p**, put **a[k]** into **S2**,
2. If **a[k]** < **p**, put **a[k]** into **S1**,
3. If **a[k]** == **p**, throw a coin and put **a[k]** into **S1**/**S2** if it lands head/tail, respectively.
Lastly, we swap **a[i]** and **a[m]** to put pivot **p** right in the middle of **S1** and **S2**.

We set **p = a[0] = 27**.  
We set **a[1] = 38** as part of **S2** so **S1 = {}** and **S2 = {38}**.  
We swap **a[1] = 38** with **a[2] = 12** so **S1 = {12}** and **S2 = {38}**.  
We set **a[3] = 39** and later **a[4] = 29** as part of **S2** so **S1 = {12}** and **S2 = {38,39,29}**.  
We swap **a[2] = 38** with **a[5] = 16** so **S1 = {12,16}** and **S2 = {39,29,38}**.  
We swap **p = a[0] = 27** with **a[2] = 16** so **S1 = {16,12}**, **p = {27}**, and **S2 = {39,29,38}**.

  

After this, **a[2] = 27** is guaranteed to be sorted and now Quick Sort recursively sorts the left side **a[0..1]** first and later recursively sorts the right side **a[3..5]**.

**Quicksort** is an efficient, general-purpose [sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm "Sorting algorithm").  
It is still a commonly used algorithm for sorting. Overall, it is slightly faster than [merge sort](https://en.wikipedia.org/wiki/Merge_sort "Merge sort") and [heapsort](https://en.wikipedia.org/wiki/Heapsort "Heapsort") for randomized data, particularly on larger distributions.

Quicksort is a [divide-and-conquer algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm "Divide-and-conquer algorithm"). It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. For this reason, it is sometimes called **partition-exchange sort**.
The sub-arrays are then sorted [recursively](https://en.wikipedia.org/wiki/Recursion_(computer_science) "Recursion (computer science)"). This can be done [in-place](https://en.wikipedia.org/wiki/In-place_algorithm "In-place algorithm"), requiring small additional amounts of [memory](https://en.wikipedia.org/wiki/Main_memory "Main memory") to perform the sorting.

Quicksort is a [comparison sort](https://en.wikipedia.org/wiki/Comparison_sort "Comparison sort"), meaning that it can sort items of any type for which a "less-than" relation (formally, a [total order](https://en.wikipedia.org/wiki/Total_order "Total order")) is defined. Most implementations of quicksort are not [stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability "Sorting algorithm"), meaning that the relative order of equal sort items is not preserved.

[Mathematical analysis](https://en.wikipedia.org/wiki/Analysis_of_algorithms "Analysis of algorithms") of quicksort shows that, [on average](https://en.wikipedia.org/wiki/Best,_worst_and_average_case "Best, worst and average case"), the algorithm takes �(�log⁡�)![O(n\log {n})](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b5ea2d55d8c31feb17ce14f35da4c93f94982b3) comparisons to sort _n_ items. In the [worst case](https://en.wikipedia.org/wiki/Best,_worst_and_average_case "Best, worst and average case"), it makes �(�2)![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392) comparisons.
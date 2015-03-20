EnhancedSalesmanSearch
======================
Use at your own risk, lists of size 10 and less don't take much memory or time but anything beyond that gets insane fast.
   11 elements require >= 6GB of memory and I ran out of ram and swap before it could finish.
   God have mercy on your soul if you run it with a 20 element list.

Very "efficient" search algorithm that will either output the key was found or that it wasn't knowing where it was found doesn't matter

As far as I can tell it has an effciency of either O(2^(n!)) or O(2^(n-1!)).

This works by getting all subsets of the initial list and then by getting the permutation of each
of those subsets. Then it will look through the permutations for lists that are 1 element long and 
compare that element to the key.

The name comes from the Traveling Salesman problem whose effciency is O(n!) for a brute force approach

To Run:
    Open a terminal and cd to the directory the .py file is in
    Then type 'python EnhancedSalesmanSearch.py'

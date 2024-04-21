"""
Create a method each_cons that accepts a list and a number n, 
and returns cascading subsets of the list of size n, like so:

each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]

each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]
  
As you can see, the lists are cascading; ie, they overlap, but never out of order.

"""
#first_solution
def each_cons(lst, n):
    num_of_iterate = (len(lst)-n) + 1
    main_list = []
    for i in range(num_of_iterate):
        sub_list = []
        for j in range(n):
            sub_list.append(lst[j+i])
        main_list.append(sub_list)
    return main_list


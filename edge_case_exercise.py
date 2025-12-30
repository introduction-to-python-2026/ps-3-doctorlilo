def move(my_list, direction):

    if 1 not in my_list:
       return my_list 
    index_of_one = my_list.index(1)
    
    if index_of_one != len(my_list) -1 and  direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif index_of_one != 0 and direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
   

    return my_list

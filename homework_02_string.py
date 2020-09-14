# A function to put consecutive duplicates of a given list into sub-lists

def split_consecutive_duplicates(givenlist):
    """
     Returns the consecutive duplicates of a given list into sublists
     :param givenlist:
         list object
    """
    split = []
    tmp = []
    # Split the consecutive duplicates from the given list into sublists
    for i in range(len(givenlist)):
        if i == 0:
            tmp = [givenlist[i]]
            split.append(tmp)
        elif givenlist[i] != givenlist[i-1]:
            tmp = [givenlist[i]]
            split.append(tmp)
        elif givenlist[i] == givenlist[i-1]:
            tmp.append(givenlist[i])

    return split


input_list = [0, 0, 1,1,1, 2, 3, 4, 4, 6, 6, 6, 8, 4, 4]
split_list = split_consecutive_duplicates(input_list)
print(split_list)

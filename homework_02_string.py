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
        elif givenlist[i] != givenlist[i-1]:
            tmp = [givenlist[i]]
        elif givenlist[i] == givenlist[i-1]:
            tmp.append(givenlist[i])
        split.append(tmp)
    final = []
    # Remove the duplicated sublists from the split list.
    for i in range(len(split)):
        if i == 0:
            final.append(split[i])
        elif split[i] != split[i-1]:
            final.append(split[i])
        elif split[i] == split[i-1]:  # skip if it equals to the previous sublist
            continue
    return final


input_list = [0, 0, 1,1,1, 2, 3, 4, 4, 6, 6, 6, 8, 4, 4]
split_list = split_consecutive_duplicates(input_list)
print(split_list)

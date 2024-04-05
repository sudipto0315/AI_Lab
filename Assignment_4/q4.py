def find_max_between_lists(list1, list2):
    max_list = []
    for num1, num2 in zip(list1, list2): # zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
        max_list.append(max(num1, num2))
    return max_list

def main():
    list1 = [1, 5, 3, 8, 10]
    list2 = [2, 4, 6, 7, 9]

    max_list = find_max_between_lists(list1, list2)
    print("Maximum elements between corresponding elements of two lists:", max_list)

if __name__ == "__main__":
    main()
def count_occurrence(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 4, 2]
    target_element = 2

    count = count_occurrence(my_list, target_element)
    print(f"The element {target_element} occurs {count} times in the list.")


main()
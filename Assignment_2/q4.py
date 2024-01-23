file_path="Assignment_2/text.txt"

def count_lines_not_starting_with_T(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        count=0
        for line in lines:
            if not line.strip().startswith('T'):
                count+=1
    return count


result = count_lines_not_starting_with_T(file_path)
print ("Number of lines not starting with 'T' in '{}': {}".format(file_path, result))
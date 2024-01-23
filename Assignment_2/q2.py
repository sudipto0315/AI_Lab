# python file modes>>
# for text files:
# r: read only
# w: write only
# a: append only
# r+: read and write
# w+: write and read
# a+: append and read
# for binary files:
# rb: read only in binary format
# wb: write only in binary format
# ab: append only in binary format
# rb+: read and write in binary format
# wb+: write and read in binary format
# ab+: append and read in binary format
output_file=open("Assignment_2/output.txt","w+")
input_file=open("Assignment_2/example.txt","r")
number=int(input("Enter the no of characters to be read form the input file: "))
output_file.write(input_file.read(number))
output_file.seek(0)
print("This text was copied to the output.txt file: ")
print(output_file.read())
input_file.close()
output_file.close()

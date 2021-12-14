# open a file, read-only 'r'
jabber = open("/Users/denesgeza/Dropbox/Python/Py_MasterClass/File IO/sample.txt", 'r')
#
# # works also with relative paths, work folder
# # jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# # close the files
# jabber.close()

# same thing as above
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# read all lines as they exist
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("c:\Users\denes\Dropbox\Python\Py_MasterClass\File IO\sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)

# for line in lines[::-1]:
#     print(line, end='')

# readline --> reads a single line
# readlines --> reads the entire file
# read ---> reads the entire file
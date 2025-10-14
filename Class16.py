# #*****************File Handling in Python****************
file = open('zia.txt', 'w')
file.write('Hello Students!\n')
file.write('This is your first file in python\n')
file.close()
print('FIle written successfully!')

file = open('zia.txt', 'a')
file.write('\nAppending a new Line in file')
file.close()
print('New Data Added successfully!')


#File reading line by line
file = open('zia.txt', 'r')
for line in file:
    print(line)
file.close()

# file reading by using .read() for the entire content of the file
file = open('zia.txt', 'r')
data = file.read()
print(data)
file.close()

# file reading by using .readline() 
file = open('zia.txt', 'r')
line1 = file.readline()
line2 = file.readline()
print('Line 1', line1)
print('Line 2', line2)


# file reading by using .readlines() for reading multiple lines of data from a file
file = open('zia.txt', 'r')
lines = file.readlines()
print(type(lines))
print(lines)

# filehandling with "with " keyword
with open('student.txt', 'w') as f:
    f.write('ALi\n')
    f.write('Sara\n')
    f.write('Umaima')
print('File automatically close!')

with open('student.txt', 'r') as a:
    lines = a.readlines()
    print(lines)

#.strip() method for removing white spaces from the strings.....
for line in lines:
    print(line.strip())
    
with open('data.txt', 'w') as f:
    f.write('Apple\n')
    f.write('Mango\n')
    f.write('Banana\n')

with open('data.txt', 'a') as f:
    f.write('Grapes\n')
    f.write('Watermelon')

with open('data.txt', 'r') as f:
    content = f.read()



with open('story.txt','r') as f:
  line_count = 0
  word_count = 0
  char_count = 0
  for line in f:
    line_count += 1
    words = line.split()
    word_count += len(words)
    char_count += len(line)
print('Lines:',line_count)
print('Words:',word_count)
print('Chars:',char_count)
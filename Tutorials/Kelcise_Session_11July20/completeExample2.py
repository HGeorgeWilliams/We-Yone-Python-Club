#Using the for loop to Read a Text File Line by Line in Python

# Open the file to be read
f = open('communityDetails.txt', 'r')

for line in f:
    print(line)

f.close()

# Open the file to be read
f = open('communityDetails.txt', 'r')

# use while to loop through the lines in the document and readline() to read line by line
while True:
    # use realine() to read each line
    fname = f.readline()
    sname = f.readline()
    dob = f.readline()

    userID = fname[0:1] + sname[0:1] + dob[6:10] + dob[3:5] + dob[0:2]
    print(userID.lower())

    # check if line is not empty
    if not fname:
        break

f.close()
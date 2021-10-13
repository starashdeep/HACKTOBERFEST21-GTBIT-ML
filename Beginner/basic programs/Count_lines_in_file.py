def file_len(fname):
    #make a file in your system called "myfile.txt"
    #in 3 separate lines , put in your name , your college name and your year of graduation
    #use python to go through the file and print the number of lines inside the file
    # as you may have already guessed , the answer should be 3
    
    # using file check the count function
    file = open("myfile.txt", "r")
    
    # this will count the number of lines initiated
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    # finally displaying he result
    print(line_count)

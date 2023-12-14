# coding: utf-8
import time

start_time = time.time()
file = open("input.txt", "r")

txt = file.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

cnt = 0

for line in txt:
    first = "0"
    last = "0"
    first_index = 0
    last_index = 0

    ### Find written number
    for i in range(0, len(numbers)):

        # First occurrence
        word_index = line.find(numbers[i])
        if word_index != -1:
            if word_index < first_index or first == "0":
                first = str(i+1)
                first_index = word_index

        # Last occurrence
        word_rindex = line.rfind(numbers[i])
        if word_rindex != -1:
            if word_rindex > last_index or last == "0":
                last = str(i+1)
                last_index = word_rindex
        
    ### Find digit number
    # First occurrence
    for char_index in range(0, len(line)):
        if ord(line[char_index]) > 48 and ord(line[char_index]) <= 57:
            if char_index < first_index or first == "0":
                first = str(line[char_index])
                first_index = char_index

    # Last occurrence
    for char_index in reversed(range(0, len(line))):
        if ord(line[char_index]) > 48 and ord(line[char_index]) <= 57:
            if char_index > last_index or last == "0":
                last = str(line[char_index])
                last_index = char_index

    cnt += int(first+last)

print(cnt)

file.close()
print("--- %s seconds ---" % (time.time() - start_time))
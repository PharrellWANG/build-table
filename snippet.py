file = open('txt/size_04.txt', 'r')
# print(file.readline(3))
# print(file.readline(4))
myList = []

for line in file:

    myList.append(line)

LINE_IDX = 4

START_POS_ONE = 12
START_POS_TWO = 72

number_of_samples = myList[LINE_IDX+4][START_POS_ONE:START_POS_ONE+9]
percentage = myList[LINE_IDX+4][START_POS_TWO:START_POS_TWO+8]
print(number_of_samples)
print(type(number_of_samples))
print(percentage)
print(type(percentage))

print(int(number_of_samples))
print(float(percentage)*100)

print('number of samples: %d7' % int(number_of_samples))
print('percentage : ' + "{0:.2f}".format(round(float(percentage)*100, 2)))
# print(type(myList[4]))
# print(myList[40])
# print(type(myList[40]))
file.close()
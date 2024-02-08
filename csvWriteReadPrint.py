import csv
import pandas
import statistics

csvfile = open("myfile3.csv", "x", newline = '')
print("File Created")
# Create column headers
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Temp', 'Noise'])
print("Columns Created")
# Create 4 rows of data 
csvwriter.writerow([21, 10])
csvwriter.writerow([24, 12])
csvwriter.writerow([12, 9])
csvwriter.writerow([33, 77])

print("Data Created")
# Close the file
csvfile.close()
print("closed after created rows")

# Open the file read it and print the first 2 rows
csvfile = open("myfile3.csv","r", newline = '')
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
line = csvfile.readline()
print(line, "readline4")
line = csvfile.readline()
print(line, "readline5")
csvfile.close()
print("closed after printing rows")

# open the file to append to it
csvfile = open('myfile3.csv',"a")
csvfile.close()
print("closed append")
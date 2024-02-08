#Event:ALT2
import statistics
import pandas
import matplotlib.pyplot as plt
import csv

filename = 'ALT2_Data'
csvfile = open(filename, "r")

print("File opened")
with open('ALT2_Data', 'r') as filename:
  csv_reader = csv.reader(filename)
  for row in csv_reader:
    print(row[0],row[1])

csvfile.close()
print("closed")
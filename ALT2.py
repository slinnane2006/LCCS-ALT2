
#Event:ALT2
import statistics
import pandas
import matplotlib.pyplot as plt
import csv

filename = 'ALT2_Data.csv'

#csvfile = open(filename, "r")
df = pandas.read_csv('ALT2_Data.csv')
print("File opened")
with open('ALT2_Data.csv', 'r') as filename:
  csv_reader = csv.reader(filename)
  for row in csv_reader:
    print(row[0],row[1])

csvfile.close()
print("closed")

filename = 'ALT2_Data.csv'
csvfile = open(filename, "r")
df = pandas.read_csv('ALT2_Data.csv')
olc=df['OnlineCovid']
print(olc)

# Compute and display the mean
mean_value = round(statistics.mean(olc), 2)
print("Mean Value:", mean_value)

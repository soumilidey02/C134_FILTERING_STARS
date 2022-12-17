import pandas as pd
import matplotlib.pyplot as plt             
import csv

df = []
with open('final.csv','r') as f:
  csvreader = csv.reader(f)
  for i in csvreader:                                               
    if i != []:              
      df.append(i)

headers = df[0]
headers[0] = 'Index'
data = df[1]

stars_filtered_distance = []
for i in data:   
  if float(i[2]) <= 100:      
    stars_filtered_distance.append(i)
  else:
    pass                            

stars_filtered_gravity = []
for i in stars_filtered_distance:
  if float(i[5].split(' ')[0]) > 150 and float(i[5].split(' ')[0]) < 350:
    stars_filtered_gravity.append(i)
  else:
    pass

with open('filtered_stars.csv','w') as f:
  csvWriter = csv.writer(f)
  csvWriter.writerow(headers)
  csvWriter.writerows(stars_filtered_gravity)
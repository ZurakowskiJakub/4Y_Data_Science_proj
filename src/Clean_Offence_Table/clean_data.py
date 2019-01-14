import csv

with open('offensetable1.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

check = ['CR','HG','CJ','FL','AB','NR','FI','IN','(penalty)','RP','BO','BR','TR','PS',
         'EL','CL','HS','TG','HO','CP','FL','SG','SF','HU','EN','CA','FI']

for i in your_list:
  for t in check:
    if t in i[0]:
      i[0] = i[0].split(t)[0]
  if not i[0]: your_list.remove(i)
  elif not i[2]: your_list.remove(i)

for i in your_list:
  for t in check:
    if t in i[0]:
      i[0] = i[0].split(t)[0]
  if not i[0]: your_list.remove(i)
  elif not i[2]: your_list.remove(i)


with open("output.csv", 'w') as resultFile:
  wr = csv.writer(resultFile, dialect='excel',delimiter=',')
  wr.writerows(your_list)



print(len(your_list))
print(your_list)

with open('output.csv', 'r') as f:
  reader = csv.reader(f)
  new_list = list(reader)

print(len(new_list))
print(new_list)

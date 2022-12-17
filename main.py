import matplotlib.pyplot as plt
import csv


#Average PH levels by mointh

x = []
y = []

with open('waterq.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        x.append(row[4])
        y.append(str(row[7]))

plt.bar(x, y, color = 'g', width = 0.72, label = "pH")
plt.xlabel('Day')
plt.ylabel('pH')
plt.title('Average pH levels by day')
plt.legend()
plt.show()


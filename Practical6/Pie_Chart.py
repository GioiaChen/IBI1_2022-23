# Import the matplotlib and use the data to draw a pie chart.
import matplotlib.pyplot as plt
labels = 'Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'
sizes = [73,42,38,28,22,19,18,12,8,7]
explode = (0,0,0,0,0,0,0,0,0,0)
colors = ['azure','lightcyan','paleturquoise','c','darkcyan','darkslategray','darkgreen','g','forestgreen','lightgreen']
# Specifies the fraction of the radius with which to offset each wedge.
plt.pie(sizes, explode = explode,labels = labels,autopct = '%1.1f%%',shadow = False,startangle = 90,colors = colors)
plt.axis('equal')
plt.show()

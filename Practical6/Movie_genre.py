# Create a dictionary with the movie genre and their number of studentsfor which this genre is their favorite
Movie_genre = {'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8}
# Add the last movie genre into the dictionary
Movie_genre['War'] = 7
# Print the dictionary of Movie genre
print(Movie_genre)
# Input a kink of movie genre and output the corresponding number.
input = 'Comedy'
print(Movie_genre[input])

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

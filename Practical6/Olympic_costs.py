# Create a list that contain the cost of each Olympic games, print the cost of the input one.
costs = [1,8,15,7,5,14,43,40]
costs = sorted(costs)
print(costs)

# Import the matplotlib and numpy.
import numpy as np
import matplotlib.pyplot as plt
N = 8
# Sort the costs and make the host cities' names shown in the same order.
olympics = [LosAngeles_1984,Seoul_1988,Barcelona_1992,Atlanta_1996,Sydney_2000,Athens_2003,Beijing_2008,London_2012]
costs = [1,8,15,7,5,14,43,40]
olympics = np.array(olympics)
costs = np.array(costs)
inds = costs.argsort()
sortedolympics = olympics[inds]
sortedcosts = costs[inds]
ind = np.arrange(N)
width = 0.35
# Draw a bar plot using the sorted data.
p1 = plt.bar(ind, sortedcosts, width)
plt.ylabel('Cost')
plt.title('Olympic_Costs')
plt.xticks(ind,sortedolympics)
plt.yticks(np.arrange(0,50,5))
plt.show()

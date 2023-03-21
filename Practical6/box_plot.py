import numpy as np
import matplotlib.pyplot as plt
N = 8
cost = (1,8,15,7,5,14,43,40)
ind = np.arrange(N)
width = 1.0
p1 = plt.bar(ind, scores, width)
plt.ylabel('Cost')
plt.title('Olympic Costs')
plt.xticks(ind,(LosAngeles1984,Seoul1988,Barcelona1992,Atlanta1996,Sydney2000,Athens2003,Beijing2008,London2012)
plt.yticks(np.arrange(0,50,5)
plt.show()


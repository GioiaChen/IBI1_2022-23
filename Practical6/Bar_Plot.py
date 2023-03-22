import numpy as np
import matplotlib.pyplot as plt
N = 8
cost = (1,8,15,7,5,14,43,40)
ind = np.arrange(N)
width = 0.35
p1 = plt.bar(ind, scores, width)
plt.ylabel('Cost')
plt.title('Olympic_Costs')
plt.xticks(ind,('LosAngeles_1984','Seoul_1988','Barcelona_1992','Atlanta_1996','Sydney_2000','Athens_2003','Beijing_2008','London_2012'))
plt.yticks(np.arrange(0,50,5))
plt.show()

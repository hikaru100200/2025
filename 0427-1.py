import matplotlib.pyplot as plt

listx = [5,8,6,7,12]
listy = [36,55,78,12,66]

plt.plot(listx,listy,marker='s',linestyle='-',color='yellow',linewidth=1,markersize=20)
plt.title('test')
plt.xlabel('degree')
plt.ylabel('day')

plt.show()
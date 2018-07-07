import matplotlib.pyplot as plt

inputs = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]
x, y = zip(*inputs)

plt.xlabel('block east of city center')
plt.ylabel('blocks north of city center')
plt.title('User Locations')
plt.plot(x, y, '.')
plt.show()

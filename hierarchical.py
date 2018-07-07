base_cluster = bottom_up_cluster(inputs)

three_clusters = [get_values(cluster) for cluster in generate_clusters(base_cluster, 3)]
for i ,cluster, marker, color in zip ([1,2,3], three_clusters, ['D','0','*'], ['r','g','b']):
	xs, ys = zip(*cluster)
	plt.scatter(xs,ys,color = color,)
	x, y = vector_mean(cluster)
	plt.xlabel('block east of city center')
	plt.ylabel('blocks north of city center')
	plt.plot(x,y,marker='$'+str(i)+'$',color='black')
plt.show()





base_cluster = bottom_up_cluster(inputs, max)

three_clusters = [get_values(cluster) for cluster in generate_clusters(base_cluster, 3)]
for i ,cluster, marker, color in zip ([1,2,3], three_clusters, ['D','0','*'], ['r','g','b']):
	xs, ys = zip(*cluster)
	plt.scatter(xs,ys,color = color,)
	x, y = vector_mean(cluster)
	plt.xlabel('block east of city center')
	plt.ylabel('blocks north of city center')
	plt.plot(x,y,marker='$'+str(i)+'$',color='black')
plt.show()

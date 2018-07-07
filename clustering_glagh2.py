
from __future__ import division
import math, random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random

#def distance(x1, y1, x2, y2):
def distance(a, b):
	x1 = a[0]
	y1 = a[1]
	x2 = b[0]
	y2 = b[1]
	d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	return d
	
def divide(a, b, c):
	for i in range(n):
		m = 200
		if distance(a, sample[i]) < m:
			m = distance(a, sample[i])
			colorlist[i] = "blue"
		if distance(b, sample[i]) < m:
			m = distance(b, sample[i])
			colorlist[i] = "red"
		if distance(c, sample[i]) < m:
			m = distance(c, sample[i])
			colorlist[i] = "green"

sample = [[-14,-5],[13,13],[20,23],[-19,-11],[-9,-16],[21,27],[-49,15],[26,13],[-46,5],[-34,-1],[11,15],[-49,0],[-22,-16],[19,28],[-12,-8],[-13,-19],[-41,8],[-11,-6],[-25,-9],[-18,-3]]

colorlist = []

n = len(sample)
k = 3


#for i in range(n):
#	sample.append([random.random(),random.random()])

#print sample

x, y = zip(*sample)



for i in range(n):
	colorlist.append("black")

rli = random.sample(range(n), 3)
print(rli)
	
colorlist[rli[0]] = "blue"
colorlist[rli[1]] = "red"
colorlist[rli[2]] = "green"
	
plt.scatter(x, y, marker = 'o', c = colorlist)
plt.plot()

#print(sample[1])

plt.show()

		
divide(sample[rli[0]], sample[rli[1]], sample[rli[2]])

plt.scatter(x, y, marker = 'o', c = colorlist)
plt.plot()
plt.show()

past = list(colorlist)

#loop
while 1:

	#blue
	count = 0
	xn = 0
	yn = 0
	for i in range(n):
		if colorlist[i] == "blue":
			count = count + 1
			xn = xn + sample[i][0]
			yn = yn + sample[i][1]
	bx = xn / count
	by = yn / count

	#red
	count = 0
	xn = 0
	yn = 0
	for i in range(n):
		if colorlist[i] == "red":
			count = count + 1
			xn = xn + sample[i][0]
			yn = yn + sample[i][1]
	rx = xn / count
	ry = yn / count

	#green
	count = 0
	xn = 0
	yn = 0
	for i in range(n):
		if colorlist[i] == "green":
			count = count + 1
			xn = xn + sample[i][0]
			yn = yn + sample[i][1]
	gx = xn / count
	gy = yn / count
	
	plt.scatter(bx, by, marker = 'x', c = "blue")
	plt.scatter(rx, ry, marker = 'x', c = "red")
	plt.scatter(gx, gy, marker = 'x', c = "green")
	plt.scatter(x, y, marker = 'o', c = colorlist)
	plt.plot()
	plt.show()
	divide([bx,by], [rx,ry], [gx,gy])
	
	if past == colorlist:
		break
	past = list(colorlist)
	
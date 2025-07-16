import matplotlib.pyplot as plt
l =('python','scala','c#','java')
index = (1,2,3,4)
size =[40,17,35,29]
plt.bar(index,size,color='blue',tick_label = l)
plt.ylabel('usages')
plt.xlabel('languages')
plt.show()
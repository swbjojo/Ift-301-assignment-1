import matplotlib.pyplot as plt
categories= ['Mushroom','Pineapple','Prawns','Sausage','Spinach']
values = [0.17, 0.3, 0.085, 0.19, 0.3]


plt.barh(categories, values, color='blue')

plt.title('Bar Chart')
plt.xlabel('Proportion of Total')
plt.ylabel('Categories')
 
plt.show()


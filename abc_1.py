import matplotlib.pyplot as plt
import pandas as pd
a = pd.read_csv('ss.csv')
d=pd.DataFrame(a)
x = d['name']
y = d['age']
plt.bar(x,y,label='employee data', color='red')
plt.xlabel('emp name')
plt.ylabel('emp age')
plt.title('my company')
plt.legend()
plt.show()
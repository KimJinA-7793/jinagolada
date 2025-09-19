import matplotlib.pyplot as plt

season = ['spring', 'summer', 'autumn', 'winter']
corona = [300, 800, 600, 1200]

plt.title('corona status by season')
plt.xlabel('season')
plt.ylabel('corona')
plt.plot(season, corona, color = 'red', label = 'corona')
plt.legend()
plt.show()

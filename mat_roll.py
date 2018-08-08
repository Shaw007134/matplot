import matplotlib.pyplot as plt
from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)
	
frequencies = []	

max_result = die1.num_sides + die2.num_sides
x_values = range(2,max_result+1)

for value in x_values:
	frequency = results.count(value)
	frequencies.append(frequency)

# the x locations for the group
ind = x_values
plt.xticks(ind,x_values)
plt.axhline(100, linewidth=3, color='r')

plt.bar(x_values, frequencies, align="center", width=0.7)
plt.title("Roll the dice 100 times", fontsize=24)
plt.xlabel("Side", fontsize=14)
plt.ylabel("Frequency", fontsize=14)


plt.show()

	
	


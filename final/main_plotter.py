import matplotlib.pyplot as plt
import plotter as pl
states = []
no_of_simulations = 0
total = 0
with open("output.txt") as file:
    data = file.readlines()
    simulations = data[-2]
    data = data[2:-3]

    for d in data:
        l = d.split(": ")
        value = int(l[1].strip("/n"))
        total += value
        states.append([l[0],value])
        

for state in states:
    state[1] = state[1]/total * 100

sorted_data = sorted(states, key=lambda x: x[1], reverse=True)
x_axis = [i[0] for i in sorted_data];
y_axis = [i[1] for i in sorted_data]

value = 0
for val in range(19,len(y_axis)):
    value += y_axis[val]

x_axis = [x_axis[i] for i in range(19)];x_axis.append("Others")
y_axis = [y_axis[i] for i in range(19)];y_axis.append(value)

plt.figure(figsize=(16, 8))
plt.subplot(1,2,1)
plt.pie(y_axis, labels=x_axis)

plt.subplot(1,2,2)
plt.bar(x_axis[:5], y_axis[:5], color='skyblue')
plt.xlabel('State names')
plt.ylabel('Pivotal player')
plt.title('Shabley Shubik Index')
plt.ylim(0, 100)

plt.tight_layout()
plt.show()
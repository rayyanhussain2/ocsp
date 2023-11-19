import random
import matplotlib.pyplot as plt

class State:
    def __init__(self, name, key, weight):
        self.name = name
        self.key = key
        self.weight = weight

def main(permutations):
    states = [
        State("Andhra Pradesh", 0, 25),
        State("Arunachal Pradesh", 0, 2),
        State("Assam", 0, 14),
        State("Bihar", 0, 40),
        State("Chhattisgarh", 0, 11),
        State("Goa", 0, 2),
        State("Gujarat", 0, 26),
        State("Haryana", 0, 10),
        State("Himachal Pradesh", 0, 4),
        State("Jharkhand", 0, 14),
        State("Karnataka", 0, 28),
        State("Kerala", 0, 20),
        State("Madhya Pradesh", 0, 29),
        State("Maharashtra", 0, 48),
        State("Manipur", 0, 2),
        State("Meghalaya", 0, 2),
        State("Mizoram", 0, 1),
        State("Nagaland", 0, 1),
        State("Odisha", 0, 21),
        State("Punjab", 0, 13),
        State("Rajasthan", 0, 25),
        State("Sikkim", 0, 1),
        State("Tamil Nadu", 0, 39),
        State("Telangana", 0, 17),
        State("Tripura", 0, 2),
        State("Uttar Pradesh", 0, 80),
        State("Uttarakhand", 0, 5),
        State("West Bengal", 0, 42),
        State("Andaman and Nicobar Islands", 0, 1),
        State("Chandigarh", 0, 1),
        State("Dadra and Nagar Haveli and Daman and Diu", 0, 2),
        State("Jammu and Kashmir", 0, 5),
        State("Ladakh", 0, 1),
        State("Lakshadweep", 0, 1),
        State("Delhi", 0, 7),
        State("Puducherry", 0, 1),
    ]
    size = 36
    simulations = 0
    majority = 272

    print("Running simulation...")

    #Permute
    for i in range(permutations):
        #Shuffle
        for j in range(size):
            randomIndex = random.randint(0, size - 1)
            #Swap
            states[j].key, states[randomIndex].key = states[randomIndex].key, states[j].key
            states[j].weight, states[randomIndex].weight = states[randomIndex].weight, states[j].weight
            states[j].name, states[randomIndex].name = states[randomIndex].name, states[j].name

        #incrementPivot
        sumWeights = 0
        for j in range(size):
            sumWeights += states[j].weight
            if sumWeights >= majority:
                states[j].key += 1
                break
        simulations += 1

    # Post-computation tasks
    print("Simulation completed!")
    print("Total simulations:", permutations)
    return states

def plotter(states,permutations):
    for state in states:
        state.key = state.key/permutations * 100

        sorted_data = sorted(states, key=lambda x: x.key, reverse=True)
        x_axis = [i.name for i in sorted_data]
        y_axis = [i.key for i in sorted_data]

        value = 0
    for val in range(19,len(y_axis)):
        value += y_axis[val]

    x_axis = [x_axis[i] for i in range(19)];x_axis.append("Others")
    y_axis = [y_axis[i] for i in range(19)];y_axis.append(value)

    plt.figure(figsize=(16, 8))
    plt.subplot(1,2,1)
    plt.pie(y_axis, labels=x_axis)

    plt.subplot(1,2,2)
    bars = plt.bar(x_axis[:5], y_axis[:5], color='skyblue')
    plt.xlabel('State names')
    plt.ylabel('Pivotal player')
    plt.title('Shabley Shubik Index')
    plt.ylim(0, 100)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 2, round(yval, 2), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


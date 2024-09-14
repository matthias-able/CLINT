import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

atoms = ['I',
    'C', 'H', 'H', 'H', 'O', 'C', 'H', 'H', 'C', 'H', 'H', 'O',
    'C', 'H', 'H', 'C', 'H', 'H', 'N', 'C', 'H', 'N', 'C', 'H',
    'C', 'H', 'C', 'H', 'H', 'C', 'H', 'H', 'O', 'C', 'H', 'H',
    'C', 'H', 'H', 'O', 'C', 'H', 'H', 'H'
]

ions = [46, 274, 148, 280, 390, 648]


RESP_charges = []
for ion in ions:

    path = f"/home/matthiasable/automated_test_run/plus{ion}"

    # Read the contents of the file
    with open(f'{path}/qout_stage2', 'r') as file:
        data = file.read()

    # Split the data by whitespace to extract individual charges
    charges = [float(num) for num in data.split()]

    # Convert the list of charges into a NumPy array
    charges = np.array(charges)
    RESP_charges.append(charges)



fig, ax = plt.subplots()

x = np.arange(len(ions))
label = True
for ion in ions:
    iodid = RESP_charges[ions.index(ion)][0] #iod
    kette0 = np.sum(RESP_charges[ions.index(ion)][1:19]) #kette
    ring = np.sum(RESP_charges[ions.index(ion)][19:27]) #ring
    kette1 = np.sum(RESP_charges[ions.index(ion)][27:]) #kette
    if label:
        ax.plot(x[ions.index(ion)], iodid, 'x', color = 'black', label = 'Iodid')
        ax.plot(x[ions.index(ion)], kette0, 'x', color = 'blue', label = 'Kette0')
        ax.plot(x[ions.index(ion)], ring, 'x', color = 'red', label = 'Ring')
        ax.plot(x[ions.index(ion)], kette1, 'o', alpha = 0.4, color = 'purple', label = 'Kette1')
        label = False
    ax.plot(x[ions.index(ion)], iodid, 'x', color = 'black')
    ax.plot(x[ions.index(ion)], kette0, 'x', color = 'blue')
    ax.plot(x[ions.index(ion)], ring, 'x', color = 'red')
    ax.plot(x[ions.index(ion)], kette1, 'o', alpha = 0.4, color = 'purple')


# Set x-ticks and x-tick labels to the atom list
ions = ['46', '274', '148', '280', '390', '648']
plt.xticks(x, ions)
#ax.set_xticklabels(ions)#, rotation=90)  # Rotate labels if they overlap


# Set labels for the x and y axes
ax.set_xlabel('Ions')
ax.set_ylabel('Sum of RESP charges [e] ')
ax.legend()

# Save the plot
plt.savefig('plot.png')
#plt.show()

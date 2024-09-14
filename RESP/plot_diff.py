import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

atoms = [
    'C', 'H', 'H', 'H', 'O', 'C', 'H', 'H', 'C', 'H', 'H', 'O',
    'C', 'H', 'H', 'C', 'H', 'H', 'N', 'C', 'H', 'N', 'C', 'H',
    'C', 'H', 'C', 'H', 'H', 'C', 'H', 'H', 'O', 'C', 'H', 'H',
    'C', 'H', 'H', 'O', 'C', 'H', 'H', 'H'
]


# data copied of qout_stage2 files in corresponing directories
only = np.array([-0.194143, 0.127851, 0.127851, 0.127851, -0.336656, -0.052912, 0.101757, 0.101757
        , 0.179486, 0.030379, 0.030379, -0.370131, 0.113016, 0.059477, 0.059477, -0.077154
        , 0.102088, 0.102088, 0.101269, -0.068733, 0.253906, 0.101269, -0.203436, 0.277119
        , -0.203436, 0.277119, -0.077154, 0.102088, 0.102088, 0.113016, 0.059477, 0.059477
        , -0.370131, 0.179486, 0.030379, 0.030379, -0.052912, 0.101757, 0.101757, -0.336656
        , -0.194143, 0.127851, 0.127851,  0.127851])


full3 = np.array([ -0.182291, 0.121174, 0.121174, 0.121174, -0.331946, -0.057286,  0.097628,  0.097628,
  0.180814, 0.037618, 0.037618, -0.389509, -0.028345, 0.088001, 0.088001, 0.077141,
  0.083299, 0.083299, 0.060131, -0.014876, 0.266484, 0.060131, -0.225159, 0.294030,
 -0.225159, 0.294030, 0.077141, 0.083299, 0.083299, -0.028345, 0.088001, 0.088001,
 -0.389509, 0.180814, 0.037618, 0.037618, -0.057286, 0.097628, 0.097628, -0.331946,
 -0.182291, 0.121174, 0.121174, 0.121174])


plus148 = np.array([-0.923177,-0.020696,0.075104,0.075104,0.075104,-0.332603,-0.138400,0.109497
,0.109497,0.314057,-0.002921,-0.002921,-0.384371,-0.052943,0.103463,0.103463
,0.033195,0.072358,0.072358,0.080890,-0.047409,0.256780,0.080890,-0.204063
,0.271731,-0.204063,0.271731,0.033195,0.072358,0.072358,-0.052943,0.103463
,0.103463,-0.384371,0.314057,-0.002921,-0.002921,-0.138400,0.109497,0.109497
,-0.332603,-0.020696,0.075104,0.075104,0.075104])

plus148 = plus148[1:]


plus280 = np.array([-0.915227,-0.140948,0.107116,0.107116,0.107116,-0.298767,-0.082731,0.080808
,0.080808,0.334349,-0.013606,-0.013606,-0.408058,0.056766,0.074356,0.074356
,0.037902,0.055624,0.055624,0.069207,-0.088294,0.237793,0.069207,-0.147937
,0.247369,-0.147937,0.247369,0.037902,0.055624,0.055624,0.056766,0.074356
,0.074356,-0.408058,0.334349,-0.013606,-0.013606,-0.082731,0.080808,0.080808
,-0.298767,-0.140948,0.107116,0.107116,0.107116])

plus280 = plus280[1:]




diff = only - full3

set_to_compare = full3

label = 'full'




fig, ax = plt.subplots()
    
# Dictionary to hold colors for each atom type
colors = {
    'C': 'black',
    'H': 'blue',
    'O': 'red',
    'N': 'green'
}

# Iterate over each atom and corresponding diff value to plot
for i, (atom, value) in enumerate(zip(atoms, diff)):
    color = colors.get(atom, 'grey')  # Default to blue if atom type is not in colors dictionary
    ax.plot(i, value, 'o', color=color)

    if i == 0:
        ax.plot(i, only[i], 'x', color='grey', label = 'only')
        ax.plot(i, set_to_compare[i], 'x', color='purple', label = label)
    else:
        ax.plot(i, only[i], 'x', color='grey')
        ax.plot(i, set_to_compare[i], 'x', color='purple')


ax.hlines(0, 0, 44, color = 'grey', linestyle = 'dashed')

# Set x-ticks and x-tick labels to the atom list
ax.set_xticks(range(len(atoms)))
ax.set_xticklabels(atoms)#, rotation=90)  # Rotate labels if they overlap

# Set labels for the x and y axes
ax.set_xlabel('Atoms')
ax.set_ylabel('Diff of RESP charges [e]')

# Create custom legend
legend_elements = [Line2D([0], [0], marker='o', color='w', label=atom, markerfacecolor=color) for atom, color in colors.items()]
leg1 = ax.legend(handles=legend_elements, title='Atom Types')
ax.add_artist(leg1)

ax.legend()
# Display the plot
plt.savefig(label)
plt.show()

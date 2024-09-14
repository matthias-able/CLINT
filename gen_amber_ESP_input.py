import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse


parser = argparse.ArgumentParser(description='Process log file and output XYZ coordinates.')
parser.add_argument('input_file', type=str, help='Path to the g16 log file')
args = parser.parse_args()

# Path to log file
log_file_path = args.input_file


# Function to extract coordinates from log file
def extract_molecule_coordinates(file_path):
    pattern = r'Atomic Center\s+(\d+)\s+is at\s+(-?\d+\.\d+)\s*(-?\d+\.\d+)\s*(-?\d+\.\d+)'
    coordinates = []

    pattern2 = r'\s+(\d+)+\s+(\d+)\s+\d+\s+-?\d*\.?\d+\s+-?\d*\.?\d+\s+-?\d*\.?\d+'
    section_dist_m = True
    map_center_to_atom_number = []

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            match2 = re.search(pattern2, line)

            # look for coodinates
            if match:
                center_nb, x, y, z = match.groups()
                coordinates.append([int(center_nb), float(x), float(y), float(z)]) #in Angstrom 

            # stop searching form pattern2 when distance matrix is reached in file     
            if 'Distance matrix (angstroms)' in line:
                section_dist_m = False  
            # look for atomic numbers
            if match2 and section_dist_m:
                center_nb, atomic_number = match2.groups()
                map_center_to_atom_number.append([int(center_nb), int(atomic_number)])
        map_center_to_atom_number = np.array(map_center_to_atom_number)

    # replace atomic center with atomic number    
    for row in coordinates:
        index = np.where(row[0] == map_center_to_atom_number[:,0])[0][0]
        row[0] = map_center_to_atom_number[index][1]
    return coordinates
    
    
# Function to extract coordinates from log file
def extract_ESP_coordinates(file_path):
    pattern = r'ESP Fit Center\s+[\d\*]+ is at\s+(-?\d+\.\d+)\s*(-?\d+\.\d+)\s*(-?\d+\.\d+)'
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                x, y, z = map(float, match.groups())
                coordinates.append((x, y, z))
    coordinates = np.array(coordinates) # in Angstrom
    print(coordinates.shape)                    
    return coordinates
    

# Function to extract fit values from log file
def extract_ESP_values(file_path):
    pattern = r'\s+[\d\*]+\s+Fit\s+(-?\d+\.\d+)'
    values = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                value = float(match.groups()[0])
                values.append(value)
    values = np.array(values)
    print(values.shape)               
    return values


# Write coordinates to file in XYZ format
def write_coordinates_to_xyz(coordinates, output_file, esp = False):
    '''
    esp = True: write He to first coloum
    '''
    with open(output_file, 'w') as file:
        file.write(str(len(coordinates)) + '\n' + '\n')
        if esp:
            for x, y, z in coordinates:
                file.write(f"{2}    {round(x, 11)}    {round(y, 11)}    {round(z, 11)}\n") 
        else:
            for atom_n, x, y, z in coordinates:
                file.write(f"{atom_n}    {round(x, 11)}    {round(y, 11)}    {round(z, 11)}\n")        
            


# create mask to find high layer atoms in atomic fit centers
def create_mask(file_path):

    with open(file_path, 'r') as file:
        start = False
        stop = False
        mask = []

        for line in file:
            # start at Symbolic Z-matrix:
            if line[0:7] == ' Charge' and not stop:
                start = True
                # print(line[:])
            
            if start and line == ' \n':
                stop = True

            if len(line) > 56 and start and not stop:
                print(line)
                if line[57] == 'H':
                    mask.append(True)
                elif line[57] == 'L':
                    mask.append(False)
    # print(mask)
    return mask


def format_to_scientific_notation(value):
    '''
    Converts value to Bohr
    Format with 7 digits and space if non negative
    '''
    value *= 1.8897259886 # convert ot Bohr
    formatted_value = f"{value:.7E}"
    if not formatted_value.startswith('-'):
        formatted_value = ' ' + formatted_value
    return formatted_value


# Write esp file
def write_esp_file(coordinates, mask, esp_coordinates, values, output_file):
    '''
    write .esp file like amber does
    coordinates in bohr
    '''
    with open(output_file, 'w') as file:
        file.write('   44' + str(len(esp_coordinates)) + '    0' + '\n')
        # this calculation is maybe still wrong
        

        for coord, mask_value in zip(coordinates, mask):
            (atom_n, x, y, z) = coord
            if mask_value:
                x, y, z = format_to_scientific_notation(x), format_to_scientific_notation(y), format_to_scientific_notation(z)
                file.write(f"                  {x}  {y}  {z} \n") 
        
        
        for value, coord in zip(values, esp_coordinates):
            (x, y, z) = coord
            x, y, z = format_to_scientific_notation(x), format_to_scientific_notation(y), format_to_scientific_notation(z)
            file.write(f"   {value:.7E}  {x}  {y}  {z} \n")  


# Main function to plot 3D scatter plot
def plot_coordinates(mol_coordinates, ESP_coordinates):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x_mol = [coord[1] for coord in mol_coordinates]
    y_mol = [coord[2] for coord in mol_coordinates]
    z_mol = [coord[3] for coord in mol_coordinates]
    
    x_ESP = [coord[0] for coord in ESP_coordinates]
    y_ESP = [coord[1] for coord in ESP_coordinates]
    z_ESP = [coord[2] for coord in ESP_coordinates]
            
    ax.scatter(x_mol[0], y_mol[0], z_mol[0], color = 'red', label='atom 0 - Iodin')
    # ax.scatter(x_mol[1], y_mol[1], z_mol[1], color = 'red', label='atom 1 - Iodin')
    ax.scatter(x_mol[1:], y_mol[1:], z_mol[1:], color = 'black')
    # ax.scatter(x_mol[2:], y_mol[2:], z_mol[2:], color = 'black')
    ax.scatter(x_ESP, y_ESP, z_ESP, color = 'tab:red', s=2, alpha=0.1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show()




# Extract coordinates from log file
mol_coordinates = extract_molecule_coordinates(log_file_path)
ESP_coordinates = extract_ESP_coordinates(log_file_path)
ESP_values = extract_ESP_values(log_file_path)

# Write coordinates to XYZ file
# write_coordinates_to_xyz(ESP_coordinates, f'{log_file_path[:-4]}_ESP_coordinates.xyz', esp=True)
# write_coordinates_to_xyz(mol_coordinates, f'{log_file_path[:-4]}_mol_coordinates.xyz')
mask = create_mask(log_file_path)
write_esp_file(mol_coordinates, mask, ESP_coordinates, ESP_values, output_file = f'{log_file_path[:-4]}_python.esp')



# Plot coordinates in a 3D scatter plot
plot_coordinates(mol_coordinates, ESP_coordinates)


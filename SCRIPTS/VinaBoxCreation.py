import re
import os
import subprocess
from SCRIPTS.paths import ADFRsuite_PATH
CURRENT_DIR = os.getcwd()


def vinaBoxCreation():
    # Read the the protein file that ends with pdbqt from the Protein_prepared folder
    protein_files = [f for f in os.listdir(os.path.join(
        CURRENT_DIR, 'OUTPUTS', 'Protein_prepared')) if f.endswith('.pdbqt')]

    if len(protein_files) == 0:
        raise Exception(
            'No prepared protein file found in Protein_prepared folder.')
    elif len(protein_files) > 1:
        raise Exception(
            'Multiple prepared protein files found in Protein_prepared folder.')
    else:
        protein_path = os.path.join(
            CURRENT_DIR, 'OUTPUTS', 'Protein_prepared', protein_files[0])

    # Read the ligand file from the Ligand_prepared folder
    ligand = os.listdir(os.path.join(
        CURRENT_DIR, 'OUTPUTS', 'Ligand_prepared'))
    ligand_path = os.path.join(CURRENT_DIR, 'OUTPUTS',
                               'Ligand_prepared', ligand[0])

    # change the working directory to the protein_prepared folder
    os.chdir(os.path.join(CURRENT_DIR, 'OUTPUTS', 'Protein_prepared'))

    # Run prepare_gpf.py script to generate the .gpf file
    subprocess.run([os.path.join(ADFRsuite_PATH, 'bin', 'pythonsh'), f'{CURRENT_DIR}/SCRIPTS/prepare_gpf.py', '-r', protein_path, '-l',
                   ligand_path, '-o', f'{CURRENT_DIR}/OUTPUTS/vina_box/{protein_files[0][:-6]}.gpf', '-y'])

    # change the working directory to the vina_box folder
    os.chdir(os.path.join(CURRENT_DIR, 'OUTPUTS', 'vina_box'))

    # Read lines from text file that ends with .gpf
    with open(f"{protein_files[0][:-6]}.gpf", "r") as f:
        lines = f.readlines()

    # Join lines into a single text string
    text = ''.join(lines)

    # Extract xyz-coordinates
    pattern = r'gridcenter\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)'
    matches = re.findall(pattern, text)

    # extracte the xyz-coordinates
    for match in matches:
        center_x = match[0]
        center_y = match[1]
        center_z = match[2]

    # write the extracted xyz-coordinates to a text file
    with open(f"vina_box.txt", "w") as f:
        f.write(f'center_x = {center_x}\n')
        f.write(f'center_y = {center_y}\n')
        f.write(f'center_z = {center_z}\n')
        f.write(f'size_x = 20\n')
        f.write(f'size_y = 20\n')
        f.write(f'size_z = 20\n')

    # change the working directory back to the current directory
    os.chdir(CURRENT_DIR)

    # print vina box creation success message with xyz coordinates and bix size
    print(f"\nVina box created successfully with the following parameters:\n"
          f"center_x = {center_x}\n"
          f"center_y = {center_y}\n"
          f"center_z = {center_z}\n"
          f"size_x = 20\n"
          f"size_y = 20\n"
          f"size_z = 20\n")


if __name__ == "__main__":
    vinaBoxCreation()

import os
import subprocess

# get the current path
CURRENT_PATH = os.getcwd()


def ligandPreparation():
    # Check if the Ligand folder exists
    if not os.path.exists(os.path.join(CURRENT_PATH, 'INPUTS', 'Ligand')):
        # raise an error if the folder does not exist
        raise Exception(
            'Ligand folder does not exist. Please create a "Ligand" folder in the current directory then add your ligands to it.')
    else:
        # check if Ligands folder contains ligand
        if len(os.listdir(os.path.join(CURRENT_PATH, 'INPUTS', 'Ligand'))) == 0:
            # raise an error if the Ligands folder is empty
            raise Exception(
                'Ligand folder is empty. Please add your ligand(s) to the Ligand folder.')
        else:
            # get the list of ligands in the Ligands folder
            ligands = os.listdir(os.path.join(
                CURRENT_PATH, 'INPUTS', 'Ligand'))
            for ligand in ligands:
                # check if the ligand is sdf file
                if ligand.endswith('.sdf'):
                    # get the ligand path
                    ligand_path = os.path.join(
                        CURRENT_PATH, 'INPUTS', 'Ligand', ligand)
                    # get path for the output file
                    output_path = os.path.join(
                        CURRENT_PATH, 'OUTPUTS', 'Ligand_prepared', f"{ligand[:-4]}_H_charged.pdbqt")
                    # run obabel from the command line to add hydrogen and charge to the ligand
                    subprocess.run(
                        ['obabel', '-isdf', ligand_path, '-O', output_path, '-h', '-p', '-r'])


if __name__ == "__main__":
    ligandPreparation()

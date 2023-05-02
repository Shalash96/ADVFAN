import os
import subprocess
from SCRIPTS.paths import VINA_PATH


def dockingVina(exhaustiveness='8', num_modes='9', energy_range='3'):
    # get the current path
    CURRENT_PATH = os.getcwd()

    # get the path of the receptor from protein_prepared folder
    protein_files = [f for f in os.listdir(os.path.join(
        CURRENT_PATH, 'OUTPUTS', 'Protein_prepared')) if f.endswith('.pdbqt')]

    # make sure that there is only one protein in the protein_prepared folder with the pdbqt extension
    if len(protein_files) != 1:
        raise Exception(
            'Protein folder is empty or contains more than one protein. It should contain only one protein with the pdbqt extension')

    PROTEIN = os.path.join(CURRENT_PATH, 'OUTPUTS',
                           'Protein_prepared', protein_files[0])

    # get the list of the ligands from ligand_prepared folder
    LIGANDS_PATH = os.path.join(CURRENT_PATH, 'OUTPUTS', 'Ligand_prepared')
    LIGANDS = os.listdir(os.path.join(
        CURRENT_PATH, 'OUTPUTS', 'Ligand_prepared'))

    # get the path of the vina box from vina_box folder
    VINA_BOX = os.path.join(CURRENT_PATH, 'OUTPUTS',
                            'vina_box', 'vina_box.txt')

    # performing docking for each ligand
    for ligand in LIGANDS:
        if ligand.endswith('.pdbqt'):
            ligand_path = os.path.join(LIGANDS_PATH, ligand)
            output_path = os.path.join(
                CURRENT_PATH, 'OUTPUTS', 'Docking_results', f"{ligand[:-6]}_poses.pdbqt")
            print(
                f"Docking of {ligand[:-6]} to the {protein_files[0]} started. Please wait...")
            with open(os.path.join(CURRENT_PATH, 'OUTPUTS', 'Docking_results', f"{ligand[:-6]}_docking_summary.txt"), 'w') as f:

                f.write("""\n\n
########################################################################################################################################################                
#               This docking process was run through AutoDock Vina For Absolute Noobs scripts'ADVFAN'                                                  #
#               These scripts are a wrapper for AutoDock Vina, AutoDock Tools and openbabel to simplify the docking process for beginners.             #
#               They are written by: Mahmoud Shalash ===>  https://twitter.com/__shalash__                                                             #
#               The code is available on my GitHub:  ===>  https://github.com/Shalash96                                                                #
########################################################################################################################################################""")

                subprocess.run([VINA_PATH, '--receptor', PROTEIN, '--ligand', ligand_path,
                                '--config', VINA_BOX, '--out', output_path,
                                '--exhaustiveness', exhaustiveness, '--num_modes', num_modes, '--energy_range', energy_range], stdout=f)

            print(
                f"Docking of {ligand} to the {protein_files[0]} finished.")


if __name__ == "__main__":
    dockingVina(exhaustiveness='8', num_modes='9', energy_range='3')

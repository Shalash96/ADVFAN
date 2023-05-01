import os
import subprocess


def dockingVina():
    # get the current path
    CURRENT_PATH = os.getcwd()
    # get the path of the vina executable
    VINA_PATH = os.path.join(CURRENT_PATH, 'ADFRsuite-1.0', 'bin', 'vina')

    # get the path of the receptor from protein_prepared folder
    protein_files = [f for f in os.listdir(os.path.join(
        CURRENT_PATH, 'OUTPUTS', 'Protein_prepared')) if f.endswith('.pdbqt')]

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
                CURRENT_PATH, 'OUTPUTS', 'Docking_results', f"{ligand[:-6]}_docked.pdbqt")
            # subprocess.run([VINA_PATH, '--receptor', PROTEIN, '--ligand', ligand_path,
            #                 '--config', VINA_BOX, '--out', output_path,
            #                 '--exhaustiveness', '8', '--num_modes', '9', '--energy_range', '3'])
            # write the docking results print on the terminal screen to a file
            # print to the terminal screen that the docking is running
            print(
                f"Docking of {ligand[:-6]} to the {protein_files[0]} started. Please wait...")
            with open(os.path.join(CURRENT_PATH, 'OUTPUTS', 'Docking_results', f"{ligand[:-6]}_docking_results.txt"), 'w') as f:

                f.write("""\n\n
########################################################################################################################################################                
#               This docking process was run through AutoDock Vina For Absolute Noobs scripts'ADVFAN'                                                  #
#               These scripts are a wrapper for AutoDock Vina, AutoDock Tools and openbabel to simplify the docking process for beginners.             #
#               They are written by: Mahmoud Shalash ===>  https://twitter.com/__shalash__                                                             #
#               The code is available on my GitHub:  ===>  https://github.com/Shalash96                                                                #
########################################################################################################################################################""")

                subprocess.run([VINA_PATH, '--receptor', PROTEIN, '--ligand', ligand_path,
                                '--config', VINA_BOX, '--out', output_path,
                                '--exhaustiveness', '8', '--num_modes', '9', '--energy_range', '3'], stdout=f)
            # print to the terminal screen that the docking is finished
            print(
                f"Docking of {ligand} to the {protein_files[0]} finished.")


if __name__ == "__main__":
    dockingVina()

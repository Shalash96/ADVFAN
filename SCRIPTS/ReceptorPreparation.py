import pymol
import subprocess
import os


# get the current path
CURRENT_PATH = os.getcwd()


def clean_pdb(input_dir, output_dir, filename, chain='A'):
    # Load the file and the name of the chain to keep
    pymol.cmd.load(os.path.join(input_dir, filename))
    # Remove all HETATM records
    pymol.cmd.remove('hetatm')
    # Remove all solvent
    pymol.cmd.remove('solvent')
    # Remove all all chains except A
    pymol.cmd.remove(f'not chain {chain}')
    # Save the file
    output_file = os.path.join(output_dir, f"{filename[:-4]}_clean.pdb")
    pymol.cmd.save(output_file)
    return output_file


def receptorPreparation():
    # Check if the Ligand folder exists
    if not os.path.exists(os.path.join(CURRENT_PATH, 'INPUTS', 'Protein')):

        # # raise an error if the folder does not exist
        raise Exception(
            'Protein folder does not exist. Please create a "Protein" folder in the current directory then add your protein to it.')
    else:
        # check if Protein folder contains only one protein
        if len(os.listdir(os.path.join(CURRENT_PATH, 'INPUTS', 'Protein'))) != 1:
            # raise an error if the Protein folder is empty
            raise Exception(
                'Protein folder is empty or contains more than one protein.')
        else:
            # get the list of proteins in the Protein folder
            proteins = os.listdir(os.path.join(
                CURRENT_PATH, 'INPUTS', 'Protein'))
            for protein in proteins:
                # check if the protein is pdb file
                if protein.endswith('.pdb'):
                    # run clean_pdb function to clean the protein and save it to the Protein_prepared folder
                    cleaned_pdb = clean_pdb(os.path.join(CURRENT_PATH, 'INPUTS', 'Protein'), os.path.join(
                        CURRENT_PATH, 'OUTPUTS', 'Protein_prepared'), protein, chain='A')

                    # run obabel from the command line to add hydrogen to the protein
                    subprocess.run(
                        ['obabel', '-ipdb', cleaned_pdb, '-O', cleaned_pdb[:-4]+'_H.pdb', '-h'])

                    # run prepare_receptor.py (Autodock tools) from the command line to add charges to the protein
                    subprocess.run([os.path.join(CURRENT_PATH, 'ADFRsuite-1.0', 'bin', 'prepare_receptor'),
                                   '-r', cleaned_pdb[:-4]+'_H.pdb', '-o', cleaned_pdb[:-4]+'_H_charged.pdbqt'])


if __name__ == "__main__":
    receptorPreparation()

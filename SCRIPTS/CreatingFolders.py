import os

# define the directory structure


""""

├── INPUTS                    ====> Where the user will put the ligand and protein files
│ ├── Ligand                  ====> Where the user will put the ligand files
│ └── Protein                 ====> Where the user will put the protein files
├── OUTPUTS                   ====> Where the output files will be saved
│ ├── Ligand_prepared         ====> Where the prepared ligand files will be saved
│ └── Protein_prepared        ====> Where the prepared protein files will be saved


"""""


def creatingFolders():

    dir_structure = {
        "INPUTS": ["Ligand", "Protein"],
        "OUTPUTS": ["Ligand_prepared", "Protein_prepared", "Docking_results", "vina_box"]
    }

    # iterate over the directories in the directory structure
    for directory, subdirectories in dir_structure.items():
        # check if the directory exists
        if not os.path.exists(directory):
            # create the directory if it doesn't exist
            os.mkdir(directory)
        # iterate over the subdirectories in the directory
        for subdirectory in subdirectories:
            # define the path to the subdirectory
            subdirectory_path = os.path.join(directory, subdirectory)
            # check if the subdirectory exists
            if not os.path.exists(subdirectory_path):
                # create the subdirectory if it doesn't exist
                os.mkdir(subdirectory_path)

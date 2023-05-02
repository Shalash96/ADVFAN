# Autodock Vina For Absolute Noobs (ADVFAN)

## What is ADVFAN?

ADVFAN helps you to run single docking/virtual screening with just one command line code. It is a group of python scripts that use Autodock vina, ADFRsuite, and open babel to perform the docking process wthout knowing to much about how too use these software

## How it works?

1. Folders creation step
   It starts with creating the folders, where the user will add ligand(s) and protein, and folders, where the prepared ligand(s) and protein and docking results will be saved.
```
   ├── INPUTS ====> Where the user will put the ligand and protein files
   │ ├── Ligand ====> Where the user will put the ligand files(.sdf)
   │ └── Protein ====> Where the user will put the protein files(.pdb)
   ├── OUTPUTS ====> Where the output files will be saved
   │ ├── Ligand_prepared ====> Where the prepared ligand files will be saved(.pdbqt)
   │ └── Protein_prepared ====> Where the prepared protein files will be saved(.pdbqt)
```
2. Ligand preparation step
It read the ligand(s) file you put in`INPUTS/Ligand`directory and add hydrogen and partial charge to it using open babel. The new file will be saved in *.pdbqt* format in`OUTPUTS/Ligand_prepared`**NOTE** Ligand files must be in *.sdf* format 
3. Protein preparation step
It read the protein file you put in`INPUTS/Protein`directory and save the output files in`OUTPUTS/Protein_prepared`after performing the follwing steps:
    1. It use Pymol library to remove water, ligands, and if the protein consists of multi chains, all of them will be removed except **chain A**. This the default, but the user can change this and select which chain to remain. The file created will then be saved as *.pdb* file.
    2. The files created from the previous step will then be read by open babel to add hydrogens and save it as *.pdb* file.
    3. After adding hydrogen,`prepare_receptor`script from`ADFRsuite-1.0` will then be used to add the partial charge to the protein and the output will be saved as _.pdbqt_ format.

4. Vina box creation step
   After preparing both the ligand and the protein, ADVFAN will run `prepare_gpf` script from `ADFRsuite-1.0` to generate _.gpf_ file. ADVFAN will read the created file to extract the xyz-coordinates of the grid center and save them to `OUTPUTS/vina_box/vina_box.txt`.
   **NOTE** The default box size is 20, 20, 20, and the grid center is calaculated automatically by AutoDock vina unless the user passed a certain size and center
5. Docking step
   After creating all the required files to perform the docking process, ADVFAN will run vina software using these files, and the docking results will be saved in `OUTPUTS/Docking_results`. There will be two files for each ligand - _.pdbqt_ file which have the conformation of the good binding poses - _.txt_ file which show a summary for the docking process

## How to start with it?

To use ADVFAN, you have to make sure that you install **AutoDock Vina**, **Open Babel**, **ADFRsuite-1.0**, and **Pymol python library** on your machine

- To install Pymol, use the followimg command `pip install pymol`
- To install AutoDock Vina, click [here](https://autodock-vina.readthedocs.io/en/latest/installation.html)
- To install open babel version 2.4, click [here](https://www.herongyang.com/Cheminformatics/Babel-Install-Open-Babel-241-from-Source-Code.html)
  **NOTE** make sure you have version 2.x not 3.x from open babel to avoid the problem of adding partial charge to protein. For more click [here](https://sourceforge.net/p/openbabel/mailman/openbabel-discuss/thread/A9E7F432-E248-4AE4-A289-AA8BA93A8B85@ebi.ac.uk/)
- To install ADFRsuite-1.0, click [here](https://ccsb.scripps.edu/adfr/downloads/)

After installing them add the paths of open babel, vin, and ADFRsuite to the `SCRIPTS/paths.py` file, a preview content of the file is shown below. If you installed them in your `~` directory the following paths should work fine with you and no need to change them.

```
VINA_PATH = os.path.join(os.path.expanduser(
    '~'), 'vina_1.2.3_linux_x86_64')


ADFRsuite_PATH = os.path.join(os.path.expanduser('~'), 'ADFRsuite-1.0')


obabel_PATH = os.path.join(os.path.join('/usr', 'local', 'bin', 'obabel'))
```

## How to use it?

You only provide the ligand files and the protein file then run`python ADVFAN.py` from the terminal, and all the previous steps will occur behind the scene. **How easy!!**

## What are the docking parameter used?

By running run`python ADVFAN.py`, ADVFAN will use the default parameters which are:

- center_x = auto
- center_y = auto
- center_z = auto
- size_x = 20
- size_y = 20
- size_z = 20
- Chain where the docking will occur is A
- Docking exhaustiveness is 8
- Docking number of modes is 9
- Docking energy range is 3

## How to control these parameters?

```
usage: ADVFAN.py [-h] [-c] [-e] [-nm] [-er] [--new] [--size  [...]] [--center  [...]]

options:
  -h, --help            show this help message and exit
  -c , --chain          Chain name of the protein to keep
  -e , --exhaustiveness
                        Exhaustiveness of the docking
  -nm , --num_modes     Number of docking modes
  -er , --energy_range
                        The maximum energy difference allowed between the best binding mode and the worst binding mode
  --new                 Delete the input files abd their docking results and start afresh
  --size  [ ...]        Size of the vina box. The default is 20 20 20. If you want to change it, input should be in the form of x y z. Only separate by one
                        space not comma
  --center  [ ...]      xyz coordinations of the grid center. The default is auto calaculated by Vina. If you want to change it, input should be in the form
                        of x y z. Only separate by one space not comma

```

### Examples

- `python ADVFAN.py` run with default parameters
- `python ADVFAN.py -c B -e 32 -nm 12 -er 2` this will delete all chains except B, exhaustiveness = 32, number of modes = 12, and the energy range is 2

## what is up coming?

I am thinking of creating a docker container for this project to make it more easier where you just download the container and run the scripts without fruther installation of third libraries. But I am current learning Docker at the moment :).

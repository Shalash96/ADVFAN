from SCRIPTS.LigandPrepartion import ligandPreparation
from SCRIPTS.ReceptorPreparation import receptorPreparation
from SCRIPTS.CreatingFolders import creatingFolders
from SCRIPTS.VinaBoxCreation import vinaBoxCreation
from SCRIPTS.DockingVina import dockingVina

# take the chain name as input from the user from the command line
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Perform docking using AutoDock Vina with just one command.\
            The script will create the necessary folders, prepare the ligand and the receptor, \
            create the docking box, and perform the docking. In the INPUTS folder, you add the ligand \
            and the protein. The ligand should be in the Ligand folder and the protein should be in the \
            Protein folder. The ligand should be in sdf format and the protein should be in pdb format. \
            The script will create the OUTPUTS folder and save the results of the docking in it. \
            ')
    parser.add_argument('-c', '--chain', type=str.capitalize, default='A',
                        help='Chain name of the protein to keep', metavar='')
    parser.add_argument('-e', '--exhaustiveness', type=str, default='8',
                        help='Exhaustiveness of the docking', metavar='')
    parser.add_argument('-nm', '--num_modes', type=str, default='9',
                        help='Number of docking modes', metavar='')
    parser.add_argument('-er', '--energy_range', type=str, default='3',
                        help='The maximum energy difference allowed between the best binding mode and the worst binding mode', metavar='')

    parser.add_argument('--new', action='store_true', default=False,
                        help='Delete the input files and their docking results and start afresh')

    parser.add_argument('--size', type=int, nargs='+',
                        help='Size of the vina box. The default is 20 20 20. If you want to change it, \
                            input should be in the form of x y z. Only separate by one space not comma', metavar='')
    parser.add_argument('--center', type=int, nargs='+',
                        help='xyz coordinations of the grid center. The default is auto calaculated by Vina. \
                        If you want to change it, input should be in the form of x y z. Only separate by one space not comma', metavar='')

    args = parser.parse_args()

    if args.new:
        # delete everything and start afresh
        creatingFolders(True)

    else:
        creatingFolders()
        ligandPreparation()
        receptorPreparation(args.chain)
        vinaBoxCreation(size=args.size, center=args.center)

        # print to the terminal screen the deafult values of the docking parameters if the user didn't specify them
        # or the values that the user specified
        print('The docking parameters are as follows:')
        print(f"Chain where the docking will occur is {args.chain}")
        print(f"Docking exhaustiveness is {args.exhaustiveness}")
        print(f"Docking number of modes is {args.num_modes}")
        print(f"Docking energy range is {args.energy_range}")

        dockingVina(args.exhaustiveness, args.num_modes, args.energy_range)

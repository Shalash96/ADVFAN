import pymol


def clean_pdb(filename, chain='A'):
    # Load the file and the name of the chain to keep
    pymol.cmd.load(filename)
    # Remove all HETATM records
    pymol.cmd.remove('hetatm')
    # Remove all solvent
    pymol.cmd.remove('solvent')
    # Remove all all chains except A
    pymol.cmd.remove(f'not chain {chain}')

    # Save the file
    pymol.cmd.save(filename[:-4] + '_clean.pdb')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        clean_pdb(sys.argv[1])
    elif len(sys.argv) == 3:
        clean_pdb(sys.argv[1], sys.argv[2].capitalize())
    else:
        print("""
        This script is used to clean a PDB file.
        It removes all HETATM records, all solvent and all chains except the one specified.
        Usage: python clean_pdb.py <pdb_file> chain name you want to keep (optional)
        example python clean_pdb.py 1a0j.pdb => This will keep chain A (This is the default) and remove all other chains, HETATM records and solvent
        example python clean_pdb.py 1a0j.pdb B => This will keep chain B and remove all other chains, HETATM records and solvent
        """)

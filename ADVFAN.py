from SCRIPTS.LigandPrepartion import ligandPrearation
from SCRIPTS.ReceptorPreparation import receptorPreparation
from SCRIPTS.CreatingFolders import creatingFolders
from SCRIPTS.VinaBoxCreation import vinaBoxCreation

if __name__ == "__main__":
    creatingFolders()
    ligandPrearation()
    receptorPreparation()
    vinaBoxCreation()

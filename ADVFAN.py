from SCRIPTS.LigandPrepartion import ligandPreparation
from SCRIPTS.ReceptorPreparation import receptorPreparation
from SCRIPTS.CreatingFolders import creatingFolders
from SCRIPTS.VinaBoxCreation import vinaBoxCreation
from SCRIPTS.DockingVina import dockingVina
if __name__ == "__main__":
    creatingFolders()
    ligandPreparation()
    receptorPreparation()
    vinaBoxCreation()
    dockingVina()



class Deployment():
    """
    The instance of this class describes the deployment of a player at one turn
    It does not care about whether the deployment is feasible or not, this should be determined by the searching algorithm
    """
    def __init__(self,info_deploy,def_deploy,player_index):
        """
        :param info_deploy: a list of unit_loc of information unit deployed at this turn
        :param def_deploy: a list of unit_loc of defensive unit deployed at this turn
        :param player_index: 0 for the player and 1 for the enemy
        """
        self.info_deploy = info_deploy
        self.def_deploy = def_deploy
        self.player_index = player_index


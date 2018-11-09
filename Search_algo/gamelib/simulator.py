from .deployment import Deployment
from .game_map import GameMap,GameUnit

class Simulator():
    def __init__(self,my_dep:Deployment,en_dep:Deployment,gameState):
        self.my_dep = my_dep
        self.en_dep = en_dep
        self.my_info_unit_loc = []
        self.en_info_unit_loc = []
        self.currentMap = gameState.game_map
        self.destroyed_units = []
        self.damaged_units = []
        self.my_o_hp = gameState.my_health # o stands for original
        self.en_o_hp = gameState.enemy_health
        self.my_hp = self.my_o_hp # keeps track of my hp during simulation
        self.enemy_hp = self.en_o_hp
        self.frame_num = 0

    def _simulate_one_frame(self):
        """
        This function simulate one frame based on the current gameState
        it does so by doing the following:
        1.Info Units Move
            a. determine where they would move
            b. determine what is the square they would be at at the next frame
            c. change f_info_unit_loc and e_info_unit_loc
        2.Deals damage
            a. if any unit reaches the edge, reduces health
            b. defensive units deal damage
            c. information units deal damage
            d. update remaining unit
            e. update currentMap
        """
        pass

    def _if_simu_ends(self):
        """
        :return: whether simulation should end
        """
        return self.my_info_unit_loc == [] and self.en_info_unit_loc == []

    def _evaluate(self):
        """
        evaluate the outcome of simulation based on damage dealt
        the result will be used for search algorithm
        :return: a number representing the outcome of this simulation, positive if it is pro player, negative if it is pro enemy
        """

    def run(self):
        """
        run a continuous simulation
        :return: see _evaluate()
        """
        while(not self._if_simu_ends()):
            self._simulate_one_frame()
            self.frame_num += 1
        return self._evaluate()

from .deployment import Deployment
from .game_map import GameMap,GameUnit

class Simulator():
    def __init__(self,game_state,my_dep:Deployment=None,en_dep:Deployment=None):
        self.my_dep = my_dep
        self.en_dep = en_dep
        self.my_info_unit_loc = []
        self.en_info_unit_loc = []
        self.game_state = game_state
        self.gameMap = game_state.game_map
        self.destroyed_units = []
        self.damaged_units = []
        self.my_o_hp = game_state.my_health # o stands for original
        self.en_o_hp = game_state.enemy_health
        self.my_hp = self.my_o_hp # keeps track of my hp during simulation
        self.enemy_hp = self.en_o_hp
        self.frame_num = 0

        self.MOVE_UP = 1
        self.MOVE_RIGHT = 2
        self.MOVE_LEFT = 3
        self.MOVE_EXPLODE = 0

    def _get_next_move(self,unit:GameUnit):
        """
        Gives the next move of a certain unit at a given location (up,right,left or explode)
        :param unit: the unit in simulation
        :return: the move to be taken (MOVE_UP,MOVE_RIGHT,MOVE_LEFT,MOVE_EXPLODE)
        """
        # Get the intended move by the last move taken. If this is the first move the value should be 0 (explode)
        if unit.last_move == self.MOVE_EXPLODE:
            intended_move = self.MOVE_UP
        elif unit.last_move == self.MOVE_UP:
            intended_move = self.MOVE_RIGHT
        else:
            intended_move = self.MOVE_UP


    def __get_destination(self,unit:GameUnit):
        """
        :param unit:
        :return: a list of coordinates of the edge the unit tries to reach
        """
        if [unit.x, unit.y] in self.gameMap.get_edge_locations(self.game_state.game_map.BOTTOM_RIGHT):
            return self.gameMap.get_edge_locations(self.game_state.game_map.TOP_LEFT)
        else:
            return self.gameMap.get_edge_locations(self.game_state.game_map.TOP_RIGHT)

    def _get_route(self,unit:GameUnit):
        """
        Depth-First Search for shortest route
        :param unit:
        :return: the shortest route a unit would take
        """
        route = [[unit.x,unit.y]]
        impossible_node = []
        last_move = self.MOVE_EXPLODE # initialize first move
        # keep searching if destination is not reached and the first node is not given up (i.e., impossible to get to the edge)
        while route[-1] not in self.__get_destination(unit) and route[0] not in impossible_node:
            x = route[-1][0]
            y = route[-1][1]

           # DEBUG SECTION
            print('route: ',route)
            print('impossible node:',impossible_node)
            if(last_move==self.MOVE_RIGHT):
                print('MOVING RIGHT')
            elif(last_move==self.MOVE_UP):
                print('MOVING UP')
            elif(last_move==self.MOVE_LEFT):
                print('MOVING LEFT')
            else:
                pass

            # consider MOVE_RIGHT first if last_move is MOVE_UP
            if last_move == self.MOVE_UP:
                if [x+1, y] not in impossible_node and not self.game_state.contains_stationary_unit([x+1,y]):
                    route.append([x+1,y])
                    last_move = self.MOVE_RIGHT
                elif [x, y+1] not in impossible_node and not self.game_state.contains_stationary_unit([x,y+1]):
                    route.append([x,y+1])
                    last_move = self.MOVE_UP
                elif [x-1,y] not in impossible_node and not self.game_state.contains_stationary_unit([x-1,y]):
                    route.append([x-1,y])
                    last_move = self.MOVE_LEFT
                else:
                    impossible_node.append(route.pop())  # if nowhere to go, remove the last item and save it

            # consider MOVE_UP first if last move is MOVE_RIGHT or MOVE_EXPLODE(initial condition) or MOVE_LEFT
            elif last_move == self.MOVE_RIGHT or last_move == self.MOVE_EXPLODE or last_move == self.MOVE_LEFT:
                if [x, y+1] not in impossible_node and not self.game_state.contains_stationary_unit([x,y+1]):
                    route.append([x,y+1])
                    last_move = self.MOVE_UP
                # move right only when it is feasible and last move is not MOVE_LEFT to avoid repeat
                elif [x+1, y] not in impossible_node and not self.game_state.contains_stationary_unit([x+1,y]) and last_move != self.MOVE_LEFT:
                    route.append([x+1,y])
                    last_move = self.MOVE_RIGHT
                # move left only when it is feasible and last move is not MOVE_RIGHT to avoid repeat
                elif [x-1,y] not in impossible_node and not self.game_state.contains_stationary_unit([x-1,y]) and last_move != self.MOVE_RIGHT:
                    route.append([x-1,y])
                    last_move = self.MOVE_LEFT
                else:
                    impossible_node.append(route.pop())  # if nowhere to go, remove the last item and save it

        if route[0] in impossible_node:
            print("Dead end for the unit! Impossible to get to the edge without destroying")
            return None  # In this case, per frame simulation is needed
        else:
            return route





    def _simulate_one_frame(self):
        """
        This function simulate one frame based on the current game_state
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
            e. update gameMap
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

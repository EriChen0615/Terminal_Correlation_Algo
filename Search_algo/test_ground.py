from gamelib.tests import BasicTests
from gamelib.simulator import Simulator
from gamelib.deployment import Deployment
from gamelib.navigation import ShortestPathFinder
from gamelib.game_map import GameMap, GameUnit
from gamelib.game_state import GameState

global FILTER, ENCRYPTOR, DESTRUCTOR, PING, EMP, SCRAMBLER, REMOVE, FIREWALL_TYPES, ALL_UNITS, UNIT_TYPE_TO_INDEX
# initialize test and shorthands for units
test = BasicTests()
game_state = test.make_turn_0_map()
game_map = game_state.game_map

UNIT_TYPE_TO_INDEX = {}
FILTER = game_state.config["unitInformation"][0]["shorthand"]
UNIT_TYPE_TO_INDEX[FILTER] = 0
ENCRYPTOR = game_state.config["unitInformation"][1]["shorthand"]
UNIT_TYPE_TO_INDEX[ENCRYPTOR] = 1
DESTRUCTOR = game_state.config["unitInformation"][2]["shorthand"]
UNIT_TYPE_TO_INDEX[DESTRUCTOR] = 2
PING = game_state.config["unitInformation"][3]["shorthand"]
UNIT_TYPE_TO_INDEX[PING] = 3
EMP = game_state.config["unitInformation"][4]["shorthand"]
UNIT_TYPE_TO_INDEX[EMP] = 4
SCRAMBLER = game_state.config["unitInformation"][5]["shorthand"]
UNIT_TYPE_TO_INDEX[SCRAMBLER] = 5
REMOVE = game_state.config["unitInformation"][6]["shorthand"]
UNIT_TYPE_TO_INDEX[REMOVE] = 6

# set up wall for shortest path finding testing
for i in range(7,11):
    game_map.add_unit(FILTER,[9,i],0)
game_map.add_unit(FILTER,[7,10])
game_map.add_unit(FILTER,[8,10])

simulator = Simulator(game_state)
print(game_state.game_map.get_edge_locations(game_state.game_map.TOP_LEFT))
ping = GameUnit(PING,game_state.config, 0, x=7, y=6)
#print(ping.x)
#print(game_map[7,7])
print(simulator._get_route(ping))
# path_finder = ShortestPathFinder()
# game_state.game_map.add_unit('FF',[1,1])
# path_finder.initialize_map(game_state)
# path_finder.print_map()


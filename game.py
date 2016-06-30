import pokemon
import random
from pokemon import BULBASAUR
from pokemon import CHARMANDER
from pokemon import SQUIRTLE

from pokemon import ATTACK
from pokemon import DEFENSE
from pokemon import HP
from pokemon import SPEED

from pokemon import FIRE 
from pokemon import GRASS
from pokemon import NORMAL
from pokemon import WATER

from pokemon import EMBER
from pokemon import GROWL
from pokemon import SCARY_FACE
from pokemon import SCRATCH
from pokemon import TACKLE
from pokemon import TAIL_WHIP
from pokemon import VINE_WHIP
from pokemon import WATER_GUN



# MOVES that contains a dictionary. The keys are the
# move variables defined in the pokemon module. The first value is a
# string containing the move name. The second value is the type of the move
# The third value is which stat should be targeted
# by the move (HP, attack, defense, or speed)
MOVES = {EMBER: ('ember', FIRE, HP), 
         GROWL: ('growl', NORMAL, ATTACK), 
         SCARY_FACE: ('scaryface', NORMAL, SPEED), 
         SCRATCH: ('scratch', NORMAL, HP), 
         TACKLE: ('tackle', NORMAL, HP), 
         TAIL_WHIP: ('tailwhip', NORMAL, DEFENSE), 
         VINE_WHIP: ('vinewhip', GRASS, HP), 
         WATER_GUN: ('watergun', WATER, HP)} 

# get_all_pokemon returns a list of all possible Pokemon. Uses the Pokemon species
# variables defined in the pokemon module as parameters. If the
# function's parameter is True, the pokemon returned in the list is
# wild.
def get_all_pokemon(is_wild):
  if is_wild:  
    Bulbasaur = pokemon.get_new_pokemon(BULBASAUR, 
                                        get_move_set(BULBASAUR), 
                                        True)
    Charmander = pokemon.get_new_pokemon(CHARMANDER, 
                                        get_move_set(CHARMANDER), 
                                        True)
    Squirtle = pokemon.get_new_pokemon(SQUIRTLE, 
                                        get_move_set(SQUIRTLE), 
                                        True)
    pokemon_list = [Bulbasaur, Charmander, Squirtle]
  else:
    Bulbasaur = pokemon.get_new_pokemon(BULBASAUR, 
                                        get_move_set(BULBASAUR), 
                                        False)
    Charmander = pokemon.get_new_pokemon(CHARMANDER, 
                                        get_move_set(CHARMANDER), 
                                        False)
    Squirtle = pokemon.get_new_pokemon(SQUIRTLE, 
                                        get_move_set(SQUIRTLE), 
                                        False)
    pokemon_list = [Bulbasaur, Charmander, Squirtle]
  return pokemon_list

# get_move_set takes one parameter, the ID of a
# Pokemon as defined by the variables in the pokemon module, and returns a list
# of move keys as defined by the variables in the pokemon module.
def get_move_set(pokemon_ID):
  if pokemon_ID == BULBASAUR:
    move_keys = [SCARY_FACE,  TACKLE, TAIL_WHIP, VINE_WHIP]
  elif pokemon_ID == CHARMANDER:
    move_keys = [EMBER,  GROWL, SCRATCH, TAIL_WHIP]
  elif pokemon_ID == SQUIRTLE:
    move_keys = [GROWL,  SCARY_FACE,  TACKLE, WATER_GUN]
  return move_keys

# get_npc_move that takes one Pokemon parameter, which
# is the computer's pokemon. Picks a move at random from the
# Pokemon's move list and return its tuple.
def get_npc_move(poke):
  if poke.get_name() == 'Bulbasaur':
    return MOVES[random.choice(get_move_set(BULBASAUR))]
  elif poke.get_name() == 'Charmander':
    return MOVES[random.choice(get_move_set(CHARMANDER))]
  elif poke.get_name() == 'Squirtle':
    return MOVES[random.choice(get_move_set(SQUIRTLE))]

# get_npc_pokemon that returns a random wild Pokemon.
def get_npc_pokemon():
  return random.choice(get_all_pokemon(True))

# get_user_choice that takes two parameters. The first
# parameter is a list of string options to present to the user. The
# second is a prompt to be presented to the player. The function outputs
# prompt and the choices and returns an index when a user
# has selected a valid option.
# Example: get_user_choice(['Option1', 'Option2', 'Option3'], 'Select one.')
# Outputs:
# 
# Select one. 
#    0: Option1
#    1: Option2
#    2: Option3
# :: 
def get_user_choice(str_options, prompt):
  input = -1
  n = 1
  while not (input >= 0 and input < n):
    print prompt
    n = 0
    for option in str_options:
      print '   ' + str(n) + ': ' + str(str_options[n])
      n += 1
    input = int(raw_input(':: '))
  return input

# get_user_move takes one Pokemon parameter and
# uses the get_user_choice function to allow the user to select one of the
# Pokemon's moves. Returns the selected move's tuple.
def get_user_move(poke):
  if poke.get_name() == 'Bulbasaur':
    move_prompt = 'What will BULBASAUR do?'
    move_options = ['Scary Face', 
                    'Tackle', 
                    'Tail Whip', 
                    'Vine Whip']
    move_index = get_user_choice(move_options, move_prompt)
    move_list = get_move_set(BULBASAUR)
    move = MOVES[move_list[move_index]]
  elif poke.get_name() == 'Charmander':
    move_prompt = 'What will CHARMANDER do?'
    move_options = ['Ember', 
                    'Growl', 
                    'Scratch', 
                    'Tail Whip']
    move_index = get_user_choice(move_options, move_prompt)
    move_list = get_move_set(CHARMANDER)
    move = MOVES[move_list[move_index]]
  elif poke.get_name() == 'Squirtle':
    move_prompt = 'What will SQUIRTLE do?'
    move_options = ['Growl', 
                    'Scary Face', 
                    'Tackle', 
                    'Water Gun']
    move_index = get_user_choice(move_options, move_prompt)
    move_list = get_move_set(SQUIRTLE)
    move = MOVES[move_list[move_index]]
  return move


# get_user_pokemon uses get_all_pokemon to allow the user to select
# a Pokemon. Returns the selected Pokemon object.
def get_user_pokemon():
  pokemon_options = get_all_pokemon(False)
  pokemon_options_list = [pokemon_options[0].get_name(), 
                          pokemon_options[1].get_name(), 
                          pokemon_options[2].get_name()]
  return pokemon_options[get_user_choice(pokemon_options_list, 
                                         'Select a Pokemon.')]

# print_hp_meter takes one Pokemon parameter and
# prints out its hit points (HP). The meter is thirty characters long and
# adjusts based on the percentage of the Pokemon's HP that remains.
# The HP meter is output in the following format:
# [               xxxxxxxxxxxxxxx] (50/100)
def print_hp_meter(poke):
  hit_points = poke.get_hp()
  meter_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  number_of_x = int(hit_points / (10/3.))
  index = 29
  while number_of_x > 0:
    meter_list[index] = 'x'
    number_of_x -= 1
    index -= 1
  print (poke.get_name() + ': ' + 
         '[' + ''.join(meter_list) + '] (' + 
         str(hit_points) + '/100)')

# print_move_result takes three parameters. The
# first parameter is a boolean value indicating whether or not the move
# was successful. The second parameter is a Pokemon object, the Pokemon
# on which the move was performed. The third parameter is the 3-tuple
# that defines the move itself. If the move was unsuccessful, the function
# prints out: "But it failed!" The function prints out an
# explanation of the result of running the move. If the move included a damage
# multiplier (according to the get_multiplier function defined in the pokemon
# module), then the function prints out "It's super effective!". Then it
# prints out: "[Wild ]POKEMON NAME's STAT fell!" where "Wild" appears if
# the Pokemon is wild, POKEMON NAME is the name given by the Pokemon object, and
# STAT is the name of the stat effected by the move.
def print_move_result(is_successful, affected_poke, move_tuple):
  if not is_successful:
    print 'But it failed!'
  else:
    if pokemon.get_multiplier(move_tuple[1], 
                              affected_poke.get_type()) == 1.5:
      print "It's super effective!"
    if affected_poke.is_wild() == True:
      if move_tuple[2] == ATTACK:
        print "Wild " + affected_poke.get_name() + "'s ATTACK fell!"
      elif move_tuple[2] == DEFENSE:
        print "Wild " + affected_poke.get_name() + "'s DEFENSE fell!"
      elif move_tuple[2] == HP:
        print "Wild " + affected_poke.get_name() + "'s HP fell!"
      elif move_tuple[2] == SPEED:
        print "Wild " + affected_poke.get_name() + "'s SPEED fell!"
    else:
      if move_tuple[2] == ATTACK:
        print affected_poke.get_name() + "'s ATTACK fell!"
      elif move_tuple[2] == DEFENSE:
        print affected_poke.get_name() + "'s DEFENSE fell!"
      elif move_tuple[2] == HP:
        print affected_poke.get_name() + "'s HP fell!"
      elif move_tuple[2] == SPEED:
        print affected_poke.get_name() + "'s SPEED fell!"


# play() runs a Pokemon battle. The user should
# select a Pokemon and so should the computer player. Then the user and and
# computer player should each select moves until one Pokemon faints.
def play():
  user_pokemon = get_user_pokemon()
  pc_pokemon = get_npc_pokemon()
  user_poke_name = user_pokemon.get_name().upper()
  pc_poke_name = pc_pokemon.get_name().upper()
  print ('Wild ' + pc_poke_name + ' appeared! Go! ' + 
         user_poke_name + '!')
  if user_pokemon.get_speed() > pc_pokemon.get_speed():
    while (not pc_pokemon.is_fainted() and 
           not user_pokemon.is_fainted()):
      print_hp_meter(user_pokemon)
      print_hp_meter(pc_pokemon)
      player_move = get_user_move(user_pokemon)
      print user_poke_name + ' used ' + player_move[0].upper() + '!'
      is_successful = user_pokemon.attack(pc_pokemon, player_move)
      print_move_result(is_successful, pc_pokemon, player_move)
      pc_move = get_npc_move(pc_pokemon)
      print pc_poke_name + ' used ' + pc_move[0].upper() + '!'
      is_successful = pc_pokemon.attack(user_pokemon, pc_move)
      print_move_result(is_successful, user_pokemon, pc_move)
    if pc_pokemon.is_fainted():
      print 'Wild ' + pc_poke_name + ' fainted!'
    elif user_pokemon.is_fainted():
      print + user_poke_name + ' fainted!'
  else:
    while (not pc_pokemon.is_fainted() and 
           not user_pokemon.is_fainted()):
      print_hp_meter(user_pokemon)
      print_hp_meter(pc_pokemon)
      pc_move = get_npc_move(pc_pokemon)
      print pc_poke_name + ' used ' + pc_move[0].upper() + '!'
      is_successful = pc_pokemon.attack(user_pokemon, pc_move)
      print_move_result(is_successful, user_pokemon, pc_move)
      player_move = get_user_move(user_pokemon)
      print user_poke_name + ' used ' + player_move[0].upper() + '!'
      is_successful = user_pokemon.attack(pc_pokemon, player_move)
      print_move_result(is_successful, pc_pokemon, player_move)
    if pc_pokemon.is_fainted():
      print 'Wild ' + pc_poke_name + ' fainted!'
    elif user_pokemon.is_fainted():
      print user_poke_name + ' fainted!'


play()
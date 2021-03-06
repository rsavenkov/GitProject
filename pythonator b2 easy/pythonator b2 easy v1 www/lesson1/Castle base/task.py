from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z


mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# BUILDING LOCATION
# player's z coordinate used as reference point for all building
ref_z = player_z
# x value at start of stone path heading +x direction
path_x_min = 105
# x value at start of castle
castle_x_min = 121
# y value of floor of castle
floor_y = 9

# BUILDING SIZE
# castle length (in x direction)
castle_length = number
# castle width (in z direction)
castle_width = number
# castle height excluding roof including floor
castle_height = number

# BUILDING MATERIALS
air = "air"
castle = "default:stone"

# ENGINEERING CALCULATIONS
# z value of side of castle (where castle_wall_z < player_z)
wall_z = formula
# external dimensions of castle base
range_x_castle_ext = sequence
range_y_castle_ext = sequence
range_z_castle_ext = sequence
# internal dimensions of castle base
range_x_castle_int = range(castle_x_min + 1, castle_x_min + castle_length - 1)
range_y_castle_int = range(floor_y + 1, floor_y + castle_height)
range_z_castle_int = range(wall_z + 1, wall_z + castle_width - 1)

# BUILD
# clear any existing structure or ground
mc.build(range(castle_x_min - 1, castle_x_min + castle_length + 10), range(floor_y + 1, floor_y + 31), range(ref_z - 4, ref_z + 5), air)
# the base of the castle
mc.build(range_x_castle_ext, range_y_castle_ext, range_z_castle_ext, castle)
mc.build(range_x_castle_int, range_y_castle_int, range_z_castle_int, air)
# create a doorway
mc.build(castle_x_min, sequence, ref_z, air)

mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018 - 2019.

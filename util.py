import glm
# 6 x 3 matrix direction
DIRECTIONS = (glm.ivec3(1, 0, 0), 
            glm.ivec3(-1, 0, 0), 
            glm.ivec3(0, 1, 0), 
            glm.ivec3(0, -1, 0), 
            glm.ivec3(0, 0, 1), 
            glm.ivec3(0, 0, -1))
# direction vectors declarations
EAST = glm.ivec3(1, 0, 0)
WEST = glm.ivec3(-1, 0, 0)
UP = glm.ivec3(0, 1, 0)
DOWN = glm.ivec3(0, -1, 0)
SOUTH = glm.ivec3(0, 0, 1)
NORTH = glm.ivec3(0, 0, -1)

assert [EAST.x, EAST.y, EAST.z] == [1, 0, 0]
assert [WEST.x, WEST.y, WEST.z] == [-1, 0, 0]
assert [UP.x, UP.y, UP.z] == [0, 1, 0]
assert [DOWN.x, DOWN.y, DOWN.z] == [0, -1, 0]
assert [SOUTH.x, SOUTH.y, SOUTH.z] == [0, 0, 1]
assert [NORTH.x, NORTH.y, NORTH.z] == [0, 0, -1]
assert DIRECTIONS[0] == [1, 0, 0]
assert DIRECTIONS[1] == [-1, 0, 0]
assert DIRECTIONS[2] == [0, 1, 0]
assert DIRECTIONS[3] == [0, -1, 0]
assert DIRECTIONS[4] == [0, 0, 1]
assert DIRECTIONS[5] == [0, 0, -1]
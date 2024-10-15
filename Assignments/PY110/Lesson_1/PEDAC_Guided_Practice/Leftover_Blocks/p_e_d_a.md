Full Problem:

You have a number of building blocks that can be used to build a valid structure.
There are certain rules about what determines a valid structure:
 - The building blocks are cubes.
 - The structure is built in layers.
 - The top layer is a single block.
 - A block in an upper layer must be supported by four blocks in a lower layer.
 - A block in a lower layer can support more than one block in an upper layer.
 - You cannot leave gaps between blocks.


**Input:** Number of blocks

**Output:** Remainder of blocks

Rules:
- The building blocks are cubes.
- The structure is built in layers.
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

` Build downwards?`

 if there is a block at `position[layer] (2,2)` 
 then there must be blocks at `poition[layer-1] (2,2),(1,2),(2,1),(1,1)`
 
so that means a block at (_x_,_y_) in layer _p_ requires:

(_x_,_y_), (_x_,_y_-1), (_x_-1,_y_), (_x_-1,_y_-1) in layer _p_-1

The structure can only ever be symmetrical, pyramid-shaped

The math is easier of we build upside-down.

if layer 1 is always 1 block, layer 2 must be 4, 3 must be 9, 4 is 16 etc

the number of blocks to make a new layer is layer^2.

therefore, with n blocks, you can make a number of layers as such: 

p = layer count
m = cubes used
n = cube limit

this is a sum of squares problem
$$
m = \sum_{i=1}^{p} i^2 \leq n
$$
or something like that

# Data Structures
I will only use integers, no reason to use anything else.


# Algorithm
For each layer, calculate the number of cubes on it
- If the sum of that layer and the current_cube_count so far is greater than the total_cube_count:
  - return the total_cube_count minus current_cube_count
- Else: 
  - add that layer's sum to the current_cube count and move to the next layer

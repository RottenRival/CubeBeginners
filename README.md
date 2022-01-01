# CubeBeginners
This project is a solution to the very daunting 3x3 Rubik's Cube. This assumes that the reader is familiar with the notations of the cube(eg: F, R').
This uses the Beginner's method algorithm's for solving the cube.
There are three parts to this solver:
  The print_state() function shows the current state of the six faces of the cube.The sides of the cube are denoted by the first letter of it's corresponding colour.eg: 'o'-Orange   face.
The algorithm consists of:
  The white_cross() function is the first step in solving the cube in lay man's terms.
  Similarly, the first_layer(),middle_layer() etc. functions represent the following layers of the cube.
 The scrambling of the cube is done manually by the user when the program is run by giving inputs such as f,r,l etc, for clockwise twists and up,fp,rp etc for anticlockwise        twists(prime)
 Once done scrambling, the user is prompted 0 to signify the end of the scramble, after which the program executes all the functions,and displays all the algorithms required to solve the cube.
 One contribution could be timing the solution.
  

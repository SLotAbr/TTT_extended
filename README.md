# TTT_extended
Extended version of "Tic-tac-toe" with 20x20 field and "5 in a line" condition of victory.

Some notes:
1. Placement on the field of the sign is made by moving the button from the 
	borders of the screen and placing the image of the sign in its place
2. There are many different ways to check the victory conditions, the most 
	computationally profitable one I have found: store the coordinates of 
	the last move and check all possible victory positions associated with 
	the cell of the last move
3. There may be zones on the field for which you need to write unique checks
	(for the central and side parts of the field, the checks are different), 
	but this is too boring, so I expanded the size of the field (the user 
	does not have access to the entire field) to be able to use one check on 
	the entire playing field - i.e. the size of the "real" field: 
	(20 + 4 * 2 (for each side)) ** 2, but the user can only have access to 
	"playing" field of 20 ** 2
4. The higher point affects the "draw" condition: by default, the values of 
	the cells are encoded as 0 (no sign of any player), which means that 
	after occupying all possible cells, in the absence of a winner, 384 
	(28 ** 2-20 ** 2) cells will remain on the field equal to zero

Some variables Used:
 - Button_type - hint button (Displays the color of the acting side)
 - globalType - current player index
 - last_action - the coordinate of the last move
 - TypeCells - field element values (0 - empty cell; 1 - zero; 2 - cross)
 - BaseCells - list with cells
 - Win - winner index (the designation rules are the same as in TypeCells)

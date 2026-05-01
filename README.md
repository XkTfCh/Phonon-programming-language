COMMANDS:

F  - Forward:      x = (x + 1) % 50
B  - Back:         x = (x - 1) % 50
R  - Right:        y = (y + 1) % 50
L  - Left:         y = (y - 1) % 50
U  - Up:           z = (z + 1) % 50
D  - Down:         z = (z - 1) % 50

#  - Grow:         if current cell == 0: set to 1
+  - Absorb:       current += previous, previous = 0
~  - Invert:       current = -current
.  - Emit:         output chr(current % 256)
,  - Receive:      current = ord(input character)
@  - Debug:        print [x,y,z]=value
(  - Loop start:   repeat while any neighbor != 0
)  - Loop end:     jump back to matching (

MEMORY:
- Cube size: 50 x 50 x 50 (125,000 cells)
- Values range: -128 to 127 (signed byte)
- Toroidal: moving off edge wraps around
- Previous cell: remembers where you came from

EXAMPLES:

1. Create number 1:
   #

2. Create number 5:
   # F # + F # + F # + F # +

3. Move value from A to B:
   # F +

4. Simple loop (absorbs one neighbor):
   # F ( + )

5. Nested loops (collect three 1's):
   # F # R ( ( + ) )

6. Echo program:
   ,.

7. Debug position:
   FFF@

TIPS:
- # only works if cell is empty (value == 0)
- + needs previous cell - always move before using it
- Loops ( ) depend on neighbors, not current cell
- Use @ to debug coordinates and values# Phonon-programming-language
Phonon is an esoteric programming language based on moving a "phonon" (a quantum of vibration) through a 3D crystal of size 50×50×50. Instead of the classic Brainfuck tape, it uses a cube, and arithmetic is built on absorbing values from previous cells.

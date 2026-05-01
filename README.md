# Phonon

**Phonon** is an esoteric programming language based on moving a "phonon" (a quantum of vibration) through a 3D crystal lattice of size 50×50×50.


## Concept

You are a **phonon** traveling through a crystal lattice. Each cell is an atom with a charge (number from -128 to 127). A Phonon program consists of commands that:
- Move through three dimensions
- Create new charges
- Absorb charges from neighboring atoms
- Interact with the outside world via I/O

## Commands

| Command | Name | Action |
|---------|------|--------|
| `F B R L U D` | Movement | Step through the cube (toroidal wrap) |
| `#` | Grow | If current cell == 0, set to 1 |
| `+` | Absorb | Current += previous, previous = 0 |
| `~` | Invert | Current = -current |
| `.` | Emit | Output `chr(current % 256)` |
| `,` | Receive | Read character into current cell |
| `@` | Debug | Show `[x,y,z]=value` |
| `( )` | Resonate | Loop while any neighbor != 0 |

## Memory

- **Size:** 50×50×50 = 125,000 cells
- **Range:** -128 to 127 (signed byte)
- **Geometry:** Toroidal (wraps at edges)
- **Previous cell:** Always remembers where you came from

## Examples

### Create number 1

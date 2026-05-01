def run_code(code, user_input):
    cells = [[[0] * 50 for _ in range(50)] for _ in range(50)]
    x = 0
    y = 0
    z = 0
    
    result = ''
    
    px = 0
    py = 0
    pz = 0
    
    input_index = 0
    i = 0
    
    def get_cell(x, y, z):
        return cells[x][y][z]
    
    def set_cell(x, y, z, value):
        value = value % 256  
        if value >= 128:
            value -= 256
        cells[x][y][z] = value
    
    if code == '':
        return ''
    
    while i < len(code):
        
        command = code[i]
        
        if command not in ['F', 'B', 'R', 'L', 'U', 'D', '.', ',', '@', '#', '(', ')', '+', '~']:
            i += 1
            continue
        
        if command == '.':
            result += chr(get_cell(x, y, z) % 256)
            
        elif command == '@':
            value = get_cell(x, y, z)
            result += f'[{x},{y},{z}]={value} '
            
        elif command == 'F':
            px, py, pz = x, y, z
            x = (x + 1) % 50
        
        elif command == 'B':
            px, py, pz = x, y, z
            x = (x - 1) % 50
        
        elif command == 'R':
            px, py, pz = x, y, z
            y = (y + 1) % 50
        
        elif command == 'L':
            px, py, pz = x, y, z
            y = (y - 1) % 50
        
        elif command == 'U':
            px, py, pz = x, y, z
            z = (z + 1) % 50
        
        elif command == 'D':
            px, py, pz = x, y, z
            z = (z - 1) % 50

        elif command == '+':
            new_value = get_cell(x, y, z) + get_cell(px, py, pz)
            set_cell(x, y, z, new_value)
            set_cell(px, py, pz, 0)

        elif command == ',':
            if input_index < len(user_input):
                set_cell(x, y, z, ord(user_input[input_index]))
                input_index += 1
            else:
                set_cell(x, y, z, 0)
                
        elif command == '~':
            value = get_cell(x, y, z)
            set_cell(x, y, z, -value)
            
        elif command == '#':
            if get_cell(x, y, z) == 0:
                set_cell(x, y, z, 1)

        elif command == '(':
            neighbor = False
            
            dx = (x + 1) % 50
            dy = y
            dz = z
            if get_cell(dx, dy, dz) != 0:
                neighbor = True

            if not neighbor:
                dx = (x - 1) % 50
                dy = y
                dz = z
                if get_cell(dx, dy, dz) != 0:
                    neighbor = True

            if not neighbor:
                dx = x
                dy = (y + 1) % 50
                dz = z
                if get_cell(dx, dy, dz) != 0:
                    neighbor = True

            if not neighbor:
                dx = x
                dy = (y - 1) % 50
                dz = z
                if get_cell(dx, dy, dz) != 0:
                    neighbor = True

            if not neighbor:
                dx = x
                dy = y
                dz = (z + 1) % 50
                if get_cell(dx, dy, dz) != 0:
                    neighbor = True

            if not neighbor:
                dx = x
                dy = y
                dz = (z - 1) % 50
                if get_cell(dx, dy, dz) != 0:
                    neighbor = True

            if not neighbor:
                brackets = 1
                while brackets > 0:
                    i += 1
                    if i >= len(code):  
                        break
                    if code[i] == '(':
                        brackets += 1
                    elif code[i] == ')':
                        brackets -= 1

        elif command == ')':
            brackets = 1
            while brackets > 0:
                i -= 1
                if i < 0:
                    break
                if code[i] == ')':
                    brackets += 1
                elif code[i] == '(':
                    brackets -= 1
            
            continue
        
        
        i += 1
    
    return result

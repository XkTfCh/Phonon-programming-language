from PhononInterpreter import run_code

def test_debug():
    assert run_code('@', '') == '[0,0,0]=0 '

def test_movement_forward():
    assert run_code('FFF@', '') == '[3,0,0]=0 '

def test_movement_left():
    assert run_code('L@', '') == '[0,49,0]=0 '

def test_movement_up():
    assert run_code('U@', '') == '[0,0,1]=0 '


def test_absorption():
    assert run_code(',F+.B.', 'ABC') == 'A' + chr(0)

def test_growing():
    assert run_code('#@', '') == '[0,0,0]=1 '

def test_inversion():
    assert run_code(',~@', 'A') == '[0,0,0]=-65 '

def test_double_invertion():
    assert run_code('#~~@', '') == '[0,0,0]=1 '

def test_loop():
    assert run_code('#F(+)B@', '') == '[0,0,0]=0 '

def test_nested_loop():
    assert run_code('#F#R((+))@', '') == '[1,1,0]=1 '


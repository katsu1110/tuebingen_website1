if coord_x < road:
        toroad = road - coord_x
        if speed >= toroad + gap:
            step = "JUMP"
        else:
            if speed == gap:
                step = "WAIT"
            elif speed < gap:
                step = "SPEED"
            elif speed > gap:
                step = "SLOW"

    elif coord_x == road:
        step = "JUMP"

    elif coord_x >= road + gap:
        step = "SLOW" 

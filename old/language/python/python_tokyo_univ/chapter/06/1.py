def parabolic_m_step(y,x,vel_y,vel_x,stride):
    #x,x current position
    # vel vectle speed
    #stride time step

    g = 9.8
    y = y + vel_y * stride
    x = x + vel_x * stride
    vel_y = vel_y - g * stride

    return [y,x,vel_y,vel_x]

def parabolic_motion(y,x,vel_x,vel_y):
    stride = 0.3
    cur = [y,x,vel_y,vel_x]
    for i in range(0, 100):
        cur = parabolic_m_step(cur[0], cur[1],cur[2],cur[3],stride)
    return cur

print(parabolic_motion(10,10,2,-1,0.5))
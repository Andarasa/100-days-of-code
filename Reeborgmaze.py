def turn_right():
    turn_left()
    turn_left()
    turn_left()
def newall():
        if wall_on_right() and wall_in_front()== True:
            turn_left()
        elif front_is_clear() == True:
            move()
        elif right_is_clear() == True:
            turn_right()
            move()
        elif wall_on_right() == True:
            move()
        
        else:
            move()
while at_goal() != True:
    newall()   
else:
    pause()
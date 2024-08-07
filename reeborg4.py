def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def newall():
        if right_is_clear() and wall_in_front()== True:
            turn_right()
            move()
        elif wall_in_front() ==True:
            turn_left()
        
        elif wall_on_right() ==True:
            move()
        
        elif right_is_clear()== True:
            turn_right()
            move()
       
while at_goal() != True:
    newall()
    
else:
    pause()
    
from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    put_beeper_at_midpoint()

"""
Step:
Use beepers to find the midpoint
    let Karel put one beeper on the left side, and then right side
    the last spot will be midpoint
Clean the extra beepers   
"""


def put_beeper_at_midpoint():
    # handle case with one cell
    if front_is_blocked():
        put_beeper()
    else:
        put_beeper_on_each_side()
        if beepers_present():
            # if beeper is present, there are 2 columns so pick current beeper and move to other cell
            pick_beeper()
            turn_around()
            move()
        else:
            put_beepers_on_each_side()
            clean_extra_beepers()
            walk_to_middle_point()


def put_beeper_on_each_side():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()


# the end location would be the mid point
def put_beepers_on_each_side():
    while no_beepers_present():
        move()
        if beepers_present():
            turn_around()
            move()
            put_beeper()
            move()


def clean_extra_beepers():
    clean_beepers()
    while no_beepers_present():
        move()
    if beepers_present():
        move()
    clean_beepers()


def clean_beepers():
     while beepers_present():
         pick_beeper()
         if front_is_blocked():
             turn_around()
         else:
             move()


def walk_to_middle_point():
    while no_beepers_present():
        move()


def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

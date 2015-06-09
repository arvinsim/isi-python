# ==================================================
# Tale of Two Rockets
# ==================================================
import random
import math

class Rocket(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self):
        self.x += random.randrange(1, 100)
        self.y += random.randrange(1, 100)

    def get_distance(self, r):
        return math.sqrt(
           (r.x - self.x)**2 +
           (r.y - self.y)**2
        )

agm_80_viper = Rocket()
sky_sword_2 = Rocket(10, 10)

print agm_80_viper.get_distance(sky_sword_2)

# ==================================================
# Challenging
# ==================================================

class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coordinate({},{})".format(self.x, self.y)


class Person(object):
    def __init__(self, start, end, obstacles):
        self.current_position = start
        self.destination = end

    def obstacle_check(self):
        pass

    def print_if_at_destination(self):
        if (self.current_position.x == self.destination.x
                and self.current_position.y == self.destination.y):
            print "I have arrived!"

    def move_up(self):
        self.current_position.y -= 1
        self.print_if_at_destination()

    def move_down(self):
        self.current_position.y += 1
        self.print_if_at_destination()

    def move_left(self):
        self.current_position.x -= 1
        self.print_if_at_destination()

    def move_right(self):
        self.current_position.x += 1
        self.print_if_at_destination()


start = Coordinate(0, 0)
end = Coordinate(2, 2)
obstacles = [Coordinate(2,1)]

p = Person(start, end, obstacles)
p.move_right()
p.move_right()
p.move_down()
p.move_right()
p.move_down()
p.move_down()
p.move_left()

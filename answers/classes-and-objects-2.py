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
        return math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2)

agm_80_viper = Rocket()
sky_sword_2 = Rocket(10, 10)

print agm_80_viper.get_distance(sky_sword_2)

# ==================================================
# Challenging Exercises
# ==================================================


class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coordinate({},{})".format(self.x, self.y)


class Boundary(object):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def is_out_of_bounds(self, coordinate):
        if (self.x1 <= coordinate.x <= self.x2 and
                self.y1 <= coordinate.y <= self.y2):
            return False
        else:
            return True


class Person(object):
    def __init__(self, start, end, obstacles, boundary):
        self.current_position = start
        self.destination = end
        self.obstacles = obstacles
        self.boundary = boundary
        self.show_current_position()

    def is_obstacle(self, coordinate):
        for obstacle_coordinate in self.obstacles:
            if (coordinate.x == obstacle_coordinate.x and
                    coordinate.y == obstacle_coordinate.y):
                return True
        return False

    def is_destination(self, coordinate):
        if (coordinate.x == self.destination.x
                and coordinate.y == self.destination.y):
            return True
        else:
            return False

    def is_current_position(self, coordinate):
        if (coordinate.x == self.current_position.x
                and coordinate.y == self.current_position.y):
            return True
        else:
            return False

    def move_to(self, coordinate):
        if self.is_obstacle(coordinate):
            print "I hit an obstacle!"
        elif self.boundary.is_out_of_bounds(coordinate):
            print "I hit the boundary"
        elif self.is_destination(coordinate):
            self.current_position = coordinate
            print "I have arrived!"
        else:
            self.current_position = coordinate

    def show_current_position(self):
        map_length = {
            'x': max(self.boundary.x1, self.boundary.x2) + 1,
            'y': max(self.boundary.y1, self.boundary.y2) + 1
        }

        print "     "
        for y in range(map_length['y']):
            line = "    "
            for x in range(map_length['x']):
                current_coordinate = Coordinate(x, y)
                if self.is_obstacle(current_coordinate):
                    line += " O"
                elif self.is_destination(current_coordinate):
                    line += " D"
                elif self.is_current_position(current_coordinate):
                    line += " P"
                else:
                    line += " -"
            print line
        print "     "

    def move_up(self):
        self.move_to(Coordinate(
            self.current_position.x,
            self.current_position.y - 1
        ))
        self.show_current_position()

    def move_down(self):
        self.move_to(Coordinate(
            self.current_position.x,
            self.current_position.y + 1
        ))
        self.show_current_position()

    def move_left(self):
        self.move_to(Coordinate(
            self.current_position.x - 1,
            self.current_position.y
        ))
        self.show_current_position()

    def move_right(self):
        self.move_to(Coordinate(
            self.current_position.x + 1,
            self.current_position.y
        ))
        self.show_current_position()


start = Coordinate(0, 0)
end = Coordinate(2, 2)
obstacles = [Coordinate(2, 1)]
boundary = Boundary(0, 3, 0, 3)

p = Person(start, end, obstacles, boundary)
p.move_right()
p.move_right()
p.move_down()
p.move_right()
p.move_right()
p.move_down()
p.move_down()
p.move_left()

class CarMovement():

    temp_dict = {}  # another dict for storage just as a class variable

    def __init__(self, x, y, distance, axis):
        self.x = x
        self.y = y
        self.distance = distance
        self.axis = axis

    def set_x_direction(self):
        direction = self.x + 1
        return direction

    def set_y_direction(self):
        direction = self.y + 1
        return direction

    def get_direction(self, direction):
        """
        Because tuples are immutable, I need to store the current direction in a dict
        """
        current_direction = {}
        current_direction['direction'] = direction
        CarMovement.temp_dict['direction'] = current_direction.get('direction')
        return current_direction.get('direction')

    def forward_x(self):
        self.x = self.x + self.distance

    def forward_y(self):
        self.y = self.y + self.distance

    def reverse_x(self):
        self.x = self.x - self.distance

    def reverse_y(self):
        self.y = self.y - self.distance

    """
    Since it is a car, I'm looking at the travel
    only being linearly. Obviously that is not the
    case in reality, but since it is on a grid, I
    decided to approach it that way. More cases
    would need to be added.
    """

    def turn_left(self):
        if self.axis == 'x' and self.x >= 0:
            direction = CarMovement.set_y_direction(self)
            CarMovement.get_direction(self, direction)
        if self.axis == 'y' and self.x < 0:
            direction = CarMovement.set_x_direction(self) * -1
            CarMovement.get_direction(self, direction)
        if self.axis == 'y' and self.y < 0:
            direction = CarMovement.set_x_direction(self) * -1
            CarMovement.get_direction(self, direction)

    def turn_right(self):
        if self.axis == 'x' and self.x >= 0:
            direction = CarMovement.set_y_direction(self) * -1
            CarMovement.get_direction(self, direction)
        if self.axis == 'y' and self.x >= 0:
            direction = CarMovement.set_x_direction(self)
            CarMovement.get_direction(self, direction)
        if self.axis == 'y' and self.y < 0:
            direction = CarMovement.set_x_direction(self)
            CarMovement.get_direction(self, direction)

    def current_coordinates(self):
        tuple = (self.x, self.y, CarMovement.temp_dict.get('direction'))
        return tuple


class TestCar():
    """
    More cases could be added (e.g. reverse along x-axis)
    """

    def test_forward_right_turn(self):
        car = CarMovement(0, 0, 3, 'x')
        car.forward_x()
        car.turn_right()
        assert car.current_coordinates()[0] == 3
        assert car.current_coordinates()[1] == 0
        assert car.current_coordinates()[2] == -1

    def test_reverse_left_turn(self):
        car = CarMovement(0, 0, 3, 'y')
        car.reverse_y()
        car.turn_left()
        assert car.current_coordinates()[0] == 0
        assert car.current_coordinates()[1] == -3
        assert car.current_coordinates()[2] == -1

    def test_forward_left_turn(self):
        car = CarMovement(0, 0, 3, 'x')
        car.forward_x()
        car.turn_left()
        assert car.current_coordinates()[0] == 3
        assert car.current_coordinates()[1] == 0
        assert car.current_coordinates()[2] == 1

    def test_reverse_right_turn(self):
        car = CarMovement(0, 0, 6, 'y')
        car.reverse_y()
        car.turn_right()
        assert car.current_coordinates()[0] == 0
        assert car.current_coordinates()[1] == -6
        assert car.current_coordinates()[2] == 1

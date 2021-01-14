class CarPark:
    def __init__(self, length):
        if length < 1:
            raise ValueError('CarPark length must be greater or equal to 1')
        self._spaces = [None for i in range(length)]

    def get_available_spaces(self, position):
        start_position = position
        space = self._spaces[position]
        while space is None and position < len(self._spaces):
            position += 1
            if position < len(self._spaces):
                space = self._spaces[position]
        return position - start_position

    def park_vehicle(self, length, uid):
        if uid in self._spaces:
            raise ValueError('Car with same uid already parked here')
        space_index = 0
        while space_index < len(self._spaces):
            no_of_spaces = self.get_available_spaces(space_index)
            if no_of_spaces >= length:
                for i in range(space_index, space_index + length):
                    self._spaces[i] = uid
                return space_index
            else:
                space_index += no_of_spaces + 1
        return -1

    def remove_vehicle(self, uid):
        index = 0
        found = False
        while index < len(self._spaces):
            if self._spaces[index] == uid:
                if not found:
                    found = True
                self._spaces[index] = None
            else:
                if found:
                    return True
            index += 1
        return False

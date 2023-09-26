from random import choice, randint
from time import sleep


class Vacuum:

    @staticmethod
    def suck(location: str, status: str, *args, **kwargs):
        print(f'location {location} is {status}, vacuum is going to clean it!')
        time = randint(1, 4)
        while time:
            print(f'Vacuum is cleaning location {location}!\n{time} seconds left!')
            time -= 1
            sleep(1)
        print(f'location {location} has been cleaned!')

    @staticmethod
    def move(location: str, direction: str, status: str, *args, **kwargs):
        print(f'location {location} is {status}, vacuum has moved to the {direction}!')


class Location:
    def __call__(self, *args, **kwargs):
        location = choice(('A', 'B'))
        status = choice(('Dirty', 'Clean'))
        print(f'Location({location=} {status=})')
        return location, status


def reflex_vacuum_agent(location: str, status: str) -> object:
    vacuum = Vacuum()
    if status.lower() == 'dirty':
        return vacuum.suck(location=location, status=status.lower())
    if location.lower() == 'a':
        return vacuum.move(location=location, direction='right', status=status.lower())
    return vacuum.move(location=location, direction='left', status=status.lower())


# def main():
#     location_instance = Location()
#     location, status = location_instance()
#     reflex_vacuum_agent(location=location, status=status)
#
#
# if __name__ == '__main__':
#     main()

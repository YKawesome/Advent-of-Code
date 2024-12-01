from collections import namedtuple

DrawComposition = namedtuple('DrawComposition', ['reds', 'greens', 'blues'])
Game = namedtuple('Game', ['id', 'draw_compositions'])

_REDS_IN_BAG = 12
_GREENS_IN_BAG = 13
_BLUES_IN_BAG = 14


def split_cube_string_to_tuple(string: str) -> tuple[str, int]:
    '''Splits a cube string into a tuple of the color and the number of cubes'''
    split = string.split(' ')
    num = int(split[0])
    color = split[1]
    return (color, num)


def make_draw_composition(string: str) -> DrawComposition:
    '''Makes a DrawComposition'''
    comp_list = string.split(', ')
    comp_dict = {}
    for comp in comp_list:
        color, num = split_cube_string_to_tuple(comp)
        comp_dict[color] = num

    if 'red' in comp_dict:
        reds = comp_dict['red']
    else:
        reds = 0
    if 'green' in comp_dict:
        greens = comp_dict['green']
    else:
        greens = 0
    if 'blue' in comp_dict:
        blues = comp_dict['blue']
    else:
        blues = 0

    return DrawComposition(reds, greens, blues)


def split_data_line(data: str) -> list[DrawComposition]:
    '''Splits a data line into a list of DrawCompositions'''
    draws = data.split('; ')
    draw_compositions = [make_draw_composition(draw) for draw in draws]

    return draw_compositions


def split_input_line(line: str) -> Game:
    '''Splits an input line into a Game'''
    split = line.strip().split(': ')
    id = int(split[0].split(' ')[1])
    data = split[1]
    draw_compositions = split_data_line(data)

    return Game(id, draw_compositions)


def required_draw_composition(game: Game) -> DrawComposition:
    '''Returns the minimum number of each cubes for each game to be
    possible; this means taking the highest amount of cubes from each color
    in every draw'''
    reds = 0
    greens = 0
    blues = 0

    for draw_comp in game.draw_compositions:
        reds = max(reds, draw_comp.reds)
        greens = max(greens, draw_comp.greens)
        blues = max(blues, draw_comp.blues)

    return DrawComposition(reds, greens, blues)


def get_power_of_set_of_cubes(draw_comp: DrawComposition) -> int:
    return draw_comp.reds * draw_comp.greens * draw_comp.blues


def run() -> None:
    '''Runs the program'''
    f = open('Day 02/day2.txt', 'r')
    sum = 0
    for line in f:
        game = split_input_line(line)
        sum += get_power_of_set_of_cubes(required_draw_composition(game))
    print(sum)


if __name__ == '__main__':
    run()

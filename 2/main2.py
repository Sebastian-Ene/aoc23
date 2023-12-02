import requests
import math

default_extraction = {
    "blue": 0,
    "red": 0,
    "green": 0
}


def get_input_data(url: str, file_path: str) -> str:
    try:
        req = requests.get(url,
                           headers={
                               "Cookie": "_ga=GA1.2.964804608.1701523793; _gid=GA1.2.388216194.1701523793; session=53616c7465645f5f4e5c71a61d8a5f947f0f5cc2a71d3591f5ee2427f581883f0179fa2c3f640b352971bdbf97bb7371862d13e3d972177de0c754667856a852; _ga_MHSNPJKWC7=GS1.2.1701523793.1.1.1701523810.0.0.0"
                           })
        input = req.text
    except Exception as e:
        print(e)
        print("Didn't manage to fetch input data. Reading from file instead.")
        # TODO: implement this
    return input


def parse_game_input(game: str) -> list:
    print('-------------')
    print(game)
    game_input = game.split(': ')[1]
    # print(game_input)
    list_of_extractions = game_input.split('; ')
    # print(list_of_extractions)
    parsed_extractions = []
    for extraction in list_of_extractions:
        extracted_colors = extraction.split(', ')
        # print(extracted_colors)
        extraction_dict = default_extraction.copy()
        for extracted_color in extracted_colors:
            # TODO: here might want to make sure there's no bad input going on
            extraction_dict[extracted_color.split(' ')[1]] = int(
                extracted_color.split(' ')[0])
        parsed_extractions.append(extraction_dict)
    print(parsed_extractions)
    return parsed_extractions


def main():
    input = get_input_data(url='https://adventofcode.com/2023/day/2/input',
                           file_path='./input.txt')
    list_of_games = input.split('\n')[0:-1]
    sum_of_powers = 0
    # print(len(list_of_games))
    for game in list_of_games:
        needed_for_game = default_extraction.copy()
        parsed_list_of_extractions = parse_game_input(game)
        for extraction in parsed_list_of_extractions:
            for color, number in extraction.items():
                needed_for_game[color] = max(needed_for_game[color], number)
        print(needed_for_game)
        sum_of_powers += math.prod(needed_for_game.values())

    print(sum_of_powers)


main()

# tried answers:
# 56322 - bingo

# TODO:
#       1. Create a module with common functionality (like get input_data)
#       2. Refactor the code for day 2
#       3. Add unit tests
#       4. Improve performance (don't need to parse the things twice, can get the data first run)

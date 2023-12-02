import requests

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


def get_game_id(game: str) -> int:
    game_info = game.split(":")[0]
    game_id = game_info.split(' ')[1]
    return int(game_id)


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
    # print(len(list_of_games))
    game_ids_sum = 0
    for game in list_of_games:
        valid_game = True
        game_id = get_game_id(game)
        parsed_list_of_extractions = parse_game_input(game)
        for extraction in parsed_list_of_extractions:
            if extraction["red"] > 12 or extraction["green"] > 13 or extraction["blue"] > 14:
                valid_game = False
                break
        if valid_game:
            game_ids_sum += game_id
    print(game_ids_sum)


main()
# parse_game_input('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')


# tried answers
# 4239 -> too big, added the ids too many times because:
#   1. I added invalid ids instead of valid ones
#   2. Was adding them for each invalid extraction, instead of every game
# 2447 -> bingo :D

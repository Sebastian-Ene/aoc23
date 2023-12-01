import requests

numbers = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9"
}

MAX_NUMBER_OF_LETTERS_IN_A_DIGIT = 5

def run_suite(suite):
    final_sum = 0
    for line in suite:
        numb = replace_string_with_digit(line)
        # numb = parse_line(updated_line)
        print(f'{line} -> {numb}')
        final_sum += numb
    return final_sum

def parse_line(line: str) -> int:
    first_int_char = '0'
    last_int_char = '0'
    for el in line:
        if el.isdigit():
            first_int_char = el
            break
    for el in line[-1::-1]:
        if el.isdigit():
            last_int_char = el
            break
    return int(first_int_char + last_int_char)

def replace_string_with_digit(line: str) -> str:
    # print('\n--------------')
    first_int_char = '0'
    last_int_char = '0'
    # change first string 
    stop = False
    for i in range(len(line)):
        if stop:
            break
        if line[i].isdigit():
            # print('nu')
            first_int_char = line[i]
            stop=True
            break
        for j in range(i+1, min(len(line)+1, i + 1 + MAX_NUMBER_OF_LETTERS_IN_A_DIGIT)):
            substr=line[i:j]
            # print(substr)
            if substr in numbers.keys():
                # line = line.replace(substr,numbers[substr], 1)
                first_int_char = numbers[substr]
                
                stop=True
                break


    # change last string
    stop = False
    for i in range(len(line)-1,0,-1):
        # print(f'i={i}')
        if stop:
            break
        if line[i].isdigit():
            last_int_char = line[i]
            # print('dont')
            stop=True
            break
        for j in range(i, len(line)+1):
            # print(f'j={j}')

            substr=line[i:j]
            # print(substr)
            if substr in numbers.keys():
                # line = line[:i] + numbers[substr]
                last_int_char = numbers[substr]
                stop = True
                break

        # print(f'replacing {digit_str} with {digit_int}')
        # line = line.replace(digit_str, digit_int)
        # print(line)
        # print("---------------\n")
    if first_int_char == "0" and last_int_char =="0":
        return 0
    elif first_int_char == "0":
        return int(last_int_char*2)
    elif last_int_char == "0":
        return int(first_int_char*2)
    return int(first_int_char + last_int_char)

def main():
    try:
    # haha that's my session token and you can hack my aoc account hehexd
        req = requests.get('https://adventofcode.com/2023/day/1/input',
                    headers= {
						'Cookie': '_ga=GA1.2.1360020121.1701423703; _gid=GA1.2.1042369911.1701423703; ru=53616c7465645f5f88e1c5367b8f730a8b866a45af73897a495120bb9c5c448f; session=53616c7465645f5f5a54dc9a02fb9a4c7686d1f8f1fe94e1628f04a1e05bff3717c8bce6aa4fd055ee84a525c3aa6fcbcf83ed8897bad9adda1e736159f9f91f; _ga_MHSNPJKWC7=GS1.2.1701423702.1.1.1701426454.0.0.0'
					})
        input = req.text
    except Exception as e:
        pass
	#     print(e)
    # with open('./input.txt', mode='rt') as file:
    #         input = file.readlines()
    #     print(input)

    list_of_lines = input.split('\n')
    print(len(list_of_lines))

    print(run_suite(list_of_lines))

test_suite_of_doom=[
	"",
	"1",
	"q",
	"one",
	"1two",
	"one2",
	"twone",
 	"atwone",
  	"twonea",
   	"1twone",
    "twone2",
    "3twone4",
    "seven",
    "nine",
    "eight",
    # working till here
    "two1nine",
    'eightwothree',
    "abcone2threexyz",
    'xtwone3four',
    "4nineeightseven2",
    'zoneight234',
    '7pqrstsixteen'
]
main()

# print(replace_string_with_digit('abcone2threexyz'))

# print(run_suite(test_suite_of_doom))

# tried answers
# 53522
# 53538
# 53312 - bingo

# TODO: revise the code
# better indicess handling will allow for removal of the last ifs.
# code quality is bad, need to rename functions, delete functions and reorganize stuff
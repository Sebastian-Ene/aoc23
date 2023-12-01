import requests

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

try:
    # haha that's my session token and you can hack my aoc account hehexd
	req = requests.get('https://adventofcode.com/2023/day/1/input',
                    headers= {
						'Cookie': '_ga=GA1.2.1360020121.1701423703; _gid=GA1.2.1042369911.1701423703; ru=53616c7465645f5f88e1c5367b8f730a8b866a45af73897a495120bb9c5c448f; session=53616c7465645f5f5a54dc9a02fb9a4c7686d1f8f1fe94e1628f04a1e05bff3717c8bce6aa4fd055ee84a525c3aa6fcbcf83ed8897bad9adda1e736159f9f91f; _ga_MHSNPJKWC7=GS1.2.1701423702.1.1.1701426454.0.0.0'
					})
	input = req.text
except Exception as e:
	print(e)
	with open('./input.txt', mode='rt') as file:
		input = file.readlines()
		print(input)

list_of_lines = input.split('\n')
print(len(list_of_lines))

final_sum = 0
for line in list_of_lines:
    numb = parse_line(line)
    print(f'{line}:  {numb}')
    final_sum += numb
print(final_sum)






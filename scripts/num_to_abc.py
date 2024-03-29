#!/usr/bin/env python3

import sys

global standard_dict
standard_dict = {
	'00': 'a', '01': 'b', '02': 'c', '03': 'd', '04': 'e', '05': 'f', '06': 'g', '07': 'h',
	'08': 'i', '09': 'j', '10': 'k', '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q',
	'17': 'r', '18': 's', '19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z'
}

def main():
	num = sys.argv[1]

	print(convert_num(num))

def convert_num(num, key_dict = standard_dict, gap = 2):
	message = ''
	for j in range(0, len(num), gap):
		message += key_dict[num[j:j+gap]]
	return message

if __name__ == '__main__':
	main()

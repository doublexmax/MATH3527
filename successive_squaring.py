#!/usr/bin/env python3

import math
import sys

def break_into_bits(n):
        bin_transf = bin(n).replace('0b','')[::-1]

        ones = []
        square_counter = 1

        for char in bin_transf:
                if int(char):
                        ones.append(square_counter)
                square_counter = square_counter << 1

        return ones

def main():
        """
                Solve: a^b (mod m)
                Using successive squaring
        """
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        modulo = int(sys.argv[3])

        ones = break_into_bits(b)

        squares = successively_square(a, ones[-1], modulo)

        num = (squares[ones[0]])

        for bit in ones[1:]:
                num = (num * squares[bit]) % modulo

        print(squares, "all squares")
        print(ones, "bits used")
        print(num, 'answer')


def successively_square(a, b, modulo):
        squares = {}

        num = a % modulo
        square_counter = 1
        for _ in range(int(math.log(b)/math.log(2))+1):
                #print(num)
                squares[square_counter] = num
                square_counter = square_counter << 1
                num = (num ** 2) % modulo

        return squares


if __name__ == '__main__':
        main()

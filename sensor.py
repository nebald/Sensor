#!/usr/bin/env python3

class Sensor:
    name = "python"

    def generate_data(self, columns, rows, frames):

        array_size = columns * rows
        chunk = bytearray(array_size)

        for i in range(0, array_size):
            chunk[i] = i
            i += 1

        print(chunk)


if __name__ == '__main__':

    try:
        ic = Sensor()

        ic.generate_data(2, 2, 1)

    except:
        print("There's a problem with your code. Write better code!")

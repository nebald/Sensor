#!/usr/bin/env python3

class Sensor:
    name = "python"
    columns = 0
    rows = 0

    def generate(self, frames):

        array_size = self.columns * self.rows
        chunk = bytearray(array_size)

        for i in range(0, array_size):
            chunk[i] = i
            i += 1
        return chunk

    def print(self, chunk):

        print_data = bytearray(self.columns)
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                print_data[j] = chunk[self.columns * i + j]
            print(str(print_data))


if __name__ == '__main__':

    try:
        ic = Sensor()
        ic.columns = 4
        ic.rows = 4
        chunk = ic.generate(1)
        ic.print(chunk)

    except:
        print("There's a problem with your code. Write better code!")

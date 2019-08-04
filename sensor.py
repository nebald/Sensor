#!/usr/bin/env python3
import array
import os
import sys

class Sensor:
    name = "python"
    columns = 0
    rows = 0
    frames = 0

    def generate(self):

        sensor_size = self.columns * self.rows
        array_size = sensor_size * self.frames
        chunk = array.array('H', (0 for i in range(array_size)))

        for j in range(0, self.frames):
            for i in range(0, sensor_size):
                chunk[j * sensor_size + i] = j * 256 + i

        return chunk

    def print(self, chunk):

        sensor_size = self.columns * self.rows
        array_size = sensor_size * self.frames
        print_data = array.array('H', (0 for i in range(self.columns)))
        for k in range(0, self.frames):
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    print_data[j] = chunk[k * sensor_size + self.columns * i + j]
                print(print_data)

    def savefile(self, file_name, chunk):
        try:
            with open(file_name, "wb") as f:
                f.write(chunk)
                f.close()

        except:
            print("file save error")


if __name__ == '__main__':

    try:
        ic = Sensor()
        ic.columns = 4
        ic.rows = 4
        ic.frames = 2
        chunk = ic.generate()
        ic.print(chunk)
        ic.savefile('TestSave.bin', chunk)

    except:
        print("There's a problem with your code. Write better code!")



# -*- coding: utf-8 -*-

"""Overview:
    Displays the solution results of the Solitaire Klondike-Solver in order.

Usage:
    python pySolitaireResultSimulation.py <result_file> <disp_dirrection> [enable_wait_enterkey [wait_time]]

Options:
    result_file : Specify the Klondike-Solver result file.
    disp_dirrection :
        -v ... display overlap verticaly. (default)
        -h ... display overlap horizontaly.
    enable_wait_enterkey  : stop on each turn and continue with enter key enable. (defalut=false)
    wait_time   : wait time(ms) for enable_wait_enterkey. (defalut=0[ms])

Execute Example:
    $ python Solitaire_Simulation.py ./game_results/G00001.txt
    $ python Solitaire_Simulation.py ./game_results/G00002.txt -v true
    $ python Solitaire_Simulation.py ./game_results/G00003.txt -v false 100
    $ python Solitaire_Simulation.py ./game_results/G00004.txt -h true
    $ python Solitaire_Simulation.py ./game_results/G00005.txt -h false 100

Remarks:
    Solitaire result files are obtained using Klondike-Solver /MVS option.
    https://github.com/ShootMe/Klondike-Solver

    Example)
    $ git clone https://github.com/ShootMe/Klondike-Solver
    $ cd Klondike-Solver
    $ make
    $ cp ./KlondikeSolver ..
    $ cd ..
    $ ./KlondikeSolver /G 1 /MVS > 1.txt
    $ python pySolitaireResultSimulation.py 1.txt
"""

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def __init__(self, contents : List[str]) -> int:
        # replace LF
        for i, text in  enumerate(contents):
            contents[i] = contents[i].replace("\n", "")

        # set deck.
        self.deck = []
        for i in range(0, 8):
            flds = contents[i].split(": ")
            if int(flds[0]) != i:
                print("format error...")
                return 1
            self.deck.append(flds[1].replace(" ", "").split("-"))

        self.deck[1].append("")
        for i in range(2, 8):
            self.deck[i] = self.deck[i][:1] + [""] + self.deck[i][1:]

        # set mountain.
        flds = contents[8].strip().split(": ")
        self.mount = flds[1].split(" ")

        self.resolv = contents[16].split(" ")
        self.wast = []
        self.s, self.h, self.d, self.c = [], [], [], []

    """
    print deck and resolv
    """
    def print_deck(self, disp_dirrection : str) -> None:
        if disp_dirrection == "-h":
            self.print_deck_horizen()
        else:
            self.print_deck_vertical()


    def print_deck_vertical(self) -> None:
        for i in range(8):
            print("{0:2d}: {1}".format(i, self.deck[i]))
        print(" m :{0}".format(self.mount))
        print(" w :{0}".format(self.wast))
        print("----------------------------------------------------------------------------------")
        print(" s :{0}".format(self.s))
        print(" h :{0}".format(self.h))
        print(" d :{0}".format(self.d))
        print(" c :{0}".format(self.c))
        print("----------------------------------------------------------------------------------")
    #   print("resolv = {0}¥n".format(resolv))
    #   print("----------------------------------------------------------------------------------")


    def print_deck_horizen(self) -> None:
        print("---+---------------+------------------\n" \
              "     s   h   d   c    m        w\n" \
              "---+---------------+------------------")
        for i in range(0, 13):
            line = "{0:-2d} : ".format(i)
            if i < len(self.s):
                line += "{0:4}".format(self.s[i])
            else:
                line += "    "

            if i < len(self.h):
                line += "{0:4}".format(self.h[i])
            else:
                line += "    "

            if i < len(self.d):
                line += "{0:4}".format(self.d[i])
            else:
                line += "    "

            if i < len(self.c):
                line += "{0:4}".format(self.c[i])
            else:
                line += "    "

            line += " "
            if len(self.mount) > 13:
                line += "{0:4}".format(self.mount[len(self.mount) - 1 - i])
                if i + 13 < len(self.mount):
                    line += "{0:4}".format(self.mount[len(self.mount) - 1 - (i + 13)])
                else:
                    line += "    "
            else:
                if i < len(self.mount):
                    line += "{0:8}".format(self.mount[len(self.mount) - 1 - i])
                else:
                    line += "        "

            line += " "
            if len(self.wast) > 13:
                line += "{0:4}".format(self.wast[len(self.wast) - 1 - i])
                if i + 13 < len(self.wast):
                    line += "{0:4}".format(self.wast[len(self.wast) - 1 - (i + 13)])
                else:
                    line += "    "
            else:
                if i < len(self.wast):
                    line += "{0:8}".format(self.wast[len(self.wast) - 1 - i])
                else:
                    line += "        "

            print(line)

        max_deck_len = 0
        for i, _ in enumerate(self.deck):
            max_deck_len = max(max_deck_len, len(self.deck[i]))


        print("---+-----------------------------------\n" \
              "     [0] [1] [2] [3] [4] [5] [6] [7]\n" \
              "---+-----------------------------------")
        for j in range(max_deck_len):
            line = "{0:-2d} : ".format(j)
            for i in range(0, 8):
                if j < len(self.deck[i]):
                    if self.deck[i][len(self.deck[i]) - 1 - j] == "":
                        line += "--  "
                    else:
                        line += "{0:4}".format(self.deck[i][len(self.deck[i]) - 1 - j])
                else:
                    line += "    "
            print(line)
        print("---+-----------------------------------")


    def solitaire_result_simulation(self, disp_dirrection, enable_wait_enterkey : bool, wait_time : int) -> int:
        self.print_deck(disp_dirrection)

        for turn, ope in enumerate(self.resolv):
            print("turn = {0}, next = \"{1}\"".format(turn, ope))

            if enable_wait_enterkey:
                input("Hit Enter key.")
            else:
                time.sleep(wait_time/1000)

            if ope[:2] == "DR":
                draw_cnt = int(ope[2:])
                temp = ["" for _ in range(draw_cnt)]
                for pos in range(0, draw_cnt):
                    temp[draw_cnt - pos - 1] = self.mount[pos]
                self.mount = self.mount[draw_cnt:]
                self.wast = temp + self.wast

            elif ope == "NEW":
                self.mount = []
                for i in range(len(self.wast) - 1, -1, -1):
                    self.mount.append(self.wast[i])
                self.wast = []

            elif ope[:1] == "F":
                target_deck = int(ope[1:])
                if self.deck[target_deck][0] == "":
                    self.deck[target_deck] = [self.deck[target_deck][1]] + [""] + self.deck[target_deck][2:]
                else:
                    self.deck[target_deck] = [""] + self.deck[target_deck][1:]

            elif ope.isdecimal():
                src, dst = int(ope[:1]), int(ope[1:])
                self.deck[dst] = [self.deck[src][0]] + self.deck[dst]
                self.deck[src] = self.deck[src][1:]

            elif ope[:1] == "W":
                if ope[1:].isdecimal():
                    target_deck = int(ope[1:])
                    self.deck[target_deck] = [self.wast[0]] + self.deck[target_deck]
                    self.wast = self.wast[1:]
                else:
                    suit = ope[1]
                    if suit == "S":
                        self.s.append(self.wast[0])
                    elif suit == "H":
                        self.h.append(self.wast[0])
                    elif suit == "D":
                        self.d.append(self.wast[0])
                    elif suit == "C":
                        self.c.append(self.wast[0])
                    self.wast = self.wast[1:]

            elif "-" in ope:
                src = int(ope[0])
                dst = int(ope[1])
                cnt = int(ope[3])
                self.deck[dst] = self.deck[src][:cnt] + self.deck[dst]
                self.deck[src] = self.deck[src][cnt:]
                
            elif ope[:1].isdecimal():
                src = int(ope[0])
                suit = ope[1]
                if suit == "S":
                    self.s.append(self.deck[src][0])
                elif suit == "H":
                    self.h.append(self.deck[src][0])
                elif suit == "D":
                    self.d.append(self.deck[src][0])
                elif suit == "C":
                    self.c.append(self.deck[src][0])
                self.deck[src] = self.deck[src][1:]

            elif ope == "":
                pass

            else:
                print("{0} not define.".format(next))
                return -1

            self.print_deck(disp_dirrection)

        return 0


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <result_file> <-v | -h> [enable_wait_enterkey [wait_time]]".format(argv[0]))
        print("\n" \
              "Example)\n" \
              "$ python Solitaire_Simulation.py ./game_results/G00001.txt\n" \
              "$ python Solitaire_Simulation.py ./game_results/G00002.txt -v true\n" \
              "$ python Solitaire_Simulation.py ./game_results/G00003.txt -v false 100\n" \
              "$ python Solitaire_Simulation.py ./game_results/G00004.txt -h true\n" \
              "$ python Solitaire_Simulation.py ./game_results/G00005.txt -h false 500")
        exit(1)

    disp_dirrection = "-h"
    if argc >= 3:
        if argv[2] == "-v":
            disp_dirrection = "-v"

    enable_wait_enterkey = False
    if argc >= 4:
        if argv[3].upper() == "TRUE":
            enable_wait_enterkey = True

    wait_time = 0
    if argc >= 5:
        if argv[4].isdecimal():
            wait_time = int(argv[4])

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    contents = testDataFile.readlines()

    sl = Solution(contents)
    time0 = time.time()

    result = sl.solitaire_result_simulation(disp_dirrection, enable_wait_enterkey, wait_time)

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

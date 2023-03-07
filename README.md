# pySolitaireResultSolution

Displays the solution results of the Solitaire Klondike-Solver in order.

Solitaire result files are obtained using Klondike-Solver /MVS option.<br>
https://github.com/ShootMe/Klondike-Solver


## 1. Build the Klondike-Solver and pySolitaireResultSimulation execute.

```
$ git clone https://github.com/ShootMe/Klondike-Solver
$ cd Klondike-Solver
$ make
$ cp ./KlondikeSolver ..
$ cd ..
$ ./KlondikeSolver /G 1 /MVS > 1.txt
$ python pySolitaireResultSimulation.py 1.txt
```

## 2. Usage

```
$ python pySolitaireResultSimulation.py <result_file> <disp_dirrection> [enable_wait_enterkey [wait_time]]
```

## 3. Options

|option|remark|
|---|---|
|result_file|Specify the Klondike-Solver result file.|
|disp_dirrection|-v ... display overlap verticaly. (default)|
||-h ... display overlap horizontaly.|
|enable_wait_enterkey|stop on each turn and continue with enter key enable. (defalut=false)|
|wait_time|wait time(ms) for enable_wait_enterkey. (defalut=0[ms])|

## 4. Execute command examples

### 4-1. Execute command example1

Display overlap horizontaly and enable_wait_enterkey.

```
$ python Solitaire_Simulation.py ./game_results/G00001.txt
...
...
$ python Solitaire_Simulation.py ./game_results/G00002.txt -v true
...
...
$ python Solitaire_Simulation.py ./game_results/G00003.txt -v false 100
...
...
$ python Solitaire_Simulation.py ./game_results/G00004.txt -h true
...
...
$ python Solitaire_Simulation.py ./game_results/G00005.txt -h false 100
...
...
```

### 4-2. Execute command example2

Display overlap verticaly and enable_wait_enterkey.

```
$ python pySolitaireResultSimulation.py ./game_results/G00001.txt -v true
 0: ['']
 1: ['4D', '']
 2: ['4C', '', '3C']
 3: ['6H', '', '7D', '9S']
 4: ['JD', '', '2C', '7S', 'AH']
 5: ['AS', '', 'TS', '2H', '6S', 'AD']
 6: ['5C', '', 'JC', 'KS', '2D', '8H', '4H']
 7: ['KD', '', '6C', 'JH', '5D', '3S', '4S', '3H']
 m :['9D', 'TC', '2S', 'QC', 'KH', '5S', '9C', 'AC', 'QH', 'QD', '8S', '6D', '7C', '9H', 'JS', 'QS', '8C', '5H', 'TD', '3D', 'KC', '7H', '8D', 'TH']
 w :[]
----------------------------------------------------------------------------------
 s :[]
 h :[]
 d :[]
 c :[]
----------------------------------------------------------------------------------
turn = 0, next = "5S"
Hit Enter key.
    ...
    ...
turn = 121, next = ""
Hit Enter key.
---+---------------+------------------
     s   h   d   c    m        w
---+---------------+------------------
 0 : AS  AH  AD  AC
 1 : 2S  2H  2D  2C
 2 : 3S  3H  3D  3C
 3 : 4S  4H  4D  4C
 4 : 5S  5H  5D  5C
 5 : 6S  6H  6D  6C
 6 : 7S  7H  7D  7C
 7 : 8S  8H  8D  8C
 8 : 9S  9H  9D  9C
 9 : TS  TH  TD  TC
10 : JS  JH  JD  JC
11 : QS  QH  QD  QC
12 : KS  KH  KD  KC
---+-----------------------------------
     [0] [1] [2] [3] [4] [5] [6] [7]
---+-----------------------------------
 0 : --  --  --  --  --  --  --  --
---+-----------------------------------
Execute time ... : x.xxxxxx[s]
```

```
$ python pySolitaireResultSimulation.py ./game_results/G00001.txt -v true
 0: ['']
 1: ['4D', '']
 2: ['4C', '', '3C']
 3: ['6H', '', '7D', '9S']
 4: ['JD', '', '2C', '7S', 'AH']
 5: ['AS', '', 'TS', '2H', '6S', 'AD']
 6: ['5C', '', 'JC', 'KS', '2D', '8H', '4H']
 7: ['KD', '', '6C', 'JH', '5D', '3S', '4S', '3H']
 m :['9D', 'TC', '2S', 'QC', 'KH', '5S', '9C', 'AC', 'QH', 'QD', '8S', '6D', '7C', '9H', 'JS', 'QS', '8C', '5H', 'TD', '3D', 'KC', '7H', '8D', 'TH']
 w :[]
----------------------------------------------------------------------------------
 s :[]
 h :[]
 d :[]
 c :[]
----------------------------------------------------------------------------------
turn = 0, next = "5S"
Hit Enter key.
    ...
    ...
turn = 121, next = ""
Hit Enter key.
 0: ['']
 1: ['']
 2: ['']
 3: ['']
 4: ['']
 5: ['']
 6: ['']
 7: ['']
 m :[]
 w :[]
----------------------------------------------------------------------------------
 s :['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']
 h :['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH']
 d :['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
 c :['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC']
----------------------------------------------------------------------------------
Execute time ... : x.xxxxxx[s]
```

## Licence

[MIT](https://github.com/NobuyukiInoue/pySolitaireResultSimulation/blob/main/LICENSE)


## Author

[Nobuyuki Inoue](https://github.com/NobuyukiInoue/)

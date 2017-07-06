# target-solver

A command line tool to solve the newspaper puzzle "Target Puzzle", written in Python3.

## Getting Started

This project consists of the following two files.
* `TargetSolver.py` - The command line interface Python script.
* `wordsEn.txt` - A list of valid English words.

These files must be present in the same directory to run.

### Prerequisites

To run target-solver, the host machine must have the following installed:
* `Python3` - The programming language in which target-solver was written. Available [here](https://www.python.org/).

### Running

The tool may be started by running the script `TargetSolver.py` as follows:
`python3 TargetSolver.py` 

The response will be a prompt for the nine letters of an instance of the Target Puzzle.

### Use

The Target Puzzle game provides the player with a collection of nine letters arranged in a grid like the following.

<table align="center">
    <tr>
        <td align="center">S</td>
        <td align="center">I</td>
        <td align="center">S</td>
    </tr>
    <tr>
        <td align="center">A</td>
        <td align="center"><b>N</b></td>
        <td align="center">A</td>
    </tr>
    <tr>
        <td align="center">E</td>
        <td align="center">C</td>
        <td align="center">M</td>
    </tr>
</table>

The objective is to form as many words as possible that use each given letter at most once. Every accepted word must follow one additional condition: they must use the centre letter.

After starting target-solver, the Target Puzzle letters must be entered in a special order. The letters must be given as a string of nine, with the centre letter appearing first.

For the above puzzle, target-solver would expect the following input.  
`NSISAAECM`  
Where the order of the last eight letters is unimportant.

After receiving a valid collection of letters, target-solver identifies the fitting words and prints them in two categories. These categories are the "Definite" and "Possible". The "Possible" words are those ending in "s". Some variants of the game do not allow plurals.

## Authors

* **Marc Katzef** - [mkatzef](https://github.com/mkatzef)

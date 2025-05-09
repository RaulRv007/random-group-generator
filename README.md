# Random Group Generator

This Python script generates random groups from a list of people (or elements), based on a specified group size. It divides a given list into groups while ensuring that the size of each group is as uniform as possible. If there are leftover elements, they are distributed across the groups. The program also handles cases where the total number of people is not divisible evenly by the group size.

## Table of Contents
- [How It Works](#how-it-works)
- [Performance Analysis (Big O)](#performance-analysis-big-o)
- [Code Walkthrough](#code-walkthrough)
- [Usage](#usage)

## How It Works

### Input
The script takes in two inputs:
1. **mGroup**: The number of people per group.
2. **A list of names (or elements)**, which will be divided into groups.

### Grouping Logic
1. The script calculates the total number of groups required using the ceiling function, ensuring that all people are included even if the number is not divisible by the specified group size.
2. The list is divided into two parts:
    - **Groupable**: The portion that can be evenly divided into groups.
    - **Leftover**: The remainder, which will be distributed across the groups.
3. The groups are formed in two stages:
    - First, groups are created from the groupable part.
    - Then, leftover elements are distributed evenly across the groups, ensuring that no group exceeds the size specified.
4. **Shuffling (optional)**: The script includes a shuffle method that can be used to randomize the list of people before grouping them, though it is currently commented out in the code.

### Output
The script prints the number of groups and the elements of each group.

## Performance Analysis (Big O)

### Time Complexity
- **O(n)**, where `n` is the number of elements in the input list. This is because the list is iterated over multiple times (for splitting, forming groups, and distributing leftovers).
- The `random.shuffle` method (if used) also has a time complexity of **O(n)**.

### Space Complexity
- **O(n)**, where `n` is the number of elements in the input list. The script creates additional lists to store the groups, which requires space proportional to the size of the input list.

## Code Walkthrough

### Class Definition
- The `Group` class is initialized with the list of people (`myList`) and the desired group size (`m`).
- The number of groups is calculated using `math.ceil(len(myList) / m)`.

### `generateGroups()` Method
- This method divides the list into two sections:
  - **Groupable**: People who can form full groups.
  - **Leftover**: The remainder.
- Groups are formed by iterating over the groupable list and filling each group until it reaches the desired size (`m`).
- Leftover people are then distributed across the groups in a way that keeps the groups as balanced as possible.

### `shuffle()` Method (optional)
- The `shuffle` method uses `random.shuffle` to randomize the order of people in the list before grouping. It is not used in the current version of the code.

### Input Example
An example input list `myInput` is provided, containing 30 elements. The script will divide this list into groups based on the user input for `mGroup`.

## Usage

1. Clone this repository or copy the code to your local machine.
2. Run the script in a Python environment.
3. Input the desired number of people per group when prompted.
4. View the results as the groups are printed on the screen.


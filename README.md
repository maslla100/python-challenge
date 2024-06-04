# Python Challenge

## Overview
This repository contains two Python projects, PyBank and PyPoll, developed as part of a data analytics course. These projects showcase the application of Python scripting to analyze financial and election data, providing insights through data manipulation and analysis.

## Table of Contents
- [Overview](#overview)
- [PyBank](#pybank)
  - [Objective](#objective)
  - [Technologies](#technologies)
  - [Usage](#usage)
  - [Results](#results)
- [PyPoll](#pypoll)
  - [Objective](#objective)
  - [Technologies](#technologies)
  - [Usage](#usage)
  - [Results](#results)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## PyBank

### Objective
The PyBank project involves analyzing financial records to calculate key metrics such as the total number of months, net total amount of profit/losses, average change in profit/losses, greatest increase in profits, and greatest decrease in profits over a given period.

### Technologies
- Python
- CSV module
- File I/O

### Usage
1. Place the `budget_data.csv` file in the `Resources` folder inside the `PyBank` directory.
2. Run the `main.py` script to perform the analysis.
3. The results will be printed to the terminal and saved in the `analysis` folder as `financial_analysis.txt`.

### Image Results
![PyBank Results](/PyBank/PyBank.png)

## PyPoll

### Objective
The PyPoll project involves analyzing election data to determine the total number of votes, a complete list of candidates who received votes, the percentage and total number of votes each candidate won, and the winner of the election based on popular vote.

### Technologies
- Python
- CSV module
- File I/O

### Usage
1. Place the `election_data.csv` file in the `Resources` folder inside the `PyPoll` directory.
2. Run the `main.py` script to perform the analysis.
3. The results will be printed to the terminal and saved in the `analysis` folder as `election_results.txt`.

### Image Results
![PyPoll Results](/PyPoll/pypoll.png)

## Repository Structure
python-challenge/
│
├── PyBank/
│ ├── Resources/
│ │ └── budget_data.csv
│ ├── analysis/
│ │ └── financial_analysis.txt
│ └── main.py
│
├── PyPoll/
│ ├── Resources/
│ │ └── election_data.csv
│ ├── analysis/
│ │ └── election_results.txt
│ └── main.py
│
└── README.md


## Installation
1. Clone the repository:
    ```
    git clone https://github.com/maslla100/python-challenge.git
    ```
2. Navigate to the project directory:
    ```
    cd python-challenge
    ```
3. Follow the usage instructions for each project to run the scripts and view the results.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.



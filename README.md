# Python Challenge

Python scripts used to help analyze budget/financial data (PyBank) and to help a small, rural town modernize its vote-counting process (PyPoll).

## Background

For this project, I created two Python scripts.

* [PyBank](#pybank)
* [PyPoll](#pypoll)


### <a name="pybank"></a>PyBank

Inside the **PyBank** folder, you will find a script that is used to help analyze budget/financial data for a company. The data is in a csv file and includes two columns, **Date** and **Profit/Losses**. 

The csv file being analyzed is located [here](./PyBank/Resources/budget_data.csv).
The script file is located [here](./PyBank/main.py).

When you run the script, the script analyzes the profit/losses numbers and calculates the following:

* The total number of months included in the dataset.
* The net total amount of "Profit/Losses" over the entire period.
* The average of the changes in "Profit/Losses" over the entire period.
* The greatest increase in profits (date and amount) over the entire period.
* The greatest decrease in losses (date and amount) over the entire period.

When the script is finished, the financial analysis will be printed to the terminal as well as exported to a [text file](./PyBank/financial_results.txt) in the same directory as the script.

### <a name="pypoll"></a>PyPoll

Inside the **PyPoll** folder, you will find a script that is used to help a small, rural town modernize its vote-counting process. The data is in a csv file and includes three columns, **Voter ID**, **County**, and **Candidate**. 

The csv file being analyzed is located [here](./PyPoll/Resources/election_data.csv).
The script file is located [here](./PyPoll/main.py).

When you run the script, the script analyzes the votes and calculates the following:

* The total number of votes cast.
* A complete list of candidates who received votes.
* The percentage of votes each candidate won.
* The total number of votes each candidate won.
* The winner of the election based on popular vote.

When the script is finished, the election results will be printed to the terminal as well as exported to a [text file](./PyPoll/election_results.txt) in the same directory as the script.

## Running the scripts

To run either one of the scripts:

1. Download or clone this repository to a local directory on your computer.

2. From a command line terminal (for example, Git Bash on Windows), change directory into the root directory (**python-challenge**) and then change directory into the **PyBank** or **PyPoll** directory, depending on which script you want to run.

3. Run the script by running the following command:

  ```bash
  python main.py
  ```

When finished, the script prints the results to the terminal and exports the results to a text file in the same directory as the script.

## Sample output

After running a script, the results are printed to the terminal, similar to the following examples:

* PyBank

```bash
$ python main.py
        Date  Profit/Losses
0   Jan-2010         867884
1   Feb-2010         984655
2   Mar-2010         322013
3   Apr-2010         -69417
4   May-2010         310503
..       ...            ...
81  Oct-2016         102685
82  Nov-2016         795914
83  Dec-2016          60988
84  Jan-2017         138230
85  Feb-2017         671099

[86 rows x 2 columns]
Total number of months: 86
Net total amount of profit/losses: $38382578
Average of changes: $-2315.12
Greatest increase amount: $1926159.0
Greatest increase date: Feb-2012
Greatest decrease amount: $-2196167.0
Greatest decrease date: Sep-2013
-----------------------------------
Financial Analysis
-----------------------------------
Total Months: 86
Total: $38,382,578.00
Average Change: $-2,315.12
Greatest Increase in Profits: Feb-2012, $1,926,159.00
Greatest Decrease in Profits: Sep-2013, $-2,196,167.00
```

* PyPoll

```bash
$ python main.py
         Voter ID County Candidate
0        12864552  Marsh      Khan
1        17444633  Marsh    Correy
2        19330107  Marsh      Khan
3        19865775  Queen      Khan
4        11927875  Marsh      Khan
...           ...    ...       ...
3520996  18050509  Marsh      Khan
3520997  13060332  Marsh      Khan
3520998  16754708  Queen      Khan
3520999  12083146  Queen      Khan
3521000  14526187  Queen  O'Tooley

[3521001 rows x 3 columns]
Total number of votes cast: 3521001
List of candidates who have received votes:
['Khan' 'Correy' 'Li' "O'Tooley"]
Number of votes each candidate won:
[2218231, 704200, 492940, 105630]
Percentage of votes each candidate won:
[63.0, 20.0, 14.0, 3.0]
Winner: Khan
---------------------------------------------------------------
Election Results
---------------------------------------------------------------
Total votes: 3,521,001
---------------------------------------------------------------
Candidates  Number of Votes Percentage of Votes (%)
      Khan        2,218,231                   63.0%
    Correy          704,200                   20.0%
        Li          492,940                   14.0%
  O'Tooley          105,630                    3.0%
---------------------------------------------------------------
Winner: Khan
---------------------------------------------------------------
```


## Jupyter Notebook

This repository includes Jupyter Notebook files for both **PyBank** and **PyPoll**, which is where the scripts can be viewed/executed as well.

* [PyBank](./PyBank/PyBank.ipynb)
* [PyPoll](./PyPoll/PyPoll.ipynb)

## Technologies used

The following technologies were used to build the scripts:

* Python
* Pandas
* Jupyter Notebook
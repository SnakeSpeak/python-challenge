# python-challenge
PyBank: breaks down budget_date.csv into lists containing dates, dollar amounts, and the differences between those amounts per month by looping through every row. Then uses their lists' indexes as references when calculating greatest profits/losses and their corresponding months.

Prints results to the terminal and to a text file in PyBank\analysis titled, "final_analysis.txt"

PyPoll: access election_data.csv, and stores names in candidates list, which then counts how many times the names pop up in the list and puts that in a dictionary called "cand_votes" ({'cand1': ##, 'cand2': ##,...}). Also creates a dictionary called "cand_pct" which calculcates the percentage of votes per candidate.


Prints results to the terminal and to a text file in PyPoll/analysis titled, "poll_results.txt"

Very dynamic, as any election data csv that follows the same column conventions can be brought in and "poll_result.txt" will change printed results.
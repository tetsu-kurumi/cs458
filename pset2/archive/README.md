CS 458/558 - Problem Set 2
Assigned:	Wednesday January 31st
Deadline:	Monday March 4, 11:59pm
The world's biggest casino: the stock market
In homework 1, you wrote a procedure hitme() which decided whether to have the dealer give you a card for your blackjack hand.
In this assignment, you will write a procedure invest(ticker, client=False), which will take a stock ticker symbol as its argument and return one of three values: buy, sell, or hold. It will also provide an explanation for its recommendation. The optional client parameter can be one of: income, growth, or esg, in which case the procedure will evaluate the stock for inclusion in an income portfolio, growth portfolio, or environment, social, and governance portfolio.

You will use the Yahoo finance api: yahooquery, which is installed as a Python module on the zoo. See yquery.html for more information and a demonstration.

Your program will be similar to your blackjack program. When it gets a ticker, it will use yahooquery to get information about the stock and then use that information to index a table of results. Here are some sample indices:

beta beta: a measure of the stocks volatility relative to the market as a whole.
market cap whether the stock is a large cap (> $10 billion), mid cap (< $10 billion and > $2 billion) or small cap (> $250 million and < $2 billion)
growth vs value growth e.g., no or low dividend and volatile vs value e.g., dividend and stable.
ESG Companies are graded on ESG: environment, social, and corporate governance. That is, companies that fight climate change and promote diversity get high ESG scores. The question is: are they more profitable than the nasty old companies.
Earnings surprise Did their recent earnings report exceed expectations or disappoint?
sector In what sector does the company operate? e.g., energy, technology, materials.
yahooquery provides you these data (and a boatload more) for most US companies. For this assignment, that is your world. All companies should be US and report in US dollars.
You should gather data on dozens of companies and determine which of these indices can predict performance. To do so, you need to look at a stock's performance for the past 10 years or so. A stock is good if it outperformed the S and P 500 index during that period, and bad if it did worse than the S and P. The ticker for the S and P is "^GSPC".

Your analysis does not need to be one size fits all. You may evaluate companies differently depending on their size, sector, or ESG scores. For example, you could have one metric for technology companies and another for banks.

Explanation
Your procedure needs to provide an explanation that justifies your recommendation. Your process may be either quantitative or qualitative. You might use a machine learning classification based on the Merrill Lynch model portfolios or you might come up with your own set of rules. The explanation should be qualitative. I don't want to see R2's or p-values.
We will not evaluate the accuracy of your recommendation. We are more interested in the coherency of your explanation. Does it make sense? Is it a good story? Even the best Wall Street analyst is not going to be right all the time.

SUBMIT
This assignment will be submitted through Gradescope on the Course Assignments page. You should submit two files: hw2.py and a README file which explains how your program works, as well as a transcript of the program in action. Alternatively, you can submit a jupyter notebook file, hw2.ipynb which contains both code and discussion. The jupyter notebook can also include zippy graphs. The clients love graphs. If you submit a jupyter notebook, also submit the downloaded html and py files - that is, a total of three files.
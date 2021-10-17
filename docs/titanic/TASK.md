
## From Future Learn: 2.20, Putting it all together & 2.21, Sharing Your Report
[edited]

The sinking of the Titanic was a tragedy. Around two-thirds of the people aboard died. Apart from the fact that it was travelling fast in a
known icebergs area, the extent of the loss of life was also due to lifeboats deployment & evacuation policy.

We have seen that the important steps in data analysis are:

* Understanding a problem and developing focused, answerable questions
* Exploring the data we have and visualising it to understand underlying patterns
* Reporting your findings, once the stages in the analysis and modelling are complete
* Addressing limitations of our analysis or assumptions we have made

In this short assignment, you will apply these steps.

<br>

### Your task

Write a short report on the passenger survival rates. Your analysis should include:

1. Your research questions - what are you able to answer from the data you have, and the analysis you have done? For
   example, your question might be: ‘What was the difference in survival between passengers of different ticket classes?’
2. The results of the analysis as (at least one) table and graph. These should be easy to understand and include the
   correct labels and legend (colour key) if appropriate.
3. A short discussion of the results, their implications, and what they say about the evacuation policy on the
   Titanic. You should also discuss the limitations of the dataset and any assumptions you have made.

Write your report as a word document or PDF with the tables and graphs embedded in the document. You should aim for
around 300 words. We’ll give instructions for how to share your report on the next step.

<br>

### Help for getting started

Take a look at the dataset [titanic.csv](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv). It contains data on 891 actual
passengers from the Titanic.  The columns describe whether they survived (1=yes, 0=no), their sex (female, male), and the passenger
class (1=first class, 2=second class, 3=third class). Other information such as age and fare paid is also included.

We can import this dataset into Python by adapting the Python code used
in [Step 2.2 of the course](https://www.futurelearn.com/courses/data-science-artificial-intelligence/4/steps/1185340).

```python
import pandas as pd

# noinspection PyTypeChecker
url: str = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic = pd.read_csv(filepath_or_buffer=url)
print(titanic)
```

Check for yourself that the first few lines are the same as the CSV file.  A quick summary of the quantitative variables
in the dataset is given by the following Python code.

```python
# noinspection PyUnresolvedReferences
titanic.describe()
```

Suppose we wish to investigate the relationship between survived, sex, and passenger class (`pclass`). The following Python
code produces a table counting those who did and did not survive by sex and passenger class.

```python
# noinspection PyUnresolvedReferences
table = titanic.groupby(['sex', 'pclass', 'survived'])['survived'].aggregate('count').unstack()
print(table)
```

The table can be directly turned into a bar graph in order to visualise the results.

```python
# noinspection PyUnresolvedReferences
table.plot(kind='bar',stacked=True)
```

Of course, we should add a title, axis labels, and perhaps change the colours of the bars.

<br>

### Further reading

* Kaggle. (n.d.) [Titanic: Machine learning from disaster](https://www.kaggle.com/c/titanic/data)
* Mwaskom. (2014). Seaborn-data / titanic.csv [Dataset](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv)
* Schiller, L. (2016). [Investigating the Titanic dataset with Python](http://luizschiller.com/titanic/)
* Yavus, S. (2019, April 10). Getting started with data analysis with Python Pandas: Hands-on exercises (with Titanic dataset). [Medium](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)

===============================================================================
CompEcon: Some Project Ideas 
===============================================================================

You are encouraged to come up with your own project ideas. 
Please pick a topic that has to do with economics. It is often best to focus on
a more local topic as opposed to a very broad question such as "poverty in the
world."  It is going to be much easier and ultimately more meaningful if you
focus on "poverty in Maryland" or even better "poverty in Baltimore." The more
local, usually, the better and the less abstract the whole research exercise
becomes. For some topics that's of course not possible.

I would also encourage you to pick economic topics that "matter." Now, what
matters often depends on who is asking of course but think about all the big
issues in economics such as inequality, poverty, unemployment, minimum wages,
guaranteed minimum income, inflation, economic growth, health insurance issues,
retirement issues, obesity epidemic, discrimination issues along various
socioeconomic dimensions (i.e., race, gender, sexual orientation, religion,
etc.), immigration issues, political economics (i.e., election issues), crime, 
environmental issues, educational issues to just name a few.
There are many interesting research questions that you could ask that I would
consider meaningful and important. 

These are the types of projects student typically do in this class.

1. Web scraping
-------------------------------------------------------------------------------
Use `Beautiful Soup <https://pypi.python.org/pypi/beautifulsoup4/>`_ to scrape
data from the web. Use the `Pandas <http://pandas.pydata.org/>`_ and 
`ggplot <http://ggplot.yhathq.com/>`_ libraries for data
cleaning and graphical summaries and employ basic Econometric methods  to
analyse your data. Some example topics are:

You can come up with similar projects based on online data. I prefer topics
that are very local. Start with Towson, Baltimore, maybe Maryland centered
topics if you can. Like `this example <http://www.cs.cornell.edu/~karthik/projects/rateprof-scrape/DOCUMENTATION.html>`_
where a student wrote scripts to scrape RateMyProfessor.com. And a follow up
`project <ExampleProjectPPT.pdf>`_ where the ratings were correlated with graduation rates.

2. Survey data analysis
-------------------------------------------------------------------------------

Use data from the Medical Expenditure Panel Survey
`MEPS <http://meps.ahrq.gov/mepsweb/>`__ and analyze health state transition
probabilities over the life-cycle of individuals. This is 
a data project that will require deepening your knowledge of the **Pandas**
library. You are required to download the
data, transform it into Python readable files, clean it, and produce graphs
and summary statistics. 
If you already took Econometrics you can try to implement ``mlogit`` or ``mprobit`` models.

  * Literature to get you started: 
    `Jung (2015) <https://juejung.github.io/papers/markovtransitions.pdf>`_
  * Data: `MEPS <http://meps.ahrq.gov/mepsweb/>`_

3. Machine learning project
-------------------------------------------------------------------------------

For a machine learning project you will need data. Either you use an existing
data source, i.e., a survey, data from a firm, a city, etc. or you have to
assemble or collect the data yourself. You could use web-scraping for this or
download data through an API from a website or content provider.

Once you have the data you can try to predict, classify, etc.

Here is a link to a pretty cool project I just found: 
`Employee Churn Model based on IBM firm level data <https://towardsdatascience.com/building-an-employee-churn-model-in-python-to-develop-a-strategic-retention-plan-57d5bd882c2d>`_
As you can see it's really just a logistic regression that predicts whether an
employee is going to resign or not and which variables are the main drivers for
that decision. It is of course presented as machine learning topic as opposed
to the traditional econometric framework that you are familiar with from Econ
306. This just means that the "regressions" are not just logistic regressions,
but include other forecasting models such as tree decision models, etc.
The models are then evaluated following the machine learning approach to
find the best model which makes the most accurate predictions. If you are
interested in digging deeper into this please have a look at Geron (2019)
"Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow" which is
a very comprehensive introduction to machine learning in Python.

4. Tax simulation policy
-------------------------------------------------------------------------------

Simulate optimal tax policy in an overlapping generations economy. This
is probably a Python project as it deals with optimization methods. 

  * Literature to get you started: 
    `Glomm and Jung (2013) <https://juejung.github.io/papers/timing05142012.pdf>`_
  * Codes:

5. GUI programming
-------------------------------------------------------------------------------

GUI programming in Python using
`tkinter <https://docs.python.org/3.4/library/tkinter.html>`_

  * Literature to get you started:

6. Object oriented programming
-------------------------------------------------------------------------------

Agent-based modeling using `simPy <http://simpy.readthedocs.org/en/latest/>`_ in
Python. This requires object-oriented-programming 

  * Literature to get you started: 
     1. Dhananjay K. Gode and Shyam Sunder (1993), "Allocative
        Efficiency of Markets with Zero-Intelligence Traders: Market as a
        Partial Substitute for Individual Rationality," Journal of Political
        Economy Vol. 101, No. 1, pp. 119-137 
     2. `John Stachurski's website <http://quant-econ.net/py/python_oop.html>`_

7. Network graphs
-------------------------------------------------------------------------------

Use `iGraph <http://igraph.sourceforge.net/index.html>`_ 
to analyze network data. Some network data can be found under this
`link <http://www-personal.umich.edu/~mejn/netdata/>`_.

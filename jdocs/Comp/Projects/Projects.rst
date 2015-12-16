===============================================================================
Suggested Projects 
===============================================================================

You are encouraged to come up with your own project ideas. If you have
trouble with that, you can use some of these suggestions to get you
started on a project.

1. Web scraping
-------------------------------------------------------------------------------
Use `Beautiful Soup <https://pypi.python.org/pypi/beautifulsoup4/>`_ to scrape
data from the web. Use the `Pandas <http://pandas.pydata.org/>`_ and 
`ggplot <http://ggplot.yhathq.com/>`_ libraries for data
cleaning and graphical summaries and employ basic Econometric methods  to
analyse your data. Some example topics are:

  * Use `Yelp <http://www.yelp.com/baltimore>`_ reviews to find the best car
    wash in Baltimore. You need to write a script that automatically downloads
    the data from various website based on yelp links. You need to parse
    through the html files to find star ratings, prices, discounts, etc. You
    can plot time trends by repeatedly scraping data on different days.

You can come up with similar projects based on online data. I prefer topics
that are very local. Start with Towson, Baltimore, maybe Maryland centered
topics if you can. Like `this example <http://www.cs.cornell.edu/~karthik/projects/rateprof-scrape/DOCUMENTATION.html>`_
where a student wrote scripts to scrape RateMyProfessor.com. 

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

3. Tax simulation policy
-------------------------------------------------------------------------------

Simulate optimal tax policy in an overlapping generations economy. This
is probably a Python project as it deals with optimization methods. 

  * Literature to get you started: 
    `Glomm and Jung (2013) <https://juejung.github.io/papers/timing05142012.pdf>`_
  * Codes:

4. GUI programming
-------------------------------------------------------------------------------

GUI programming in Python using
`tkinter <https://docs.python.org/3.4/library/tkinter.html>`_

  * Literature to get you started:

5. Object oriented programming
-------------------------------------------------------------------------------

Agent-based modeling using `simPy <http://simpy.readthedocs.org/en/latest/>`_ in
Python. This requires object-oriented-programming 

  * Literature to get you started: 
     1. Dhananjay K. Gode and Shyam Sunder (1993), "Allocative
        Efficiency of Markets with Zero-Intelligence Traders: Market as a
        Partial Substitute for Individual Rationality," Journal of Political
        Economy Vol. 101, No. 1, pp. 119-137 
     2. `John Stachurski's website <http://quant-econ.net/py/python_oop.html>`_

6. Network graphs
-------------------------------------------------------------------------------

Use `iGraph <http://igraph.sourceforge.net/index.html>`_ 
to analyze network data. Some network data can be found under this
`link <http://www-personal.umich.edu/~mejn/netdata/>`_.

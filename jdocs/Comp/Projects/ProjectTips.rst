===============================================================================
Tips for Successful Projects
===============================================================================

Undergraduate research projects typically fall within three categories:

  1. Data analysis of existing survey data
  2. Web scraping with subsequent data analysis
  3. Simulation models that require optimization

I will make some suggestions and provide links for each one of the project
types next.

When you work towards your first presentation, I strongly suggest you use and
economics research relevant search engine like:
`EconPapers <https://econpapers.repec.org/scripts/search.pf?ft=>`_
in order to find relevant literature.

1. Data Analysis Projects (and Machine Learning Projects)
-------------------------------------------------------------------------------

Since you are working with data that is already available in some form, your
focus will be on data cleaning and the subsequent econometric/statistical 
analysis.
I expect you to become very familiar with the `Pandas <http://pandas.pydata.org/>`_ 
library as it is the core library for doing data analysis in Python.
For graphs I suggest you also check out `ggplot <http://ggplot.yhathq.com/>`_ 
or the `Bokeh <http://bokeh.pydata.org/en/latest/>`_ library which is newer and
allows for somewhat interactive graphs that could be embedded into websites.
You may also want to check out the `pydata <http://pydata.org/>`_ website.

I expect you to make professional looking summary tables and graphs of your
data for starters. This should then be followed by regression analysis (OLS or
related models) similar to what you have been introduced in Econ 205 and Econ
306.

The structure of your paper (about 20 pages) will roughly follow this outline:

  1. Introduction (with literature review)
  2. Model (Econometric model, e.g., :math:`y = \beta_0 + \beta_1 X + \epsilon`)
  3. Data (Description of data survey and summary stats)
  4. Results (Regression analysis etc.)
  5. Conclusion

  * References
  * Appendix: Tables
  * Appendix: Figures

**Developed Expertise:** General data analysis, data wrangling, advanced
graphing libraries, econometric modeling


2. Web Scraping Projects
-------------------------------------------------------------------------------

If you work on a web scraping project you need to familiarize yourself with one
of the many scraping libraries out there. One of the more basic ones is
`Beautiful Soup <https://pypi.python.org/pypi/beautifulsoup4/>`_. We go over at
least one simple example in class where we scrape data from `YouTube
<https://www.youtube.com/>`_.

A more powerful web scraping framework is `scrapy <http://scrapy.org/>`_.
According to `Stack Overflow <http://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler>`_
the difference between the two is as follows::

    Scrapy is a Web-spider or web scraper framework. You give Scrapy a root URL
    to start crawling, then you can specify constraints on how many number of
    URLs you want to crawl and fetch,etc., It is a complete framework for
    Web-scrapping or crawling. [...]

    BeautifulSoup is a parsing library which also does pretty job of fetching
    contents from URL and allows you to parse certain parts of them without any
    hassle. It only fetches the contents of the URL that you give and stops. It
    does not crawl unless you manually put it inside a infinite loop with
    certain criteria.

    In simple words, with Beautiful Soup you can build something similar to
    Scrapy.  Beautiful Soup is a library while Scrapy is a complete framework.

In order to scrape data successfully you also need to learn/understand the
basics of the hypertext markup language or **html**. There are many short
introductions available on the net, so you need to work through some of
those `intros to html <http://www.google.com/search?q=intro+to+html>`_ in order
to get up to speed.  

Your expertise will therefore be developed in text processing using
lists, string manipulation, and scraping frameworks. If you feel very brave you
may also want to check out the basics of `regular expressions
<https://docs.python.org/3/howto/regex.html>`_ which is a pattern matching
concept that will allow you to pretty much grab anything from a website.

Since you will spend a considerable amount of time trying to acquire the data,
I will be less demanding when it comes to the data analysis part of your
project.  Still, the library that you probably want to use for the data
analysis part is again `Pandas <http://pandas.pydata.org/>`_ for organizing and
cleaning the data and possibly `matplotlib <http://matplotlib.org/>`_ for
making graphs. 

The structure of your paper (about 20 pages) will roughly follow this outline:

  1. Introduction (with literature review)
  2. Data (Description of source and how acquired)
  3. Results (Summary statistics, graphs, etc.)
  4. (Optional: Regression analysis)
  5. Conclusion

  * References
  * Appendix: Tables
  * Appendix: Figures

**Developed Expertise:** Web scraping basics, basics in data wrangling, text
parsing and string methods, basics in html and regular expressions (pattern
matching)

3. Simulation Projects
-------------------------------------------------------------------------------

If you are working on a simulation project then you have to familiarize
yourself with `numpy <http://www.numpy.org/>`_ for basic numerical coding objects
like arrays, `scipy <http://docs.scipy.org/doc/>`_ for optimization libraries
and `matplotlib <http://matplotlib.org/>`_ for graphing your optimization or
simulation results.

You can read ahead in the lecture notes to see how a simple 2-period
optimization problem is set up in Python. You will also want to read up on how
to define `functions in Python <http://www.google.com/search?q=functions+in+python>`_.

For a more general simulation approach you may also want to dig into
`object-oriented-programming (OOP) <http://www.google.com/search?q=python+object+oriented+programming>`_
a slightly different programming paradigm that allows you to keep data objects
and functional methods that can be applied on them neatly together. Check out
the lecture on OOP as well to get a rough idea.

The structure of your paper (about 20 pages) will roughly follow this outline:

  1. Introduction (with literature review)
  2. Model
  3. Equilibrium
  3. Results (Simulation of policy experiments, etc.)
  4. Conclusion

  * References
  * Appendix: Tables
  * Appendix: Figures

**Developed Expertise:** Optimization methods, functional programming, 
object oriented programming, economic modeling


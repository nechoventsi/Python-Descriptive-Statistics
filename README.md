# Descriptive Statistics and the Least Squares Method using Python

*Ventsislav Dimitrov*  
*University of Sofia "St. Klimen Ohridski"*  
*Faculty of Physics, Department of Astronomy*  

In the theory of probability and statistics the concepts of mean and mathematical expectation are often used as synonyms, for the assessment of central tendency in a probability distribution, or in the values of a random variable which is characterized in that distribution. On the other hand, in order to evaluate the noise in the data or deviations of that data from the central average value, we can use statistical estimates by variation, dispersion or standard deviation. When looking for a correlation between variables in an astronomical excerpt or database, we usually resort to the use of the correlation coefficient *r* or to the application of a linear / non-linear regression.

Such statistical evaluations are applied in virtually all areas of science, where astronomy is no exception. The methods described in this project could be used to define the statistical properties of astronomical catalogs or experimentally derived data from an observational program. Of course, most of these formulas are usually implemented in the software that we use to analyze the data, but the aim of the current project is to show the possible implementations of these methods in Python using *lists*, *conditional blocks*, *iteration*, *reading and writing* a file, etc.

## Prerequisites

To be able to go through the examples in this project, you'll have to obtain these if you haven't got them:  
* *Python 2.7*
* the modules *NumPy*, *SciPy*, *Matplotlib*
* *iPython*

You can install the extra modules using your favourite method, but I recommend installing [Anaconda by Continuum Analytics](https://www.continuum.io/downloads) - it includes all these in a neat package, plus some more useful scientific tools.

When the project is finished, you will be able to view/run it in a couple of different ways: by cloning the repository and running the main scripts, or by running iPython Notebook from the project folder

    $ cd Python-Descriptive-Statistics
    $ ipython notebook

and then checking out the file `Descriptive Statistics.ipynb`.

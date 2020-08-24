# About
This repository contains several [Jupyter](https://jupyter.org/) notebooks. These notebooks
provide an introduction to programming in Python.

The focus of the material is students with 
little or no previous programming experience, especially in non-technical courses of study. 
To support these students in learning the complex skill of programming, the
[Four Components Instructional Design (4C/ID)](http://www.tensteps.info/) method was used to create the material.

The notebooks are organized as in a directory structure in ascending complexity. Each directory contains a 
notebook explaining the topic as well as *howto-notebook* that summarises the most important aspects. 
Furthermore, there is an exercise folder that contains exercises according to the 4C/ID model. In the 
exercises folder, there is always an index file linking to all the available exercises. As an example consider the
topic [conditionals](/notebooks/30_conditionals). The folder contains the following files:

- [conditionals.ipynb](/notebooks/30_conditionals/conditionals.ipynb): The introduction to the topic (i.e. the lecture)
- [conditionals_howto.ipynb](/notebooks/30_conditionals/conditionals_howto_eng.ipynb): the howto 
- [exercises](/notebooks/30_conditionals/exercises): a folder containing all the exercises for the topic
    - [00_conditional_exercises.ipynd](/notebooks/30_conditionals/exercises/00_conditional_exercises.ipynd): the index file for the exercises. 

All the exercises contain unit tests. These tests can be used by the students to check their solutions. The unit tests have been created using 
[nose](https://nose.readthedocs.io/en/latest/). Furthermore, all the exercises contain the annotations required by 
[nbgrader](https://nbgrader.readthedocs.io/en/stable/).

# Contributing

## Extensions
Jupyter Notebook Extensions are simple add-ons which can significantly improve your productivity in the notebook environment.
They automate tedious tasks such as formatting code or add features like creating a table of contents.
While there are numerous existing extensions, we can also write our own extension to do extend the functionality of Jupyter.

### Steps to modify/activate extensions

1. run the following code in a command prompt to activate nbExtensions:
`pip install jupyter_contrib_nbextensions && jupyter contrib nbextensions install`
1. copy the extions folder, ex. ``extensions\default_cell`` in the nbextensions directory for your environment.
your ``jupyter_contrib_extensions`` directory could be:
``/usr/local/lib/python3.8/site-packages/jupyter_contrib_nbextensions/nbextensions``
1. When you make a change to the extension files while developing and you want to see the effects in 
a Jupyter Notebook,you need to run the command ``jupyter contrib nbextensions install`` to rewrite the Jupyter config files.
Then, restart the notebook server to see your changes.
1. In your jupyter server page you can activate/deactivate each extension under the tab ``Nbextensions``

### Structure of a Jupyter Notebook Extension
There are 3 parts (at minimum) to any Jupyter Notebook extension:
1. ``description.yaml`` : A configuration file read by Jupyter
1. ``main.js`` : The Javascript code for the extension itself
1. ``README.md`` : A markdown description of extension

# Todos
- After the first semester teaching whith these notebooks it became clear that some of the exercises require some rework. Currently, the explanation of the task is not always clear enough.
- Translate the notebooks and exercises.
# Acknowledgements 
The work on this material has been supported by 

- The SQSL-Project of the FH Aachen: https://www.fh-aachen.de/en/hochschule/projekt-sqsl/
- The [Stifterverband](https://www.stifterverband.org/) in the context of a *Senior-Fellowship für Innovationen in der digitalen Hochschullehre*: https://www.stifterverband.org/digital-lehrfellows-nrw/2019/drumm

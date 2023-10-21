Technical Setup Guide
----------------------

The infrastructure chapter details what parts there are, this chapter explains how to use them correctly by explaining how to set everything up and how to maintain it. If the setup contains a lot of files and folders, give an overview of their structure and purpose. If not separately given, this is the place to document functions, APIs, and other code objects. When describing these objects include their purpose as well as the expected in- and outputs. Also, you might want to include a part with the most frequent errors and how to handle them.

You can also include code blocks:

    >>> from {{ package_name }}.function.example_function import print_something
    >>> print_something(a="Hello", b="World!")

or:

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       a = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

or:

.. code-block:: python
   :linenos:

   def some_other_function():
       # this is a comment
       print 'Switch on line numbers for the individual block'
       a = False
       b = True
       return a

or:

.. code-block:: bash

    $  git clone https://github.com/example_user/example_repo.git
    $  cd example_repo

For the PDF export: If you have a very long table, you can use the class *longtable* to break the table over multiple pages.

.. list-table:: Table Title
   :class: longtable
   :header-rows: 1

   * - **Column 1**
     - **Column 2**
   * - value 1
     - value 1
   * - value 2
     - value 2
   * - value 3
     - value 3
   * - value 4
     - value 4
   * - value 5
     - value 5
   * - value 6
     - value 6
   * - value 7
     - value 7
   * - value 8
     - value 8
   * - value 9
     - value 9
   * - value 10
     - value 10
   * - value 11
     - value 11

You can also specify the column widths:

.. list-table::
   :widths: 5 10
   :header-rows: 1

   * - **Column 1**
     - **Column 2**
   * - value 1
     - value 1
   * - value 2
     - value 2
   * - value 3
     - value 3

It’s often easier to reference a CSV file than to create a table using RST syntax.

.. .. csv-table:: Table Title
   :file: csv_file_path.csv
   :widths: 30, 70
   :header-rows: 1

.. note::
   This is a note.

.. warning::
    This is a warning.

Include plots by specifying the path to a source file as argument to the directive:

.. plot:: source/plots/plot.py
   :width: 400
   :format: doctest
   :include-source: False

   This is the plot caption

or by using doctest syntax:

.. plot::
   :width: 400
   :format: doctest
   :include-source: False

    >>> import seaborn as sns
    >>> import matplotlib as mpl
    >>> colors_good_to_bad = ["#0000FF", "#000000", "#283440", "#6C7D8C", "#FE0D6C"]
    >>> statworx_palette = sns.color_palette(colors_good_to_bad, as_cmap=True)
    >>> df = sns.load_dataset("diamonds")
    >>> f, ax = plt.subplots(figsize=(7, 5))
    >>> sns.histplot(
    >>>     df,
    >>>     x="price", hue="cut",
    >>>     multiple="stack",
    >>>     palette=statworx_palette[:5],
    >>>     edgecolor=".3",
    >>>     linewidth=.5,
    >>>     log_scale=True,
    >>> )
    >>> ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    >>> plt.show()

You can also include the source code of your plots:

.. plot::
   :width: 400
   :format: doctest
   :include-source: True

    >>> import seaborn as sns
    >>> import matplotlib as mpl
    >>> colors_blue = ["#0000FF", "#3343FF", "#6573FF", "#98A3FF", "#CCD1FF", "#F2F3FF"]
    >>> statworx_palette = sns.color_palette(colors_blue, as_cmap=True)
    >>> df = sns.load_dataset("diamonds")
    >>> f, ax = plt.subplots(figsize=(7, 5))
    >>> sns.histplot(
    >>>     df,
    >>>     x="price", hue="cut",
    >>>     multiple="stack",
    >>>     palette=statworx_palette[:5],
    >>>     edgecolor=".3",
    >>>     linewidth=.5,
    >>>     log_scale=True,
    >>> )
    >>> ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    >>> plt.show()

.. raw:: latex

    \newpage

Use `sphinx-apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_ to automatically generate your code documentation. It will generate separate rst-files including an *automodule* directive for each py-file.

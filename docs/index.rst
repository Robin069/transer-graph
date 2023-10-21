
.. only:: builder_html

Creating a Project Documentation with Sphinx
==============================================

Move to the docs folder and install needed packages:

.. code-block::

    $  cd docs
    $  pip install -r requirements.txt

Creates separate rst-files for each py-file in the src folder for your code documentation:

.. code-block::

    $  sphinx-apidoc -o source ../src

Create HTML/PDF output:

.. code-block::

    $  sphinx-build -M html ./ build
    $  sphinx-build -M latexpdf ./ build


A more detailed description can be found on `Confluence <https://statworx.atlassian.net/wiki/spaces/INTERN/pages/1908670465/Documentation+with+Sphinx>`_.

Content
========

.. toctree::
   :maxdepth: 2
   :caption: Content

   source/0_abstract
   source/1_use_case
   source/2_data
   source/3_methodology
   source/4_infrastructure
   source/5_user_guide
   source/6_technical_setup_guide
   source/7_appendix

.. only:: builder_html

   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

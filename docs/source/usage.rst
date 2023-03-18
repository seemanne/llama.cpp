Usage
=====

.. _installation:

Installation
------------

To use llamacpypy, first install it using pip:

.. code-block:: console

   (.venv) $ pip install llamacpypy

Architecture basics
----------------

Llamacpypy is built in an object oriented manner. The main feature is the Llama class. 
The idea is that the library should provide the opportunity to run inference in web apis etc. This means that the class can be initialized without loading the model into memory.

Llama class
----------------


.. autoclass:: llamacpypy.Llama



For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']


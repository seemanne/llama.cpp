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

.. py:class:: llamacpypy.Llama 

   The main model class

   :param model_name: Path to model binary
   :type model_name: str
   :param model_params_dict: Optional dict for model configuration, see llamacpypy.DEFAULT_PARAMS
   :type model_params_dict: dict
   :param warm_start: Whether to load to model into memory at initialization
   :type warm_start: bool

   .. py:method:: Llama.generate()

      Generate text using the current loaded model.

      :param promt: Promt to start from
      :type promt: str
      
      :return: The generated text
      :rtype: str

   .. py:method:: Llama.set_params()

      Set the model params using a parma dict, the input will be type-checked.

      :param model_params_dict: Param dict, check llamacpypy.DEFAULT_PARAMS
      :type model_params_dict: dict
   
   .. py:method:: Llama.load_model()

      Load the model into memory for inference.



.. autoclass:: llamacpypy.Llama

   :members:



For example:

>>>from llamacpypy import Llama
>>>llama = Llama('models/7B/ggml-model-q4_0.bin')
>>>print(llama.generate("This is the weather report, we are reporting a clown fiesta happening at backer street. The clowns "))
This is the weather report, we are reporting a clown fiesta happening at backer street. The clowns 1st of July parade was going to be in their own neighborhood but they just couldn't contain themselves;
They decided it would look better and probably have more fun if all went into one area which meant that the whole town had to shut down for a little while as all roads were blocked. At least traffic wasn’t too bad today because most of people are out shopping, but I did see some shoppers in their car driving away from Backer street with “clowns” on wheels outside their windows…
The kids lined up along the route and waited for the parade to pass by


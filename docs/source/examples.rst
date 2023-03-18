Examples
========

Running an API server using FastAPI
-----------------------------------

Install the required dependencies:

.. code-block:: console

    pip install fastapi
    pip install "uvicorn[standard]"
    pip install llamacpypy

Set up a file named main.py:

.. code-block:: python

    from fastapi import FastAPI
    from llamacpypy import Llama

    llama = Llama('path/to/model/binary')
    app = FastAPI()

    @app.get('/')
    async def read_root():
        return {'Hello' : 'World'}

    @app.put('/generate')
    async def generate(prompt: str):
        result = llama.generate(prompt)
        return {"model_output" : result}

Run the uvicorn test server and query to your hearts content

.. code-block:: console

    uvicorn main:app --reload
    curl -X 'PUT' 'http://127.0.0.1:8000/generate' -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"prompt": "your promt here"}
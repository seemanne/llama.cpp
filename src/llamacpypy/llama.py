from ._core import LlamaModel

DEFAULT_PARAMS = {

    "n_predict" : 128,
    "repeat_last_n" : 64,
    "n_ctx" : 512,

    "top_k" : 40,
    "top_p" : 1.0,
    "temp" : 0.7,
    "repeat_penalty" : 1.3,

    "n_batch" : 8
}


class Llama():

    def __init__(self, model_name: str, model_params_dict: dict=None, warm_start=True) -> None:
        """Creata a llama model instance from a given binary.
        Will load the model into memory if warm_start=True

        Args:
            model_name (str): Path to model binary (.bin)
            model_params_dict (dict, optional): Model params dict, see llama.DEFAULT_PARAMS for what parameters are supported. Defaults to None.
            warm_start (bool, optional): Wether to load the model into memory on init. Alternatively can be done using Llama.load_model(). Defaults to True.
        """
        
        self.is_loaded = False
        self.model_name = model_name
        self.model = LlamaModel(model_name)
        if model_params_dict:
            self.set_params(model_params_dict)
        else:
            self.set_params(DEFAULT_PARAMS)
        if warm_start:
            self.load_model()

    def generate(self, prompt: str) -> str:
        """Generate text from loaded model

        Args:
            prompt (str): Given starting promt

        Returns:
            str: generated text
        """
        if not self.is_loaded:
            raise ReferenceError(f"The Model has not been loaded yet, call Llama.load_model() or instatiate with warm_start=True")
        return self.model.generate(prompt)
    
    def set_params(self, model_param_dict: dict):
        """Set model params, will perform a type check before handing to cpp

        Args:
            model_param_dict (dict): see llama.DEFAULT_PARAMS for what parameters are supported
        """

        _typecheck_model_params(model_param_dict)
        self.model.set_params(**model_param_dict)
    
    def load_model(self):
        """Load the model into memory

        Raises:
            ReferenceError: Model already loaded
            ValueError: Model failed to load
        """

        if self.is_loaded:
            raise ReferenceError(f"The Model has already been loaded, please instantiate a new class")
        ret = self.model.load_model()
        if not ret:
            raise ValueError(f"Model {self.model_name} did not load properly. Is the filepath correct?")
        self.is_loaded = True
        
    


def _typecheck_model_params(model_params_dict):

    floats = ['top_p', 'temp', 'repeat_penalty']
    ints = ['n_threads', 'n_predict', 'repeat_last_n', 'n_ctx', 'top_k', 'n_batch']
    for key in model_params_dict:
        
        if key in floats:
            if not isinstance(model_params_dict[key], float):
                raise TypeError(f"Model parameter {key} must be a float, was given a {type(model_params_dict[key])}")
        if key in ints:
            if not isinstance(model_params_dict[key], int):
                raise TypeError(f"Model parameter {key} must be an int, was given a {type(model_params_dict[key])}")

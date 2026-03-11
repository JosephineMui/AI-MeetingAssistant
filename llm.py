'''
IBM WatsonX utilizes various language models, including Llama 3 by Meta, which is currently
the strongest open-source language model.


Here's how the code works:

Setting up credentials: The credentials needed to access IBM's services are pre-arranged by 
the Skills Network team, so you don't have to worry about setting them up yourself.

Specifying parameters: The code then defines specific parameters for the language model. 

'MAX_NEW_TOKENS' sets the limit on the number of words the model can generate in one go. 
'TEMPERATURE' adjusts how creative or predictable the generated text is.

Setting up Llama 3 model: Next, the LLAMA3 model is set up using a model ID, the provided 
credentials, chosen parameters, and a project ID.

Creating an object for Llama 3: The code creates an object named llm, which is used to interact 
with the Llama 3 model. A model object, LLAMA3_model, is created using the Model class, which 
is initialized with a specific model ID, credentials, parameters, and project ID. Then, an 
instance of WatsonxLLM is created with LLAMA3_model as an argument, initializing the language 
model hub llm object.

Generating and printing response: Finally, 'llm' is used to generate a response to the question, 
"How to read a book effectively?" The response is then printed out.
'''

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

my_credentials = {
    "url"    : "https://us-south.ml.cloud.ibm.com"
}

params = {
        GenParams.MAX_NEW_TOKENS: 700, # The maximum number of tokens that the model can generate in a single run.
        GenParams.TEMPERATURE: 0.1,   # A parameter that controls the randomness of the token generation. A lower value makes the generation more deterministic, while a higher value introduces more randomness.
    }

LLAMA2_model = Model(
        model_id= 'meta-llama/llama-3-2-11b-vision-instruct', 
        credentials=my_credentials,
        params=params,
        project_id="skills-network",  
        )

llm = WatsonxLLM(LLAMA2_model)  

print(llm("How to read a book effectively?"))

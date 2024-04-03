import numpy as np
from openai import OpenAI

_ = load_dotenv('openAI.env')
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('openAI_api_key'),
)

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

#Generar binario
desc = "película de la segunda guerra mundial"
emb = get_embedding(desc)

#Recuperar lista a partir del archivo binario
emb_binary = np.array(emb).tobytes()
rec_emb = list(np.frombuffer(emb_binary, dtype=arr.dtype))
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key="pcsk_4mGPBD_MSvWEvMCg5uJe1p2nbLY8VqiSRwuLbKZwdRWwP54cyvBtmKXXARYhH4JH4u1mqp")


index = pc.Index("cuhbot")

embeddings=OpenAIEmbeddings(api_key = "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")

vector_store = PineconeVectorStore(embedding=embeddings, index=index)

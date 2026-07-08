from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key="pcsk_6yfVHZ_JxYdjn9grNyhzpe4zray1FqChd5h4NGD833eX4BArSQymNS3MdLjcCNrL3RxFLR")


index = pc.Index("rag")

embeddings=OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = PineconeVectorStore(embedding=embeddings, index=index)

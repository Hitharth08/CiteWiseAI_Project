from core.embedder import EmbeddingModel
from core.vectorstore import VectorStore


class Retriever:

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.store = VectorStore(384)

    def build(self, chunks):
        embeddings = self.embedder.encode(chunks)
        self.store.add(embeddings, chunks)

    def retrieve(self, question):
        embedding = self.embedder.encode([question])[0]
        return self.store.search(embedding)
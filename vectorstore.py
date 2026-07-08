import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add(self, embeddings, chunks):
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.chunks.extend(chunks)

    def search(self, embedding, k=3):

        embedding = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(embedding, k)

        results = []

        for idx in indices[0]:

            if idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results
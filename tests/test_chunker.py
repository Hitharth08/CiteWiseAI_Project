from core.chunker import TextChunker

def test_chunk_creation():
    text = "Hello World " * 200
    chunks = TextChunker.chunk(text)

    assert len(chunks) > 0
    assert isinstance(chunks, list)
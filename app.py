import streamlit as st

from core.parser import DocumentParser
from core.chunker import TextChunker
from core.retriever import Retriever
from core.citations import CitationEngine
from core.llm import LLM

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CiteWise AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📚 CiteWise AI")
st.sidebar.markdown("### Research Agent")
st.sidebar.markdown("---")

st.sidebar.success("✅ Upload your research documents")

st.sidebar.info("""
Supported Files

• PDF

• DOCX

• TXT
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Technology")

st.sidebar.write("🧠 Groq LLM")
st.sidebar.write("📚 FAISS")
st.sidebar.write("🔍 Sentence Transformers")
st.sidebar.write("📄 PyMuPDF")

st.sidebar.markdown("---")
st.sidebar.caption("ROOMAN AI Assignment")

# ---------------- MAIN PAGE ---------------- #

st.title("📚 CiteWise AI")

st.markdown(
"""
### Intelligent Research Agent with Citations

Ask questions from your uploaded research documents using
Retrieval-Augmented Generation (RAG).
"""
)

st.divider()

# ---------------- FILE UPLOAD ---------------- #

uploaded_files = st.file_uploader(
    "📄 Upload PDF / DOCX / TXT",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

st.divider()

# ---------------- QUESTION ---------------- #

question = st.text_input(
    "💬 Ask your research question"
)

# ---------------- BUTTON ---------------- #

if st.button("🔍 Research", use_container_width=True):

    if not uploaded_files:
        st.warning("Please upload at least one document.")
        st.stop()

    if not question:
        st.warning("Please enter a question.")
        st.stop()

    all_chunks = []

    with st.spinner("📄 Reading documents..."):

        for file in uploaded_files:

            text = DocumentParser.parse(file)

            chunks = TextChunker.chunk(text)

            all_chunks.extend(chunks)

    with st.spinner("🧠 Creating embeddings..."):

        retriever = Retriever()

        retriever.build(all_chunks)

    with st.spinner("🔍 Searching relevant information..."):

        retrieved = retriever.retrieve(question)

    context = "\n\n".join(retrieved)

    with st.spinner("🤖 Generating AI response..."):

        llm = LLM()

        answer = llm.generate(
            question,
            context
        )

    st.divider()

    st.success("✅ Answer")

    st.write(answer)

    st.divider()

    st.subheader("📚 Source Citations")

    st.code(
        CitationEngine.format(retrieved)
    )

st.divider()

st.caption("© 2026 CiteWise AI | Research Agent with Citations")
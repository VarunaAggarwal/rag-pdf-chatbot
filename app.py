import streamlit as st

from src.rag_pipeline import build_rag_from_uploaded_files, ask_question


st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="📚"
)


st.title("📚 RAG PDF Chatbot")

st.write(
    "Upload one or more PDF documents and ask questions about them."
)


uploaded_files = st.file_uploader(
    "Upload your PDF documents",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files:

    st.success(
        f"{len(uploaded_files)} PDF(s) uploaded successfully!"
    )

    st.subheader("Uploaded Documents")

    for file in uploaded_files:

        st.write(f"📄 {file.name}")


    with st.spinner("Building knowledge base..."):

        index, chunks, sources = build_rag_from_uploaded_files(
            uploaded_files
        )


    st.success("Knowledge base ready! You can now ask questions.")


    question = st.text_input(
        "Ask a question about your documents:"
    )


    if st.button("Ask"):

        if question:

            with st.spinner("Finding the answer..."):

                answer = ask_question(
                    question,
                    index,
                    chunks
                )

            st.subheader("Answer")

            st.write(answer)

            st.subheader("Source")

            for source in set(sources):

                st.write(f"📄 {source}")

        else:

            st.warning("Please enter a question.")
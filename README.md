# LLM Multilingual RAG
A small project to study LLM Multilingual RAG and Langchain. The main objective of this project is to create a helpful chatbot that can answer customer questions about information retrieval from vector databases.

## Use in project
1. Poetry: Python packaging and dependency management
2. Model [vilm/vinallama-7b-chat-GGUF](https://huggingface.co/vilm/vinallama-7b-chat-GGUF)

## Setup project
1. Download the model `vinallama-7b-chat_q5_0.gguf` from [vilm/vinallama-7b-chat-GGUF](https://huggingface.co/vilm/vinallama-7b-chat-GGUF/resolve/main/vinallama-7b-chat_q5_0.gguf?download=true) and save it to `model/vinallama-7b-chat_q5_0.gguf`.
2. Install Poetry:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -

    poetry --version # Poetry (version 1.8.3)
    ```

    If you encounter the error `dyld[20269]: Library not loaded` when running Poetry, please uninstall it first using the following command:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    ```
3. Install package dependencies and activate the Poetry shell:
    ```bash
    poetry shell # Activate the Poetry shell

    poetry install
    ```

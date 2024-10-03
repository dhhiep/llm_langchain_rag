# LLM Multilingual RAG
A small project to study LLM Multilingual RAG and Langchain. The main objective of this project is to create a helpful chatbot that can answer customer questions about information retrieval from vector databases.

## Use in project
1. Poetry: Python packaging and dependency management
2. [Ollama](https://github.com/ollama/ollama): An open-source project that serves as a powerful and user-friendly platform for running LLMs on your local machine
3. Model: [llama3.2](https://www.llama.com/)
4. FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints
5. Chatbot: A chatbot that can answer customer questions about information retrieval from vector databases

## Setup project
1. Install Poetry:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -

    python --version # Python 3.12.4
    poetry --version # Poetry (version 1.8.3)
    ```

    If you encounter the error `dyld[20269]: Library not loaded` when running Poetry, please uninstall it first using the following command:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    ```

2. Install package dependencies and activate the Poetry shell:
    ```bash
    poetry shell # Activate the Poetry shell
    poetry install
    ```

3. Install Ollama: Go to [Ollama](https://ollama.com/download) and follow the instructions to install it on your local machine.

4. Download model llama3.2 and start the server:
    ```bash
    # List models of Ollama https://ollama.com/library
    ollama pull llama3.2:3b
    ollama serve

    # Test the server
    curl http://localhost:11434/api/generate -d '{
      "model": "llama3.2:3b",
      "prompt": "Why is the sky blue?",
      "stream": false
    }'

    # Response
    # {"model":"llama3.2:3b","created_at":"2024-10-02T23:27:39.681843Z","response":"The sky appears blue to us during the daytime due to a phenomenon called Rayleigh scattering, named after the British physicist Lord Rayleigh. Here's what happens:\n\n1. **Sunlight enters Earth's atmosphere**: When sunlight enters our planet's atmosphere, it consists of a spectrum of colors, including all the colors of the visible spectrum (red, orange, yellow, green, blue, indigo, and violet).\n2. **Scattering occurs**: As sunlight travels through the atmosphere, it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2). These molecules scatter the light in all directions.\n3. **Shorter wavelengths scattered more**: The smaller (shorter) wavelengths of light, like blue and violet, are scattered more than the longer wavelengths (like red and orange). This is because the smaller molecules are more effective at scattering shorter wavelengths.\n4. **Blue light dominates our view**: As a result, when we look up at the sky, we see mostly the scattered blue light from all directions. This is why the sky appears blue to us during the daytime.\n\nIt's worth noting that:\n\n* During sunrise and sunset, the sky can appear more red or orange due to a different scattering process involving atmospheric particles and water vapor.\n* At night, the sky appears dark because there's no sunlight to scatter.\n* In cloudy or hazy conditions, the color of the sky can be affected by other scattering processes.\n\nSo, that's why the sky is blue!","done":true,"done_reason":"stop","context":[...],"total_duration":9894272250,"load_duration":20968542,"prompt_eval_count":31,"prompt_eval_duration":3369451000,"eval_count":302,"eval_duration":6497741000}%

    curl http://localhost:11434/api/generate -d '{
      "model": "llama3.2:3b",
      "prompt": "Tại sao bầu trời màu xanh?",
      "stream": false
    }'

    # Response
    # {"model":"llama3.2:3b","created_at":"2024-10-02T23:29:21.336769Z","response":"Bầu trời thường được nhìn thấy với màu xanh do hiện tượng phân tử khí trong không khí. Các phân tử khí là những hạt nhỏ, nhẹ và di chuyển nhanh, tạo ra hiệu ứng pha màu khi chiếu sáng từ mặt trời.\n\nKhi ánh sáng mặt trời đi qua không khí, các phân tử khí này sẽ hấp thụ hoặc phản xạ một số bước sóng của ánh sáng. Màu xanh thường được hấp thụ tốt bởi các phân tử khí, vì vậy phần lớn ánh sáng xanh sẽ bị mất đi trước khi nó có thể đến mắt chúng ta.\n\nÁnh sáng còn lại, với màu sắc khác nhau, sẽ được phản xạ trở lại không khí và đến mắt chúng ta. Do đó, bầu trời thường được nhìn thấy với màu xanh lá cây hoặc xanh dương nhẹ, tùy thuộc vào độ cao của ánh sáng mặt trời trong bầu khí quyển và sự hiện diện của các phân tử khí.\n\nNgoài ra, còn có một số yếu tố khác ảnh hưởng đến màu sắc của bầu trời, chẳng hạn như:\n\n- Thời gian ngày: Bầu trời thường có màu đậm hơn vào buổi chiều và buổi tối do sự hiện diện của ánh sáng Mặt Trời.\n- Độ cao của ánh sáng mặt trời: Ánh sáng mặt trời thấp hơn khi chúng ta ở gần địa cực, điều này làm cho bầu trời có màu xanh đậm hơn.\n- Sự hiện diện của các aerosol trong không khí: Các aerosol như bụi, hơi nước và khí clo cũng có thể ảnh hưởng đến màu sắc của bầu trời.\n\nTóm lại, màu xanh của bầu trời là kết quả của việc hấp thụ hoặc phản xạ ánh sáng mặt trời bởi các phân tử khí trong không khí.","done":true,"done_reason":"stop","context":[...],"total_duration":9896445250,"load_duration":30707042,"prompt_eval_count":33,"prompt_eval_duration":2494202000,"eval_count":344,"eval_duration":7369613000}%
    ```
    **Note**:
    - If you error `Error: listen tcp 127.0.0.1:11434: bind: address already in use`, please close the Ollama application and run the command `ollama serve` again.

5. Load PDF, embedding data and store to vector DB

    ```bash
    cp .env.template .env

    python prepare_vector_db.py

    ls data/db
    # index.faiss index.pkl
    ```

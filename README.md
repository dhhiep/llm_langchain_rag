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
6. Test QA with RAG from `data/pdf/*.pdf`

    ```bash
    py main.py

    # Answer:  {'question': 'Mã chương ngành đào tạo toán tin là gì?', 'result': 'Mã ngành đào tạo toán tin là 7460117.'}
    # Answer:  {'question': 'Chương trình đào tạo ngành toán tin thì đào tạo ở đâu?', 'result': 'Theo dự thảo Chương trình đào tạo ngành Toán tin Khóa 2023, chương trình đào tạo sẽ được thực hiện tại hai cơ sở:\n\n1. Cơ sở 1: 227 Nguyễn Văn Cừ, P4, Q5, Thành Phố Hồ Chí Minh.\n2. Cơ sở 2: Phường Linh Trung, Thành Phố Thủ Đức, Thành phố Hồ Chí Minh.\n\nVậy, chương trình đào tạo ngành Toán tin sẽ được thực hiện tại hai cơ sở này.'}
    # Answer:  {'question': 'Chương trình giảng dạy ngành toán tin, mục tiêu MT1.1 là gì?', 'result': 'Mục tiêu MT1.1 của chương trình giảng dạy ngành toán tin là "Khái quát kiến thức khoa học và xã hội cơ bản, kiến thức nền tảng Toán học".'}
    # Answer:  {'question': 'Tóm tắt cấu trúc của chương trình đào tạo', 'result': 'Cấu trúc của chương trình đào tạo Cử nhân Toán Tin như sau:\n\n1. Thông tin chung về chương trình đào tạo\n\t* Tên ngành đào tạo: Toán Tin (tiếng Việt) / Mathematics and Computer Sciences (tiếng Anh)\n\t* Mã ngành đào tạo: 7460117\n\t* Trình độ đào tạo: Đại học\n\t* Tên chương trình: Cử nhân Toán Tin\n\t* Loại hình đào tạo: Chính quy\n\t* Thời gian đào tạo: 4 năm\n2. Mục tiêu đào tạo\n\t* Mục tiêu chung của chương trình là đào tạo cử nhân có kiến thức và kỹ năng về toán tin.\n3. Thông tin chi tiết về chương trình đào tạo\n\t* Ngôn ngữ giảng dạy: Tiếng Việt\n\t* Nơi đào tạo:\n\t\t+ Cơ sở 1: 227 Nguyễn Văn Cừ, P4, Q5, Thành Phố Hồ Chí Minh\n\t\t+ Cơ sở 2: Phường Linh Trung, Thành Phố Thủ Đức, Thành phố Hồ Chí Minh'}
    # Answer:  {'question': 'Tiêu chuẩn và điều kiện làm thành viên Hội đồng quản trị', 'result': 'Theo Điều 18 của Điều lệ Ngân hàng, tiêu chuẩn và điều kiện làm thành viên Hội đồng quản trị là:\n\n1. Có năng lực hành vi dân sự đầy đủ, không thuộc đối tượng bị cấm quản lý Ngân hàng theo quy định của Luật Doanh nghiệp;\n2. Có trình độ chuyên môn phù hợp với vị trí đảm nhiệm;\n3. Có sức khỏe, phẩm chất đạo đức tốt và trung thực;\n4. Không có tranh chấp hoặc khiếu nại về quyền lợi, nghĩa vụ giữa thành viên Hội đồng quản trị với nhau hoặc với Ngân hàng.\n5. Đáp ứng các tiêu chuẩn và điều kiện khác theo quy định của Luật Doanh nghiệp và Điều lệ Ngân hàng.'}
    # Answer:  {'question': 'Thời hạn xóa kỷ luật cho người lao động là bao lâu?', 'result': 'Thời hạn xóa kỷ luật cho người lao động là 03 tháng nếu bị khiển trách sau 03 tháng hoặc bị xử lý kỷ luật bằng hình thức kéo dài thời hạn nâng lương sau 06 tháng kể từ ngày bị xử lý, nếu không tái phạm thì đương nhiên được xóa kỷ luật.'}
    ```

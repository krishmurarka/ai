# Model Runner and Monitoring

Welcome to the Model Runner and Monitor repository! This repository provides functionality to seamlessly run OpenAI and open-source models and monitor various metrics such as cost, latency, and other performance indicators.

## Features

- **Seamless Model Execution**: Run OpenAI and open-source models with ease.
- **Monitoring Capabilities**: Easily monitor the cost, latency, and other performance metrics of model calls.
- **Customizable**: Adapt the monitoring functionality to suit your specific requirements.
- **User-friendly Interface**: Intuitive interface for managing model executions and monitoring metrics.

## Installation

Follow these steps to set up Model Runner and Monitor on your system:

1. **Create a Virtual Environment Using Conda**:

    ```bash
    conda create -p venv python==3.12 -y
    ```

2. **Activate the Environment**:

    ```bash
    conda activate venv
    ```

3. **Install Required Packages**:

    Install all the required packages from `requirements.txt` using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create `.env` File**:

    - Create a `.env` file similar to `.env-example`. You need to obtain two keys:
      - **OpenAI Key**: If you want to run OpenAI calls.
      - **Langchain Key**: If you want monitoring from Langsmith.
     
5. ** download oolama in your computer to use open-source models **

## Usage

1. **Run the model with langsmith using streamlit**:

    ```bash
    streamlit run src/main.py
    ```

2. **Running Open AI API directly without streamlit**:

    ```bash
    python src/main.py
    ```

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

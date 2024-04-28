from models.local_lama import run_ollama
from models.open_ai import run_open_ai_langchain
from models.open_ai_api import run_open_ai_api


def main():

    # To run Open AI from Langchain and use Monitoring of Langsmith
    # run_open_ai_langchain()

    # To Run OpenSource Models
    run_ollama()

    # To Directly run open AI from python openai
    run_open_ai_api()


if __name__ == "__main__":
    main()

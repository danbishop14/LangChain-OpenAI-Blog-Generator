# Blog Generator App

This is a blog generator app powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and created by [@DanBishop](https://www.linkedin.com/in/daniel-bishop-0900971a3/). The app allows users to input an idea and generate a 1000-word article with specified tone, writing style, and complexity level. The app uses the OpenAI API to generate the content and requires users to input their own API key.

## How to Deploy

1. Fork or download this repository.
2. Create an account on [Streamlit Cloud](https://streamlit.io/cloud).
3. In Streamlit Cloud, go to the "New App" section and choose your GitHub repository.
4. Make sure the `app.py` file is selected as the main app file.
5. Click "Deploy" and wait for the app to be published.

## Setup

1. Make sure you have Python 3.6 or later installed.
2. Install the required packages listed in the `requirements.txt` file.
3. Obtain an OpenAI API key from [OpenAI](https://beta.openai.com/signup/) and set it as an environment variable.

## Local Deployment

1. Clone the repository.
2. Install the required packages listed in the `requirements.txt` file.
3. Set the OpenAI API key as an environment variable.
4. Run the command `streamlit run main.py` in your terminal.

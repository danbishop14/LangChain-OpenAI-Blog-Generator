import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

# Prompt template for the blog generator
template = """
    You are a technical copywriter fluent in all subjects. You are developing a blog article about "{idea}" with a "{tone}" tone.
    Create a(n) article that covers the topic in {complexity} detail with a title, headline, engaging introduction, and provide a few interesting 
    facts and statistics with hyperlinks and the formatting to fit medium.com’s editing language in a {style} style.
"""

prompt = PromptTemplate(
    input_variables=["tone", "style", "complexity", "idea"],
    template=template,
)

# Function to load the language model
def load_LLM(openai_api_key):
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

# Setting the Streamlit page configuration
st.set_page_config(page_title="Blog Generator", page_icon=":robot:")
st.header("Blog Generator")

if "generated_blog" not in st.session_state:
    st.session_state.generated_blog = ""

# Displaying the credits
col1, col2 = st.columns(2)
with col1:
    st.markdown("Powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and created by \
                [@DanBishop](https://www.linkedin.com/in/daniel-bishop-0900971a3/).")

st.markdown("---")

# Function to get the OpenAI API key
def get_api_key():
    if 'api_key_value' not in st.session_state:
        st.session_state.api_key_value = ""
        st.session_state.api_key_value = st.text_input(
            label="OpenAI API Key",
            value=st.session_state.api_key_value,
            placeholder="Ex: sk-2twmA8tfCb8un4...",
            key="openai_api_key_input",
            type="default")
    else:
        st.session_state.api_key_value = st.text_input(
            label="OpenAI API Key",
            value=st.session_state.api_key_value,
            placeholder="Ex: sk-2twmA8tfCb8un4...",
            key="openai_api_key_input",
            type="password")

    return st.session_state.api_key_value

openai_api_key = get_api_key()

# Displaying the options for tone, style, and complexity
col1, col2, col3 = st.columns(3)
with col1:
    option_tone = st.selectbox(
        'Select the tone:',
        ('Informative', 'Conversational', 'Persuasive'))
with col2:
    option_style = st.selectbox(
        'Select the writing style:',
        ('Professional', 'Casual'))
with col3:
    option_dialect = st.selectbox(
        'Select the complexity level:',
        ('Basic', 'Intermediate', 'Advanced'))

# Function to get the idea input
def get_text():
    input_text = st.text_area(label="Idea Input", label_visibility='collapsed', placeholder="Enter your idea...", key="idea_input")
    return input_text

idea_input = get_text()

if len(idea_input.split(" ")) > 700:
    st.write("Please enter a shorter idea. The maximum length is 700 words.")
    st.stop()

# Function to update the text area with an example
def update_text_with_example():
    st.session_state.idea_input = "Can squirrels communicate with ghosts?"

# Button Markdown
st.markdown("""
    <style>
        .big-btn {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.button("*See An Example*", type='secondary', help="Click to see an example of an idea you will could generate a blog from.", on_click=update_text_with_example)
with col2:
    generate_blog_button = st.button("Generate Blog")

st.markdown("---")

# Generating the blog
if generate_blog_button:
    if idea_input:
        if not openai_api_key:
            st.stop()
        llm = load_LLM(openai_api_key=openai_api_key)
        prompt_with_idea = prompt.format(tone=option_tone, style=option_style, complexity=option_dialect, idea=idea_input)
        st.session_state.generated_blog = llm(prompt_with_idea)
else:
    if not openai_api_key:
        st.warning('Please insert your OpenAI API Key. Instructions found [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).', icon="⚠️")

# Display the generated_blog from the session state
st.write(st.session_state.generated_blog)

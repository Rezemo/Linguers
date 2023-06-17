import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All

PATH = 'D:\Linguers\Linguers\GPT4All-13B-snoozy.ggmlv3.q4_0.bin'

llm = GPT4All(model=PATH, verbose=True)

# prompt = PromptTemplate(input_variables=['subject'], template="""
#    what is : {subject}
#     """)

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['subject'],
    template='I will give you a subject and I need you to give me the main subtopics (most 20 percent important) to this subject (subtopics that give me 80 percent of benefit). Then explain each subtopic in a summarized and informative way step by step then give me 3 questions for each subtopic to make sure that the subject is understandable. And in the end give a plan to revise and memorize the subject (print the output in markdown format) subject: {subject}'
)



llm_chain = LLMChain(prompt=title_template, llm=llm)

st.title('🦜🔗 GPT4ALL Y\'All')
st.info('This is using the GPT4All model!')
prompt = st.text_input('Enter your prompt here!')

if prompt: 
    response = llm_chain.run(prompt)
    print(response)
    st.write(response)






# script_template = PromptTemplate(
#     input_variables = ['title', 'wikipedia_research'],
#     template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
# )

# # Memory
# title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
# script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# # Llms
# llm = OpenAI(temperature=0.9)
# title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
# script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

# wiki = WikipediaAPIWrapper()

# # Show stuff to the screen if there's a prompt
if prompt:
    print(prompt)
#     title = title_chain.run(prompt)
#     wiki_research = wiki.run(prompt)
#     script = script_chain.run(title=title, wikipedia_research=wiki_research)

#     st.write(title)
#     st.write(script)

#     with st.expander('Title History'):
#         st.info(title_memory.buffer)

#     with st.expander('Script History'):
#         st.info(script_memory.buffer)

#     with st.expander('Wikipedia Research'):
#         st.info(wiki_research)

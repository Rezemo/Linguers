# Bring in deps
import os
# from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper


apikey = "key"
os.environ['OPENAI_API_KEY'] = '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'

# App framework
st.title('AI Agent for Academic Study')
prompt = st.text_input('Put your topic of interest here, and let\'s learn together')


subject_template = PromptTemplate(
    input_variables = ['subject'],
    template="""I will give you a subject and I need you to give me the main subtopics (most 20 percent important) to this subject (subtopics that give me 80 percent of benefit)   
    the given topic is: {subject}. Futhermore, ensure that each subtopic is closely related to the main {subject} and can be covered within a reasonable time frame . """
)

# script_template1 = PromptTemplate(
#     input_variables = ['subject'],
#     template='break down the {subject} into smaller subtopics. Ensure that each subtopic is closely related to the main {subject} and can be covered within a reasonable time frame . '
# )

script_template2 = PromptTemplate(
    input_variables = ['subject'],
    template='Use examples and illustrations to help students visualize the each subtopic of the given {subject}.'
)

script_template3 = PromptTemplate(
    input_variables = ['subject'],
    template='provide a full summary of the subtopics of {subject} and a revision plan. The summary should be a brief overview of the entire subtopics of the {subject}, while the revision plan should outline the duration and time needed to complete each subpart.'
)

script_template4 = PromptTemplate(
    input_variables = ['subject'],
    template='create a table that summarizes each subtopic of the {subject}. This table can be used as a quick reference guide for students to review the content and refresh their memory. The table should include the following: each subtopics of the {subject}, learning objective, key concepts, and example/illustrations'
)



# # Memory
title_memory = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
script_memory2 = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
script_memory3 = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
script_memory4 = ConversationBufferMemory(input_key='subject', memory_key='chat_history')


# # Llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=subject_template, verbose=True, output_key='subject', memory=title_memory)
# script_chain1 = LLMChain(llm=llm, prompt=script_template1, verbose=True, output_key='script', memory=script_memory)
script_chain2 = LLMChain(llm=llm, prompt=script_template2, verbose=True, output_key='script2', memory=script_memory)
script_chain3 = LLMChain(llm=llm, prompt=script_template3, verbose=True, output_key='script3', memory=script_memory)
script_chain4 = LLMChain(llm=llm, prompt=script_template4, verbose=True, output_key='script4', memory=script_memory)


# # Show stuff to the screen if there's a prompt
if prompt:
    print(prompt)
    subject = title_chain.run(prompt)
    # script1 = script_chain1.run(subject=prompt)
    script2 = script_chain2.run(subject=prompt)
    script3 = script_chain3.run(subject=prompt)
    script4 = script_chain4.run(subject=prompt)

    st.write(subject)
    # st.write(script1)
    st.write(script2)
    st.write(script3)
    st.write(script4)

    


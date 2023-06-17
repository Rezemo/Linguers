# # Bring in deps
# import os
# # from apikey import apikey

# import streamlit as st
# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain
# from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper


# apikey = "key"
# os.environ['OPENAI_API_KEY'] = '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'

# # App framework
# st.title('AI Agent for Academic Study')
# prompt = st.text_input('Put your topic of interest here, and let\'s learn together')

# # Prompt templates
# # subject_template = PromptTemplate(
# #     input_variables = ['topic'],
# #     template='write me a youtube video title about {topic}'
# # )




# # Serrrrrrrrrrrrrrrrrrrrrrrrry 
# # subject_template = PromptTemplate(
# #     input_variables = ['subject'],
# #     template="""I will give you a subject and I need you to give me the main subtopics (most 20 percent important) to this subject (subtopics that give me 80 percent of benefit).  
# #     the given subject is: {subject} """
# # )

# # script_template1 = PromptTemplate(
# #     input_variables = ['subject'],
# #     template='explain each subtopic in a summarized and informative way step by step then give me 3 questions for each subtopic to make sure that the {subject} is understandable. '
# # )

# # script_template2 = PromptTemplate(
# #     input_variables = ['subject'],
# #     template='Also, in the end give a plan to revise and memorize the {subject} (print the output in markdown format)'
# # )




# subject_template = PromptTemplate(
#     input_variables = ['subject'],
#     template="""Identify the main topic and objectives by clearly defining the main topic and the learning objectives that the student want to achieve.   
#     the given topic is: {subject} """
# )

# script_template1 = PromptTemplate(
#     input_variables = ['subject'],
#     template='break down the topic into smaller subparts. Ensure that each subpart is closely related to the main {subject} and can be covered within a reasonable time frame . '
# )

# script_template2 = PromptTemplate(
#     input_variables = ['subject'],
#     template='Use examples and illustrations to help students visualize the {subject} being taught.'
# )

# script_template3 = PromptTemplate(
#     input_variables = ['subject'],
#     template='provide a full summary of the {subject} and a revision plan. The summary should be a brief overview of the entire {subject}, while the revision plan should outline the duration and time needed to complete each subpart.'
# )

# script_template4 = PromptTemplate(
#     input_variables = ['subject'],
#     template='create a table that summarizes the whole {subject}. This table can be used as a quick reference guide for students to review the content and refresh their memory. The table should include the following: main {subject}, learning objective, key concepts, and example/illustrations'
# )



# # # Memory
# title_memory = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
# script_memory = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
# script_memory2 = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
# script_memory3 = ConversationBufferMemory(input_key='subject', memory_key='chat_history')
# script_memory4 = ConversationBufferMemory(input_key='subject', memory_key='chat_history')


# # # Llms
# llm = OpenAI(temperature=0.9)
# title_chain = LLMChain(llm=llm, prompt=subject_template, verbose=True, output_key='subject', memory=title_memory)
# script_chain1 = LLMChain(llm=llm, prompt=script_template1, verbose=True, output_key='script', memory=script_memory)
# script_chain2 = LLMChain(llm=llm, prompt=script_template2, verbose=True, output_key='script2', memory=script_memory)
# script_chain3 = LLMChain(llm=llm, prompt=script_template3, verbose=True, output_key='script3', memory=script_memory)
# script_chain4 = LLMChain(llm=llm, prompt=script_template4, verbose=True, output_key='script4', memory=script_memory)

# # wiki = WikipediaAPIWrapper()

# # # Show stuff to the screen if there's a prompt
# if prompt:
#     print(prompt)
#     subject = title_chain.run(prompt)
# #     wiki_research = wiki.run(prompt)
#     script1 = script_chain1.run(subject=prompt)
#     script2 = script_chain2.run(subject=prompt)
#     script3 = script_chain3.run(subject=prompt)
#     script4 = script_chain4.run(subject=prompt)

#     st.write(subject)
#     st.write(script1)
#     st.write(script2)
#     st.write(script3)
#     st.write(script4)

#     with st.expander('Subject History'):
#         st.info(title_memory.buffer)

#     with st.expander('Script History'):
#         st.info(script_memory.buffer)

#     with st.expander('Script History'):
#         st.info(script_memory2.buffer)

#     with st.expander('Script History'):
#         st.info(script_memory3.buffer)

#     with st.expander('Script History'):
#         st.info(script_memory4.buffer)

# #     with st.expander('Wikipedia Research'):
# #         st.info(wiki_research)

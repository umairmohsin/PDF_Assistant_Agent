import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.openai import OpenAIChat



#Initialize
st.title("AI Search Assistant 🤖")
st.caption("An AI-powered search assistant to help you find information on the web.")


#Set openAI key
openai_key = st.text_input("Enter OpenAI API Key", type="password")

if openai_key:
    assistant = Assistant(
    llm=OpenAIChat(
        model="gpt-4o",
        max_tokens=1024,
        temperature=0.9,
        api_key=openai_key) , tools=[DuckDuckGo()], show_tool_calls=True
    )

    #Search the query from user input    
    query =st.text_input("Enter your query" , type = "default")

    if query:
        #Get response from the AI Assitant 
        response = assistant.run(query , stream = False)
        st.write(response)    
        

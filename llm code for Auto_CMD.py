from langchain_community.tools import ShellTool
shell_tool = shell_tool()

#shell_tool.run({"commands": ["useradd vimal"]})

from langchain.llms import OpenAI

mymodel = OpenAI(openai_api_key="please enter your API key ")

from langchain.agents import AgentType

from langchain.agents import initialize_agent


mycmd_chain = initialize_agent(llm=mymodel , tools=[shell_tool] , agent="zero-shot-react-description" , verbose= True)

myprompt = input("Enter your prompt") 

output = mycmd_chain.run(myprompt)
print(ouput)

# from langchain_ollama import ChatOllama
# from langchain.memory import ConversationBufferWindowMemory
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# memory = ConversationBufferWindowMemory(k=5)

# prompt = PromptTemplate(
#     input_variables=["history", "input"],
#     template=(
#         "You are a chatbot that remembers past interactions.\n"
#         "Use your memory to answer based on previous discussions.\n\n"
#         "{history}\n"
#         "User: {input}\n"
#         "Assistant:"
#     )
# )
# llm = ChatOllama(model="gemma:2b")

# conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)


# print("🤖 Chatbot is ready! Type 'exit' to stop.\n")
# history = ""

# while True:
#     user_input = input("You: ")
    
#     if user_input.lower() in ["exit", "quit"]:
#         print("Chatbot: Goodbye! 👋")
#         break

#     # Get response from chatbot
#     response = conversation.invoke({"history": history, "input": user_input})

#     # Extract only the assistant's message
#     assistant_reply = response.get("text", "Sorry, I didn't understand that.")

#     # Update history
#     history += f"\nUser: {user_input}\nAssistant: {assistant_reply}"

#     print(f"Chatbot: {assistant_reply}")

from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Memory to store last 3 messages
memory = ConversationBufferWindowMemory(k=3)

# Define prompt template
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=(
        "You are a chatbot that remembers past interactions.\n"
        "Use your memory to answer based on previous discussions.\n\n"
        "{history}\n"
        "User: {input}\n"
        "Assistant:"
    )
)

# Load the Gemma model
llm = ChatOllama(model="gemma:2b")

# Define conversation chain
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)

def get_chatbot_response(user_input, history=""):
    """Function to get chatbot response."""
    response = conversation.invoke({"history": history, "input": user_input})
    
    # Extract response text
    return response.get("text", "Sorry, I didn't understand that.")

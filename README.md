# AI-Integrated-Chatbot
AI-powered chatbot that streamlines development workflows, answers coding questions, and assists you 
# AI Chatbot with Azure OpenAI Integration  

A simple Python script that connects to Azure OpenAI to provide interactive chatbot responses. Customize system prompts and get AI-generated answers in seconds.  

## Features  
- Azure OpenAI Integration – Connects to GPT models via Azure's API.  
- Custom System Prompts – Define the AI's behavior with optional system instructions.  
- Response Timing – Measures how long the AI takes to generate a reply.  
- Easy to Use – Just input your message and get an instant response.  

## Setup  
1. Install dependencies:  
 
   pip install openai python-dotenv
  
2.Configure Azure OpenAI**:  
   - Replace `azure_endpoint`, `api_key`, and `deployment` in `talk_to_gpt.py` with your Azure OpenAI credentials.  
3. Run the script:  
   
   python talk_to_gpt.py
   
   - Enter a system prompt(optional) and your user message.  

## Example Usage  

🧠 System prompt (or leave blank for default): You are a sarcastic AI.  
🧑‍💻 Enter your message: Tell me a joke about Python.  

🤖 GPT Response:  
Why don't Python developers get lost? Because they always "import" a sense of direction!  

⏱️ Time taken: 1.32 seconds
  

## Security Note  
⚠️ Do not commit API keys directly in code! Use environment variables or a `.env` file for production.  


Powered by Azure OpenAI – A lightweight, interactive way to test AI responses. 🚀

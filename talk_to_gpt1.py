import time
from openai import AzureOpenAI

# Azure OpenAI configuration
azure_endpoint = "https://sfmaieffortlyh0311998918.openai.azure.com/"
api_version = "2024-12-01-preview"
api_key = "DOADseVQ8crpUZ1lSK1EwaozmCc7AphrMiZ6XXcl9ErcknYGpS0GJQQJ99BCACHYHv6XJ3w3AAAAACOGKgyn"
deployment = "gpt-4o-mini-task-1"

# Initialize client
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=azure_endpoint,
    api_key=api_key,
)

# ---- Take user input ----
system_prompt = input("🧠 System prompt (or leave blank for default): ").strip()
if not system_prompt:
    system_prompt = "You are a helpful assistant."

user_input = input("🧑‍💻 Enter your message: ").strip()

# ---- Start timing ----
start_time = time.time()

# ---- Generate response ----
response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    model=deployment,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    max_tokens=800,
)

# ---- End timing ----
end_time = time.time()
time_taken = end_time - start_time

# ---- Output ----
print("\n🤖 GPT Response:")
print(response.choices[0].message.content)
print(f"\n⏱️ Time taken: {time_taken:.2f} seconds")

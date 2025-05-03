from google import genai

client = genai.Client(api_key="AIzaSyC6WIfNDkvfj3LLXVDCcxuDwVKv_LPA3o4")
def ai_call (prompt) :

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents= prompt
    )
    print(response.text)


print("Enter the Prompt Below")
prompt = input()
ai_call(prompt)


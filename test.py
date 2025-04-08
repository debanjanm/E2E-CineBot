

from config import load_language_model

llm = load_language_model()

# question =  "Who are you?"
# question =  "Tum Kaun Ho?"
# question =  "Apni Bangla Janen?"
question = "Konse Cinema Mein Shah Rukh Khan Marne Ke Dobbara Janam Lete Hain?"

response = llm.invoke(question)
print(response.content)
import groq

# Set your Groq API key
groq_api_key ="Your API key"

client = groq.Client(api_key=groq_api_key)

def analyze_symptoms(symptoms):
    prompt = f"The user has the following symptoms: {symptoms}. What could be the possible causes and home remedies?"
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Use an appropriate Groq model
        messages=[{"role": "system", "content": "You are a medical expert."},
                  {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

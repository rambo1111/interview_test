import google.generativeai as genai
import json

def generate_interview_questions(skill, level):

    genai.configure(api_key="AIzaSyBWy_pZ_MPsPYdkLOChD0OvkW69UmeVerY")

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(f'''Act as a interviewer and give seven questions about {skill} in {level} level.
                                  Respond in JSON format.
                                  The JSON structure consists of a root object with a key interview_questions, which maps to an array of objects, each containing two key-value pairs: question (string) and topic (string), representing interview questions and their associated topics.
                                  Include some questions about real-life scenarios and case studies.
                                  Ask unique questions.
                                  Also at last add three DSA questions, which can be solved then and there in the interview, no need of extra library for them.''')
    
    response_json = json.loads(response.text[7:-4])

    # Save the JSON content to a file
    with open('questions.json', 'w') as json_file:
        json.dump(response_json, json_file, indent=4)

    print("JSON saved as questions.json'")

# Example usage
generate_interview_questions("Python", "intermediate")
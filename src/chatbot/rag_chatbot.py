import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured.")

client = genai.Client(
    api_key=API_KEY
)

def ask_gemini(context, question):

    prompt = f"""
You are Volkswagen Group Digital Solutions' Enterprise AI Assistant.

Answer ONLY using the information available in the provided context.

If the answer is not present in the context, respond exactly with:

"I couldn't find this information in the available company knowledge."

Do not guess.
Do not create policies.
Do not add external knowledge.

Always format answers like this:

# Topic

## Overview

Brief explanation.

## Details

Use bullet points.

## Process
(Only if applicable)

1. Step one
2. Step two
3. Step three

## Important Notes

Important information.

## Related Information

Mention related policy names if available.

Context:

{context}

Employee Question:

{question}
"""
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    
    return response.text

def ask_general_gemini(question):

    prompt = f"""
You are Volkswagen AI Assistant.

The user's question is NOT answered by the uploaded company documents.

Answer using your general knowledge.

If your answer is general knowledge,
clearly mention:

"This answer is based on general knowledge, not company documents."

Question:

{question}
"""
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"""
    ⚠️ AI service is temporarily unavailable.

    Reason:
    {str(e)}

    Please try again in a few seconds.
    """

    
    


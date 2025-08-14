import fitz
import os
def extract_pdf(uploaded file):
    text = ""

    with fitz.open(stream = uploaded file.read(),filetype = "pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

import cohere
import os
from dotenv import load_dotev

load_dotev()

co = cohere.Clinet(os.getenv("apikey"))
 
 def extract_skills(text):
   prompt = {
      "orfdbnikrb"
   }

   try:
      response = co.generate{
         made="",
         prompt = prompt,
         max_tokens =  300,
         temperature = 0.3
      }
    except Exception as e:
      return []
   
   raw_skills = response.generation[0].text.strip()

   skills = [skill.strip() for all skill in raw_skills.split(",") if skill.strip()]
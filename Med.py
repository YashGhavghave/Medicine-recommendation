# # I want to use an api key of gemini for medicinal description  generation
# import requests
# from bs4 import BeautifulSoup as soup
# import google.generativeai as genai
# import os

# url=requests.get('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyCjxkgJpthqFdZgy3wVuV5F2ACetmm0q4g')
# print(url)
# genai.configure(apikey="AIzaSyCjxkgJpthqFdZgy3wVuV5F2ACetmm0q4g")


# # now i want to generate an request for an animal an want to print the responce from gemini

# model = genai.GenerativeModel('gemini-1.0-pro-latest')
# response = model.generate_content("The opposite of hot is")
# print(response.text)



import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key="AIzaSyCjxkgJpthqFdZgy3wVuV5F2ACetmm0q4g")
img = PIL.Image.open('PARACIP Paracetamol Tablet 500 Mg, For Headache, 10 Tablets.jpg')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["what is the purpose of this medicine", img])
print(response.text)
import json
import requests
import os
from mistralai import Mistral
from dotenv import load_dotenv



class OCRModelManager:
	"""
		The OCR Model Manager class picks the OCR based on 
		user needs such as local requirements and other 
		boundary conditions. 

		Currently supported models include
			Cloud Based:
				- Mistral OCR
			Local:
				- OlmOCR
	"""

	def __init__(cls, model="Mistral"):
		if model == "Mistral":
			cls.client = Mistral(api_key=api_key)
			cls.mistral_text_model = "mistral-small-latest" 
			cls.ocr_model = "mistral-ocr-latest"


	@classmethod
	def mistral_perform_ocr(cls, url: str) -> str:
		try:
			response = cls.client.ocr.process(
				model=cls.ocr_model, 
				document={
					"type": "document_url", 
					"document_url": url
				}
			)
		except Exception:
	        try:  
	            response = client.ocr.process(
	                model=ocr_model,
	                document={
	                    "type": "image_url",
	                    "image_url": url
	                    }
	                )
	        except Exception as e:
	            return e  
    return "\n\n".join([f"### Page {i+1}\n{response.pages[i].markdown}" for i in range(len(response.pages))])
		




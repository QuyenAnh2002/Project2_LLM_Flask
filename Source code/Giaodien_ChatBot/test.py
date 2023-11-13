import requests
import json

url = "https://eflowai-api-stg.epacific.net/api/v1/internal-prediction/91108a28-3b8b-4268-b1d6-3e3a9bbe56d3"

payload = json.dumps({
  "question": "nguyên nhân dẫn đến bệnh béo phì là gì",
  "history": [],
  "chatId": "e9592d60-6019-403a-b59f-daa41fb4c6ba",
  "socketIOClientId": "0ErL6snTn5QGF82VAAAM"
})
headers = {
  'authority': 'eflowai-api-stg.epacific.net',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ3MTNVVHk5XzhVOFR6ZG9FMlNQeHVoMlJSYW9NQmtSMXVMQXQ5eDVrR1UwIn0.eyJleHAiOjE2OTk4MTM1MTQsImlhdCI6MTY5OTc3NzUxNSwiYXV0aF90aW1lIjoxNjk5Nzc3NTE0LCJqdGkiOiJjODNlYmMwZC04M2Y3LTQzMDgtYmU3Yi01NTI4NGE0M2FjZjYiLCJpc3MiOiJodHRwczovL2lkZW50aXR5LXN0Zy5lcGFjaWZpYy5uZXQvcmVhbG1zL2VwYWNpZmljIiwiYXVkIjpbInJlYWxtLW1hbmFnZW1lbnQiLCJhY2NvdW50Il0sInN1YiI6IjcyYjNmNTYxLTBiNDMtNGUwMi05MGU1LTE1ZDhhZDQ5M2Q1MCIsInR5cCI6IkJlYXJlciIsImF6cCI6IndvcmtmbG93YWkiLCJub25jZSI6IjM0NjRjZmZlLTAyOWQtNGI2MC1hZGI1LTYyZjUwOWFlMGY5ZSIsInNlc3Npb25fc3RhdGUiOiJjNTBkOWIyYS05MTNlLTQxZTYtOGRlMC00MDlkYzBkODRjNjIiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZXBhY2lmaWMiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsicmVhbG0tbWFuYWdlbWVudCI6eyJyb2xlcyI6WyJ2aWV3LWNsaWVudHMiLCJxdWVyeS1jbGllbnRzIl19LCJ3b3JrZmxvd2FpIjp7InJvbGVzIjpbImFsbG9uZSJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6ImM1MGQ5YjJhLTkxM2UtNDFlNi04ZGUwLTQwOWRjMGQ4NGM2MiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiS2hpw6ptIFRy4buLbmgiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJraGllbWRhaWNhIiwiZ2l2ZW5fbmFtZSI6IktoacOqbSIsImZhbWlseV9uYW1lIjoiVHLhu4tuaCIsImVtYWlsIjoidHJpbmhnaWFraGllbTAxMTJAZ21haWwuY29tIn0.iwziUtPVdfF8B_fuE1a0Bwllh05OcfnbC5YfhMdLWe9-rQGuUp_b4smiONeSV8mFPNMpJrj61Az1THZgbcUQ13wWvywPdigK_K65SSARxsa6fKmNHDFZnksDmVl4EhNr1sJihhjLvadGhsmIMt0351EYB7GLDXAfoAW0XIY0RK0Te4UIXd2rug7Ye-iu60btFB4za8xJb0_lRYvPUMPiiaoq0cuGBqN1AQwK7eo77wLj-UvyirYPKc6B1peI0wJgB3H-6kREy4CE5mOnyRlRFZf8GzVanlKqCBo_D-jqKQfUmpZo4bYmCG0mngHbUWwRgE2u9D_cmiPFOR0P-3FWWw',
  'content-type': 'application/json',
  'origin': 'https://eflowai-stg.epacific.net',
  'referer': 'https://eflowai-stg.epacific.net/',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
json_data = response.text
data_dict = json.loads(json_data)


text_value = data_dict.get('text', None)

print("Giá trị của key text:", text_value)

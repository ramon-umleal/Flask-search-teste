import requests

url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyBDmtae1gZhrLYIUEzkuSezg3RXHr8tYJQ&cx=017576662512468239146:omuauf_lfve&q=jogos"

payload={}
files={}
headers = {
  'Cookie': 'NID=511=knOEsEv229h9dcJiCeCO5PSBcVClGSruFnVl-Ak3ppkDAiyET0YngRAY9rNuqulLbXyHHnKVtaZcBgXA2rEjDAPIAsXuNZUgqaBf6e6hEKgVQcl2HnszEAJjw0g6--oTR5Suk0R719pigX8r8UIL71umyh3BoI_Zq6cLoBpQOus'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)
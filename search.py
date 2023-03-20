import requests
import json

class search_google():
    busca="roupas"
    url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDiRpTrkepY4JiTdED2f_Ilm8xhn1J-YEk&cx=a0d0f6a8489aa466b&q="+busca
    payload={}
    files={}
    headers = {
      'Cookie': 'NID=511=knOEsEv229h9dcJiCeCO5PSBcVClGSruFnVl-Ak3ppkDAiyET0YngRAY9rNuqulLbXyHHnKVtaZcBgXA2rEjDAPIAsXuNZUgqaBf6e6hEKgVQcl2HnszEAJjw0g6--oTR5Suk0R719pigX8r8UIL71umyh3BoI_Zq6cLoBpQOus'
    }
    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    #print(response.text)
    #print(str(response.status_code).strip(".").strip("\nF"))
    response_json=json.loads(response.text)
    print(response_json['queries']['request']['title'])
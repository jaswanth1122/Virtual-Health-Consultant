import requests
from bs4 import BeautifulSoup

def check_drug_interaction(medicine):
    url = f"https://www.drugs.com/drug_interactions.php?drug_list={medicine}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        interactions = soup.find_all("div", class_="interactions-reference")
        
        if interactions:
            return interactions[0].text.strip()
        else:
            return "No known interactions found."
    else:
        return "Error fetching data. Try again later."
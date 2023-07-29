import requests
from bs4 import BeautifulSoup

csResponse = requests.get(
    "https://api.peterportal.org/rest/v0/schedule/soc?term=2020%20Fall&department=COMPSCI"
).json()

icsResponse = requests.get(
    "https://api.peterportal.org/rest/v0/schedule/soc?term=2020%20Fall&department=I%26C%20SCI"
).json()


csCourses = csResponse["schools"][0]["departments"][0]["courses"]

icsCourses = icsResponse["schools"][0]["departments"][0]["courses"]

# Access the following like a list of dictionaries with keys:
# ['deptCode', 'courseComment', 'prerequisiteLink', 'courseNumber', 'courseTitle', 'sections']
print(csCourses[0]["prerequisiteLink"])


Response = requests.get(
    "https://www.reg.uci.edu/cob/prrqcgi?dept=COMPSCI&term=202392&action=view_all#112"
)
soup = BeautifulSoup(Response.text, "html.parser")

# Format the parsed html file
for x in soup.find_all("td"):
    print(x.string)

from requests import get
from bs4 import BeautifulSoup

# 오늘 출력하는 거까지 끝냈고 내일 페이징 기능 추가
def extract_wwr_jobs(keyword):
  base_url = "https://www.jobkorea.co.kr/Search/?stext="  
  response = get(f"{base_url}{keyword}")
  
  if not response.status_code == 200:
    print ("Can't request website")
  else:
    results = []

    soup = BeautifulSoup(response.text, "html.parser")
    
    recruit_info = soup.find_all('div', class_="recruit-info")
    for list in recruit_info:
      lists = list.find_all('li', class_="list-post")
      for l in lists:
        anchor = l.find('a')
        company = anchor['title']
        link = anchor['href']
        exp = l.find('span', class_="exp")
        edu = l.find('span', class_="edu")
        loc = l.find('span', class_="loc long")

        job_data = {
          'link' : f"https://www.jobkorea.co.kr{link}",
          'company' : company,
          'experience' : exp.string,
          'education' : edu.string,
          'location' : loc.string
        }

        results.append(job_data)

    for result in results:
      print (result)
      print ("\n//////\n")
 


extract_wwr_jobs("developer")



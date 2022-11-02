from requests import get
from bs4 import BeautifulSoup

def get_pages(keyword):
  base_url = "https://www.jobkorea.co.kr/Search/?stext="  
  response = get(f"{base_url}{keyword}")

  soup = BeautifulSoup(response.text, 'html.parser')
  pagination = soup.find('div', class_="tplPagination newVer wide")
  page = pagination.find_all('li')

  count_pages = len(page)

  if count_pages == 0:
    return 1
  elif count_pages >= 10:
    return 10
  else:
    return count_pages


def extract_job_korea(keyword):
  base_url = ("https://www.jobkorea.co.kr/Search/?stext=")
  
  if not get(base_url).status_code == 200:
    print ("Can't request website")
  else:
    results = []
    pages = get_pages(keyword)
    print (f"Found {pages} pages")

    for pg in range(pages):
      response = get(f"{base_url}{keyword}&Page_No={pg + 1}")
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

          if edu != None:

            job_data = {
              'link' : f"https://www.jobkorea.co.kr{link}",
              'company' : company,
              'experience' : exp.string,
              'education' : edu.string,
              'location' : loc.string
            }
            results.append(job_data)

    # for result in results:
    #   print (result)
    #   print ("\n//////\n")

    num_of_results = len(results)
    print (f"{num_of_results} results in total")
    return (results)

# extract_job_korea("developer")


import requests
from bs4 import BeautifulSoup

all_jobs = []

languages = ["rust", "golang", "git", "react","python", "css"]


def scrape_page():

  for language in languages:
    all_jobs = []

    lang_url = f"https://remoteok.com/remote-{language}-jobs"
    print(f"Scraping {lang_url}.....")

    response = requests.get(
        lang_url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36"
        })
    if response.status_code == 200:
      soup = BeautifulSoup(response.content, "html.parser")
      jobs = soup.find_all("td", class_="company position company_and_position")[1:]

      for job in jobs:
        title = job.find(class_="preventLink").find(itemprop="title").text.strip('\n')
        company = job.find(itemprop="hiringOrganization").find(itemprop="name").text.strip('\n')
        location = job.find(class_="location").text
        url = job.find("a")["href"]
        job_data = {
            "title": title,
            "location": location,
            "company": company,
            "url": f"https://remoteok.com/{url}"
        }
        all_jobs.append(job_data)

      #print(all_jobs)
      print(f"There are {len(all_jobs)} jobs now !! \n --------------------")
    else:
      print("Can't get jobs.")


scrape_page()

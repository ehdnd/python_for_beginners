import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(keyword):
  
  all_jobs = []
  
  lang_url = f"https://remoteok.com/remote-{keyword}-jobs"
  
  response = requests.get(
      lang_url,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36"
      })
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("td",
                         class_="company position company_and_position")[1:]
  
    for job in jobs:
      title = job.find(class_="preventLink").find(
          itemprop="title").text.strip('\n')
      company = job.find(itemprop="hiringOrganization").find(
          itemprop="name").text.strip('\n')
      location = job.find(class_="location").text
      url = job.find("a")["href"]
      job_data = {
          "title": title,
          "location": location,
          "company": company,
          "url": f"https://remoteok.com/{url}"
      }
      all_jobs.append(job_data)
  return all_jobs


def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", "w")
  file.write("Title, Location, Company, Link\n")
  
  for job in jobs:
    file.write(f"{job['title']}, {job['location']}, {job['company']}, {job['url']}\n")
  file.close()

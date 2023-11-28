import requests
from bs4 import BeautifulSoup

# The URL of the LinkedIn job postings page
url = "https://www.linkedin.com/jobs/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Identify the job posting elements based on your inspection
    job_postings = soup.find_all("div", class_="job-card-container")

    # Extract information from each job posting
    for job_posting in job_postings:
        job_title = job_posting.find("h2", class_="job-card-title").text.strip()
        company_name = job_posting.find("a", class_="job-card-company-name-link").text.strip()

        # Print the extracted information
        print(f"Job Title: {job_title}")
        print(f"Company: {company_name}")
        print("-" * 30)
else:
    print(f"Error: Unable to retrieve the webpage (Status Code: {response.status_code})")

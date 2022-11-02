from job_korea import get_pages, extract_job_korea

user_input = input("Which job are you looking for?")

get_pages(user_input)
job_korea = extract_job_korea(user_input)

# Write Access
file = open(f"{user_input}.csv", "w")

# Header
file.write("Company, Experience, Education, Location, Link\n")

for job in job_korea:
  file.write(f"{job['company']}, {job['experience']}, {job['education']}, {job['location']}, {job['link']}\n")
file.close()
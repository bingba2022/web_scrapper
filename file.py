def save_to_file(file_name, job_korea):
    # Write Access
    file = open(f"{file_name}.csv", "w")

    # Header
    file.write("Company, Experience, Education, Location, Link\n")

    for job in job_korea:
        file.write(f"{job['company']}, {job['experience']}, {job['education']}, {job['location']}, {job['link']}\n")
    file.close()
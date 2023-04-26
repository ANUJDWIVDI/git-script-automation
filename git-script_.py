#in case of any reqs : contact @ANUJDWIVDI On GitHub
#Mit License Provided 

import os
import subprocess
import json




# Your --- GitHub username ----
username = "ANUJDWIVDI"

# The path to the directory where you want to clone the repositories -- must be in the same same instancee
directory = "/path/to/remote/directory"

# Get a list of your repositories using the GitHub API Tool -- Fetches the repos 
url = f"https://api.github.com/users/{username}/repos"
output = subprocess.check_output(f"curl {url}", shell=True)
repos = [r["name"] for r in json.loads(output)]

# Clone or update each repository in the specified directory , Auto-refresh allows calling again and updating
for repo in repos:
    repo_path = os.path.join(directory, repo)
    if os.path.exists(repo_path):
        os.chdir(repo_path)
        os.system("git pull")
    else:
        os.chdir(directory)
        os.system(f"git clone https://github.com/{username}/{repo}.git")

#in case of any reqs : contact @ANUJDWIVDI On GitHub
import os
import subprocess

repo_path = "dotfiles"
repo_url = "git@github.com:pakyrs/dotfiles.git"
branch = "master"

# Resolve home directory
home_directory = os.path.expanduser("~")

# Adjust the repo_path with the home directory
repo_path = os.path.join(home_directory, repo_path)

# Go to the repository directory
os.chdir(repo_path)

# Check if there are any changes on the remote branch
try:
    subprocess.check_output(["git", "fetch", "origin", branch])
    output = subprocess.check_output(["git", "rev-list", "HEAD..origin/" + branch, "--count"])
    changes = int(output.strip())
    
    if changes > 0:
        # There are changes on the remote branch, perform a pull
        subprocess.call(["git", "pull", "origin", branch])
        # Update stow links
        command = "stow -Rv */"
        subprocess.run(command, shell=True, check=True)
    else:
        # Repository is up to date
        print("Repository is up to date. No changes to pull.")
except subprocess.CalledProcessError as e:
    # Failed to fetch or pull from the remote repository
    print("Failed to fetch or pull from the remote repository. Error:", e)


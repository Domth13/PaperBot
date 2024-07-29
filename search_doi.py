import subprocess
import shlex

def download_papers_from_doi_file(filename):
    # Construct the command
    cmd = (
        f'py -m PyPaperBot --doi-file={shlex.quote(filename)} '
        '--scholar-pages=1 --scholar-results=1 --dwn-dir="paper_doi"'
    )
    
    # Print the command for debugging purposes
    print(f"Executing command: {cmd}")
    
    try:
        # Execute the command
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing command: {cmd}")
        print(e)

if __name__ == "__main__":
    # Define the filename containing DOIs
    filename = 'doi.txt'
    download_papers_from_doi_file(filename)
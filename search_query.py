import subprocess
import shlex

def query_papers_from_queries(filename):
    with open(filename, "r", encoding="utf-8") as f:
        queries = f.readlines()

    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace including newlines
        if query:  # Only proceed if the query is not empty
            # Construct the command
            cmd = (
                f'py -m PyPaperBot --query="{shlex.quote(query)}" '
                '--scholar-pages=1 --scholar-results=1 --dwn-dir="paper_query"'
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
    # Define the filename containing queries
    filename = 'query.txt'
    query_papers_from_queries(filename)
import requests
from datetime import datetime, timedelta


def get_trending_repos(language="python", since="weekly"):
    base_url = "https://api.github.com"
    search_url = f"{base_url}/search/repositories"

    # Date for the last week
    last_week_date = datetime.now() - timedelta(days=7)
    last_week_str = last_week_date.strftime("%Y-%m-%d")

    query = f"created:>{last_week_str} language:{language}"
    params = {"q": query, "sort": "stars", "order": "desc"}

    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Failed to fetch repositories: {response.status_code}")
        return []


def print_repos(repos):
    for repo in repos:
        name = repo["name"]
        full_name = repo["full_name"]
        description = repo["description"]
        stars = repo["stargazers_count"]
        html_url = repo["html_url"]

        print(f"Name: {name}")
        print(f"Full Name: {full_name}")
        print(f"Description: {description}")
        print(f"Stars: {stars}")
        print(f"URL: {html_url}")
        print("-" * 80)


if __name__ == "__main__":
    language = "python"  # Change this to the programming language you're interested in
    trending_repos = get_trending_repos(language=language)
    print_repos(trending_repos)

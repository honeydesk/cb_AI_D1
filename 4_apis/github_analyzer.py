"""
GitHub Profile Analyzer (Simple)
================================
One API call. Parse JSON. Display results.

Concepts: requests, JSON parsing, dicts, .get(), status codes, f-strings
"""

import requests


def analyze_profile(username):
    """Fetch and display a GitHub user's profile."""

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    # Handle errors
    if response.status_code != 200:
        print(f"Error: Could not fetch user '{username}' (Status: {response.status_code})")
        return

    # Parse JSON response
    data = response.json()

    # Extract information
    name = data.get("name", "N/A")
    bio = data.get("bio", "No bio")
    location = data.get("location", "Not specified")
    public_repos = data["public_repos"]
    followers = data["followers"]
    following = data["following"]
    profile_url = data["html_url"]

    # Display results
    print(f"\n{'=' * 40}")
    print(f"  GitHub Profile: {username}")
    print(f"{'=' * 40}")
    print(f"  Name:       {name}")
    print(f"  Bio:        {bio}")
    print(f"  Location:   {location}")
    print(f"  Repos:      {public_repos}")
    print(f"  Followers:  {followers}")
    print(f"  Following:  {following}")
    print(f"  URL:        {profile_url}")
    print(f"{'=' * 40}\n")


# Main
username = input("Enter a GitHub username: ").strip()
analyze_profile(username)


'''
==============================================================================================
========


import requests

def analyze_github_user(username):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    

    if response.status_code == 200:

        user_data = response.json()

        print(f"Username: {user_data['login']}")

        print(f"Public Repositories: {user_data['public_repos']}")

        print(f"Followers: {user_data['followers']}")

        print(f"Following: {user_data['following']}")

    else:

        print(f"Error: User '{username}' not found.")

if __name__ == "__main__":

    analyze_github_user("honeydesk")  # Example GitHub username

'''
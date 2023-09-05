import requests

def get_puuid(username, api_key):
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={api_key}"
    return requests.get(url).json()["puuid"]


def get_matches(puuid, api_key, count=20):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={api_key}"
    return requests.get(url).json()

def get_match_duration(match_id, api_key):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    return requests.get(url).json()["info"]["gameDuration"]

if __name__ == "__main__":
    username = input("Enter summoner name: ")
    api_key = input ("Enter API key: ")
    puuid = get_puuid(username, api_key)
    matches = get_matches(puuid, api_key)
    total_duration = 0
    for match in matches:
        duration = get_match_duration(match, api_key)
        total_duration += duration
    print(f"Total duration: {total_duration} sec, {total_duration/60.0} min, {total_duration/3600.0} hrs")

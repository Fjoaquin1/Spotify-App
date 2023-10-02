import requests

# Token de autorización que debe haber sido creado previamente
token = 'BQDoTxaPBH8Nn3gjuNaF8-TJzX8jjSLB-FkKxNTUi8WM1wUSUZb8MJ2rR1_yKHK1GLZE27C0SFOhq66m6qi52kx0VmOhvTkcQM2NJ58PH5YtQgezKeUdZvI9Vu_lfpx0733oxgOtP-ozINqiv7qkKhyboti1C1uydd8t9eIAbr7yxmZAYNM_pQJ8Fkg53gBFn6w-nfRLaLGoO5huUeB5QlVln4j-oyBIkbmCVMPY5GufezZ8MupEmWed0AyvX4tFE7fsEg'

def fetch_web_api(endpoint, method='GET', body=None):
    headers = {
        'Authorization': f'Bearer {token}',
    }

    url = f'https://api.spotify.com/{endpoint}'

    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        headers['Content-Type'] = 'application/json'
        response = requests.post(url, headers=headers, json=body)

    return response.json()

def get_top_tracks():
    # Referencia del endpoint: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    response = fetch_web_api('v1/me/top/tracks?time_range=short_term&limit=5', 'GET')
    return response.get('items', [])

top_tracks = get_top_tracks()

for track in top_tracks:
    name = track.get('name', '')
    artists = [artist.get('name', '') for artist in track.get('artists', [])]
    print(f'{name} by {", ".join(artists)}')

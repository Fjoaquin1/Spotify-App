import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura tus credenciales de la aplicación de Spotify
client_id = 'df86d46e27044324a2e17e266fea66e8'
client_secret = '563205a6e4a042be9812c1c415d6d37b'

# Crea una instancia del cliente de autenticación de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Crea una instancia de la API de Spotify
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Reemplaza 'PLAYLIST_ID' con el ID de la playlist que deseas consultar
playlist_id = '54OxI9WILCh4LgEwEupPpf'

# Obtén la información de la playlist
playlist_info = sp.playlist_tracks(playlist_id)



for track in playlist_info['items']:
    track_name = track['track']['name']
    artistas = []
    track_artist = track['track']['artists']

    for diccionario_artista in track_artist:
        nombre_artista = diccionario_artista['name']
        artistas.append(nombre_artista)
    
    #print(artistas)
    print(track_name +' - '+ ' '.join(artistas))
    ("############################")

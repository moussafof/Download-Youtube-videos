from pytube import YouTube
from pytube import exceptions

def download_video(url, output_path='.', username=None, password=None):
    try:
        # Créer un objet YouTube avec l'URL
        youtube = YouTube(url)

        # Si la vidéo est âgée restreinte, une connexion peut être nécessaire
        if youtube.age_restricted:
            if username and password:
                # Authentification avec un compte
                youtube.login(username, password)
                
            else:
                raise exceptions.VideoPrivate()

        # Sélectionner la plus haute résolution disponible
        video = youtube.streams.get_highest_resolution()

        # Télécharger la vidéo dans le dossier spécifié
        video.download(output_path)

        print(f"Téléchargement de la vidéo '{youtube.title}' terminé avec succès.")
    except exceptions.VideoPrivate:
        print("La vidéo est privée ou soumise à des restrictions d'âge. Une connexion est nécessaire.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
video_url='https://www.youtube.com/watch?v=WNeLUngb-Xg'
download_video(video_url, output_path='C:\\Users\\hp\\Pictures\\Pellicule', username='', password='')

from flask import Flask, request
import tweepy
from ecclesiaste.config import create_api

# Configurer les clés d'API Twitter
#consumer_key = "votre_consumer_key"
#consumer_secret = "votre_consumer_secret"
#access_token = "votre_access_token"
#access_token_secret = "votre_access_token_secret"

# Authentifier l'application auprès de l'API Twitter
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

# Créer une instance de l'API Twitter
#api = tweepy.API(auth)
api = create_api()

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour tweeter un message
@app.route('/tweet', methods=['POST'])
def tweet_message():
    message = request.json['message']
    # Appeler la fonction pour tweeter le message
    tweet(message)
    return 'Message tweeted successfully'

# Fonction pour tweeter un message
def tweet(message):
    api.update_status(message)

# Écouter les mentions de votre compte
class MentionListener(tweepy.StreamListener):
    def on_status(self, status):
        # Vérifier si le tweet est une mention
        if status.in_reply_to_screen_name == 'ecclesiaste_bot':
            # Extraire le message de la mention
            message = status.text
            # Supprimer le nom d'utilisateur de la mention
            message = message.replace('@ecclesiaste_bot', '').strip()
            # Appeler la fonction pour tweeter le message
            tweet(message)

mention_listener = MentionListener()
mention_stream = tweepy.Stream(auth=api.auth, listener=mention_listener)

# Démarrer l'écoute des mentions
mention_stream.filter(track=['@ecclesiaste_bot'])  # Remplacez `votre_nom_compte_twitter` par votre nom d'utilisateur

if __name__ == '__main__':
    app.run()

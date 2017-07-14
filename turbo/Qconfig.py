APItoken = "5ce457608670408c8eaf9f77a4a8e77334769c0a901aaf388c2850bdc7e6ffc053b4dbaad084988ffc19f889f7ff3ad1ce3c22d7795404833ba13513fe7865d0"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
raise Exception("Please set up your access token. See Qconfig.py.")

from bs4 import BeautifulSoup
import requests

date = input("Enter the date and the musical year you want to go back to:")
response = requests.get("https://www.billboard.com/charts/hot-100" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

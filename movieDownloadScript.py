# Downlaod movies from console for Super lazy Lads
# (no egybest popup ads sh*t no more)
# OneEyeX 22/06/2022
# enjoy :)

import requests
from bs4 import BeautifulSoup
import webbrowser

moviesInfo = []
moviesLinks = []
movies = []

# hadnling missing search results
while True:
    # avoid empty input
    while True:
        movieName = input("Movie name >")
        if movieName != "":
            break
    # forming search link
    print('\nResults :')
    x = movieName.split()
    name = "+".join(x)
    result = requests.get("https://mycima.cloud/search/" + name)
    src = result.content
    soup = BeautifulSoup(src, "html.parser")

    # getting search results
    moviesInfo = soup.find_all("div", {"class": "Thumb--GridItem"})
    if len(moviesInfo) > 0:
        break
    print("No such a movie :( try again !")

# handling single or multiple serach results
if len(moviesInfo) > 1:
    for y in range(len(moviesInfo)):
        print(str(y)+" : " + moviesInfo[y].text)

    # handling wrong or non mumerical input
    while(1):
        choice = int(input("\nChoose movie: "))
        if choice in range(len(moviesInfo)):
            break
    chosenMovie = moviesInfo[int(choice)]

    # movie download page  multiple results
    link = chosenMovie.find("a").attrs['href']
else:
    # movie download page single result
    link = moviesInfo[0].find("a").attrs['href']

# opening movie link one
result = requests.get(link)
src = result.content
soup = BeautifulSoup(src, "html.parser")
movies = soup.find_all("a", {"class": "hoverable activable"})

# getting movies links for each movie
for movie in movies:
    if "upbam" in movie['href']:
        moviesLinks.append(movie['href'])
print('\n')
# listing movie links according to quality
for i in range(len(moviesLinks)):
    print(str(i)+" : " + str(moviesLinks[i]))
quality = input("Choose quality > ")

# opening the download popup
webbrowser.open(moviesLinks[int(quality)])

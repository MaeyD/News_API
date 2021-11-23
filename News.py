import requests
import tkinter as tk

def getNews():

    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=40f47262ec5945fdb4f47ad5288615c1"
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + "~ " + my_articles[i] + "\n"

    label.config(text = my_news)

canvas = tk.Tk()
canvas.geometry("")
canvas.title("News App")
canvas.configure(bg="#202A44")
f = ("Arial", 15, "italic")
t = ("Arial", 35,"bold italic")
button =tk.Button(canvas, font = t, text = "Reload", command = getNews, bg = "#EEE1C6")
button.pack(pady = 20)

label = tk.Label(canvas, font = f, justify = "left", bg = "#202A44", fg = "white")
label.pack(pady = 20)

getNews()

canvas.mainloop()

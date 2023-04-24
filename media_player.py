import webbrowser
def initial_stream(video_url):
    str_video_url = str(video_url)
    with open("video.html", "w") as file:
        file.write(str_video_url)

        webbrowser.open("video.html")
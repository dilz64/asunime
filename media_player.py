import webbrowser

def initial_stream(video_url, video_src):
    str_video_url = str(video_url)
    with open("video.html", "w") as file:
        file.write(f'<iframe allowfullscreen="true" height="100%" mozallowfullscreen="true" src="{video_src}" webkitallowfullscreen="true" width="100%"></iframe>')
        webbrowser.open("video.html")
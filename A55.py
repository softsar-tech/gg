mixer.init()
mixer.music.load('music.wav')
mixer.music.play()
HELPM = StringVar()
WINNER = StringVar()
HELPM.set("false")
def stop_():
    if HELPM.get() == "false":
        mixer.music.pause()
        HELPM.set("true")
    else:
        HELPM.set("false")
        mixer.music.unpause()

#!/usr/bin/python3

import dbus
from time import sleep


def get_players():
    bus = dbus.SessionBus()
    players = []
    for service in bus.list_names():
        if service.startswith("org.mpris.MediaPlayer2."):
            players.append(service.replace("org.mpris.MediaPlayer2.", ""))
    players = sorted(players)
    return players, bus



players, bus = get_players()
if len(players) < 1:
    print('Nothing play')
    exit()
for player in players:
    player_object = bus.get_object(f"org.mpris.MediaPlayer2.{player}", "/org/mpris/MediaPlayer2")
    metadata = player_object.Get(
        "org.mpris.MediaPlayer2.Player", "Metadata",
        dbus_interface="org.freedesktop.DBus.Properties"
    )
    if "xesam:artist" in metadata and "xesam:title" in metadata:
        artist, song = metadata["xesam:artist"][0], metadata["xesam:title"]
        print(f'{artist} - {song}')
        exit()
    #artist = metadata["xesam:artist"][0] if "xesam:artist" in metadata else player
    #song = metadata["xesam:title"] if "xesam:title" in metadata else player
    print(player)
    exit()

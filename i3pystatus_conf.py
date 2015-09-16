# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via dbus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
status.register("battery",
    format="{percentage:.2f}%",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

# This would look like this:
# Discharging 6h:51m
# status.register("battery",
#    format="{status} {remaining:%E%hh:%Mm}",
#    alert=True,
#    alert_percentage=5,
#    status={
#        "DIS":  "Discharging",
#        "CHR":  "Charging",
#        "FULL": "Bat full",
#    },)


# Shows disk usage of /
# Format:
# 42/128G [86G]
# status.register("disk",
#     path="/",
#     format="/ {avail}G",)


# status.register("disk",
#     path="/media/windows",
#     format="w {avail}G",)


# status.register("disk",
#    path="/media/datos",
#    format="d {avail}G",)


# Alsa
status.register("alsa",
    format="♪{volume}",
    format_muted="⍉",)

status.register("cmus",
    format="{status} {song_elapsed}/{song_length} {title} - {artist}",)


status.register("backlight",
    format="☀ {percentage}% ☀",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
#status.register("network",
#    interface="eth0",
#    format_up="{v4cidr}",)

# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw
#status.register("network",
#    interface="wlp0s29f7u4",
#    format_up="{essid} {quality:03.0f}%",)

status.register("network",
    interface="enp2s0",
    graph_style="braille-snake",
    format_up="LAN: ↑{bytes_sent}KB/s ↓{bytes_recv}KB/s",
    format_down="LAN",
    color_down = "#FFFFFF",
    color_up = "#00FF00",
    start_color = "#00FF00",
    end_color = "#0FFF00",)

 
status.register("network",
    interface="ppp0",
    unknown_up="True",
    graph_style="braille-snake",
    format_up="3G: ↑{bytes_sent}KB/s ↓{bytes_recv}KB/s",
    format_down="3G",
    color_down = "#FFFFFF",
    color_up = "#00FF00",
    start_color = "#00FF00",
    end_color = "#80FF00",)


status.register("network",
    interface="wlp0s29f7u4",
    graph_style="braille-snake",
    format_up="WIFI: {essid} {quality:3.0f}% ↑{bytes_sent}KB/s ↓{bytes_recv}KB/s",
    format_down="WIFI",
    color_down = "#FFFFFF",
    color_up = "#00FF00",
    start_color = "#00FF00",
    end_color = "#80FF00",)

status.run()


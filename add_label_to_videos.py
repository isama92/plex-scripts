from plexapi.server import PlexServer
from pathlib import Path
import re
from config import *

plex = PlexServer(PLEX_URL, PLEX_TOKEN)
library = plex.library.section(LIBRARY)

def channel_to_label(str):
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', str)
    return ''.join(word[0].upper() + word[1:] for word in cleaned.split() if word)

for video in library.all():
    if video.media and video.media[0].parts:
        path = video.media[0].parts[0].file
        parts = Path(path).parts
        if path.startswith('/videos/Pinchflat'):
            label = channel_to_label(parts[3])
            video.addLabel(label)
        elif path.startswith('/videos/MeTube/Video'):
            label = channel_to_label(parts[4])
            video.addLabel(label)
        elif path.startswith('videos/MeTube/Audio'):
            label = channel_to_label(parts[4])
            video.addLabel(label)
            video.addLabel('AudioOnly')
        else:
            video.addLabel('NoLabel')


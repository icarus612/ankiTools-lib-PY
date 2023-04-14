import requests
import json
import os

all_lst = [el for el in os.listdir('/home/icarus-64/.local/share/Anki2/User 1/collection.media') if 'ic_nrkt_' in el]
update_lst = [el for el in all_lst if '.mp3' not in el]

print(all_lst)
print(update_lst)

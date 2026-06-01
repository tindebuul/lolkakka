import webbrowser

def open_analytics(champ, rank, patch):

    webbrowser.open(f"https://lolalytics.com/lol/{champ}/build/?tier={rank}&patch={patch}")
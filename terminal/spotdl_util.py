import os


def getProcessType():
    print(
        "Please Choose Process Type From List Below"
        "\nDownload Song - [1]"
        "\nDownload Playlist - [2]"
        "\nDownload Album - [3]"
        "\nDownload Your Favourite Songs - [4]"
        "\nDownload All Songs From an Artist - [5]"
        "\nResume Failed/Incomplete Download - [6]"
    )
    print("Selection : ")
    processType = input()
    return processType


def getPath():
    print("Please Enter Download Location : ")
    downloadLocation = input()
    return downloadLocation


def getFormat():
    print(
        "Please Select Output Format : "
        "\n.mp3 [1]"
        "\n.m4a [2]"
        "\n.flac [3]"
        "\n.opus [4]"
        "\n.ogg [5]"
    )
    outputFormat = input()

    if outputFormat == '1':
        outputFormat = 'mp3'
    elif outputFormat == '2':
        outputFormat = 'm4a'
    elif outputFormat == '3':
        outputFormat = 'flac'
    elif outputFormat == '4':
        outputFormat = 'opus'
    elif outputFormat == '5':
        outputFormat = 'ogg'

    return outputFormat

def downloadSong():
    print("Please Enter Track Name and Artist For Download : ")
    songName = input()
    outputFormat = getFormat()
    downloadLocation = getPath()
    os.system('python -m spotdl download ' + songName + ' --output ' + '\"' + downloadLocation + '\"' + ' --format ' + outputFormat + ' --preload ')
    # os.system('python -m spotdl ' + "'" + songName + "'" + ' --output ' + '\"' + downloadLocation + '\"' + ' --output-format ' + outputFormat)


def downloadPlaylist():
    print("Please Enter Spotify PlayList Link For Download : ")
    playlistLink = input()
    outputFormat = getFormat()
    downloadLocation = getPath()
    os.system('python -m spotdl download ' + playlistLink + ' --output ' + '\"' + downloadLocation + '\"' + ' --format ' + outputFormat + ' --preload ')


def downloadAlbum():
    print("Please Enter Spotify Album Link For Download : ")
    albumLink = input()
    outputFormat = getFormat()
    downloadLocation = getPath()
    os.system('python -m spotdl download ' + albumLink + ' --output ' + '\"' + downloadLocation + '\"' + ' --format ' + outputFormat + ' --preload ')


def downloadFav():
    outputFormat = getFormat()
    downloadLocation = getPath()
    # os.system('python -m spotdl download ' + albumLink + ' --output ' + '\"' + downloadLocation + '\"' + ' --format ' + outputFormat + ' --preload ')
    # os.system('python -m spotdl ' + '--user-auth saved' + ' --output ' + '\"' + downloadLocation + '\"' + ' --output-format ' + outputFormat + ' --dt ' + downloadThread + ' --st ' + searchThread)


def downloadArtistSongs():
    print("Please Enter Spotify Artist Link For Download : ")
    artistLink = input()
    outputFormat = getFormat()
    downloadLocation = getPath()
    os.system('python -m spotdl download ' + artistLink + ' --output ' + '\"' + downloadLocation + '\"' + ' --format ' + outputFormat + ' --preload ')


def resumeDownload():
    print("Please Enter .spotdlTrackingFiles Path to Resume : ")
    restorePath = input()
    # os.system('python -m spotdl ' + restorePath)
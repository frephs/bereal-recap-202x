# BeReal Recap 202x
<img src="bereal-cover/cover.png" height="300px">

## Description

Python script to generate a music-driven timelapse from your collection of BeReal photos.
The script functions by quantizing your chosen music across three levels to put together a sequence of the photos that carousels at varying speeds in accordance with the audio's level and the duration of the music. Keep in mind that the MP3 file you select will be played from start to finish, influencing the overall length of the generated video.

## Requirements
The requirements to run this script are listed in the `requirements.txt` file. You can install them with the following command:

```bash
pip install -r requirements.txt
```

## Usage
At the time of development, the latest version of python on which the script works is 3.11 because of compatibility issues of the `librosa` module.

### 1. Generate bereal cover
In the `bereal-cover` folder you can find the bereal-lookalike template which is added as intro and outro of your recap
To generate your bereal cover run this line and enter your username. 
`python generate-cover.py`

### 2. How to export the photos
Go to [toofake.lol](https://toofake.lol/) and log in with your account. then export all of your photos in the default format (back and front camera).
Unpack the zip file and move the photos into the `bereal-export` folder.

### 3. Photo order
The berel-export folder is not going to be ordered chronologically and the modification date of the photos is not going to be the creation one but the export one.  
In order for the recap be chronological you can run the python script `fix-datetimes.py` using the following command:
```bash
cd bereal-export/
python ../fix-datetimes.py
```

### 4. Generate your timelapse
Finally:
```bash
python generate-bereal-recap.py
```

### Reccomendations
I recommend using a song with a crescendo in the middle, so that the video is more interesting and to choose a song lenght so that there is a ratio of no more than 360 photos per minute of music approximately.

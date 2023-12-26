# BeReal Recap 202x
## Description

Python script to generate a music-driven timelapse from your collection of BeReal photos.
The script functions by quantizing your chosen music across three levels to put together a sequence of the photos that carousels at varying speeds in accordance with the audio's level and the duration of the music. Keep in mind that the MP3 file you select will be played from start to finish, influencing the overall length of the generated video.

## Requirements
The requirements to run this script are listed in the `requirements.txt` file. You can install them with the following command:

```bash
pip install -r requirements.txt
```

## bereal-cover
- In the bereal-cover folder you can find the bereal-lookalike template I designed with gimp for the cover of the video. You can edit it with your own username and year of choice and export it as a `png file`.
- The installation of the font [Inter](https://fonts.google.com/specimen/Inter?preview.text=BeReal) is recommended to resemble the app's presentation. 

## Usage
At the time of development, the latest version of python on which the script works is 3.11 because of compatibility issues of the `librosa` module.

### Reccomendations
I recommend using a song with a crescendo in the middle, so that the video is more interesting and a ratio of no more than 360 photos per minute of music approximately.

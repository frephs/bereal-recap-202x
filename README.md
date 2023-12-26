# BeReal Recap 202x
<img src="bereal-cover/cover.png" height="300px">

## Description
[Disclaimer here](#disclaimer)

Python script to generate a music-driven timelapse from your collection of BeReal photos.
The script functions by quantizing your chosen music across three levels to put together a sequence of the photos that carousels at varying speeds in accordance with the audio's level and the duration of the music. Keep in mind that the MP3 file you select will be played from start to finish, influencing the overall length of the generated video.

## Requirements
The requirements to run this script are listed in the `requirements.txt` file. You can install them with the following command:

```bash
pip install -r requirements.txt
```

## bereal-cover
- In the bereal-cover folder you can find the bereal-lookalike template I designed with gimp for the intro and outro of the video. You can edit it with your own username and year of choice and export it as a `png file`.
- The installation of the font [Inter](https://fonts.google.com/specimen/Inter?preview.text=BeReal) is recommended to resemble the app's presentation. 

## Usage
At the time of development, the latest version of python on which the script works is 3.11 because of compatibility issues of the `librosa` module.

### How to export the photos
Go to [toofake.lol](https://toofake.lol/) and log in with your account. then export all of your photos in the default format (back and front camera).
Unpack the zip file and move the photos into the `bereal-export` folder.

**Edit**: just learnt toofake.lol doesn't download extra bereals but it could be awesome if it did so go there and contribute. [toofake repo](https://github.com/s-alad/toofake)

### Photo order
The berel-export folder is not ordered chronologically and the modification date of the photos is not the creation one but the export one.  
If you want the recap to be chronological you can run the python script `fix-datetimes.py` using the following command:

```bash
cd bereal-export/
python ../fix-datetimes.py
```


### Reccomendations
I recommend using a song with a crescendo in the middle, so that the video is more interesting and to choose a song lenght so that there is a ratio of no more than 360 photos per minute of music approximately.

## Contribute
Feel free to contribute. here's a list of features that would be cool to implement
- [ ] Connection to BeReal exposed api 
- [ ] Contribute to toofake for the download of extra bereals
- [ ] Script to edit the cover template automatically 
- [ ] Integrated web-app solution

## <a id='disclaimer' name="disclaimer">Disclaimer </a>
This repository does not contain any BeReal intellectual property nor it violates the terms of service as 

1. The BeReal name is used following the company guidelines on brand identity usage

2. the software in this repository provides through a script a service the company does not provide anymore, locally and without charge.

All the graphics available in the repo are made with FOSS software and fonts available on the internet under the OFL (open font license). 

It does however contain links to third party software which may not be following the company guidelines: those links can and will be removed if the company or the 3rd party software developer submit a request [here](mailto:ffrancescogenovese+bereal@gmail.com).

Features under todo in contributing are not yet implemented and are not to be taken as future milestones of this repository as this as of now remains a psrsonal project to create a timelapse.
I hereby do not take responsibility for any forks of this project which may implement those features as this software is meant to be freely distributed.

## Support me

<a href="https://paypal.me/frncscgnvs/"><img src="https://raw.githubusercontent.com/andreostrovsky/donate-with-paypal/925c5a9e397363c6f7a477973fdeed485df5fdd9/blue.svg" height="40"></a>  
If you enjoyed this project — or just feeling generous, consider buying me a beer. Cheers

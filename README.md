
<img src="assets/header_background.jpg" height ="38%" width="38%"></img> 

# Kuzgunlar Model Web Interface

![Python 3](https://img.shields.io/badge/Python-3-yellow.svg)
![Dash Plotly](https://img.shields.io/badge/Dash-1.14-turquoise.svg)
![GPL 3.0](https://img.shields.io/badge/license-GPLv3-red.svg)

This repo has been prepared so that the Kuzgunlar Turkish NLP models can be easily used by the end users.

## :exclamation: Requirements

 * Python3.4 or higher version.
 * [The Python Package Installer (pip)](https://pip.pypa.io/en/stable/installing/).

## ⚙ Kurulum

 * Clone or download this repo
 * Then use the following command to install the packages named in the requirements.txt file.
 ```bash 
  python3 -m pip install -r requirements.txt
```

 :exclamation: IMPORTANT  - Each model is ~ 450mb in size and will be downloaded automatically during initial startup. Therefore, the first run may take a long time.

 * Installation process:

![animated](assets/kurulum.gif)

## :video_game: Usage of the Web Interface

The web interface provides a very easy to use environment for the end users to test and use the models.

 * To run the interface, all you have to do is running this command.
 ```bash 
  python3 dash_app.py
```
 * Then you can use the Q&A and NER models by going to http://127.0.0.1:8050 with your browser.
 * The Kuzgunlar web interface allows you to try all other models available at https://huggingface.co/models.

 * Usage:

![animated](assets/web_arayuz.gif)

## :video_game: Usage of the Web API

The web API is useful when you need to work fast with big data.

 * To run the interface, all you have to do is running this command.
 ```bash 
  python3 api.py
```
 * Next, you need to post a POST request to the URL of the model you want to use.
 * If you use curl to request REST:
 
For NER Model:
  ```bash 
   curl http://127.0.0.1:5000/ner -H 'Content-Type: application/json' -d '{"context": "Samsun, büyükşehir statüsündeki otuz ilden biridir."}'
```

For the Question-Answer Model:
  ```bash 
   curl http://127.0.0.1:5000/qa -H 'Content-Type: application/json' -d '{"context": "Mehteran birliği 1365 yılında kuruldu.", "question": "Mehteran ne zaman kuruldu?"}'
```

For Sentiment Analysis Model:
  ```bash 
   curl http://127.0.0.1:5000/sentiment -H 'Content-Type: application/json' -d '{"context": "Bu ürün çok başarılı."}'
```

 * Usage:

![animated](assets/web_api.gif)

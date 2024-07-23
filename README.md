# DocLayoutAnalysis

## Introduction

This repo aims to analyse the layout of document. At the moment, the project is built upon the `layoutparser` toolkit, which is a very powerful deep learning-based extracting approach. 

## Features

+ Easy-to-use via already-set-up pipeline. 

## Usage

1. Install the repo

```
git clone https://github.com/What-s-behind/DocLayoutAnalysis.git
cd DocLayoutAnalysis
pip -r install requirements.txt
```

2. Running the app: in the `app.py`, there is a variable that holds the file directory, place your file in that position and run the file. 

```
python app.py
```

_Note:_ I leave an example of running `layoutparser` in the `/notebooks`, you can visit it to learn running the `layoutparser`

## Future development

+ Add more OCR tools (`easyocr`, `paddleocr`, etc.) for the diversity. 
+ Add more layout models.
+ Introduce OCR-free framework to the repo.

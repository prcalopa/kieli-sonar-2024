# KIELI

**In this project we are creating a newborn language from the mixture of ancient local languages** such as Seto, Burgenland Croatian, Aranese, Cornish and Aromanian.
We use Chat-GPT to combine words from a pair of languages and create a new original language.
Using ElevenLabs we later on synthesize from text-to-speech to bring the new language to life!

_Part of the KIELI project presented in Sonar 2024 (Barcelona)_

## Dataset generation

The dataset is already generated in `/assets/combined-words` as a set of csv files. To generate a new Dataset just follow the intructions. (The prompt include the languages to guide the LLM, if you use different languages please adapt the prompt)

### Prompting

Using Chat-GPT 4

#### Prompt

This file contains a set of words translated to different languages (English, Seto, Burgenland Croatian, Aranese, Cornish and Aromanian). Your mission is to create a set of csv files.
Each csv file will contain the following structure: Column and row titles display one of the words in all of the languages. For each cell you will invent a new word by combining the cell column and row titles into a new word that could sound good to the ear.
Create a csv file for each word.
{attach csv file. find an example in `assets/words-translated.csv`}

#### Result

Ask Chat-GPT to export the csv files as a zip file

## Development

### Requirements

This repo uses ElevenLabs API. Please create an account to get an API Key.
Create a `.env` file and copy your API Key

```
ELEVEN_LABS_KEY=***********
```

#### Install pyenv

https://github.com/pyenv/pyenv

The python verison used in this repo is specified in `.python-version`

#### Install dependencies

_Activate venv before installing requirements._
`source venv/bin/activate`

```zsh
pip install requirements.txt
```

## Run

_Activate venv before running the script._
`source venv/bin/activate`

```zsh
python generate_speech.py
```

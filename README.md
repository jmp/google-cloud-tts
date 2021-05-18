# Text to Speech using Google Cloud

Quickly generate speech from text using Google Cloud Text-to-Speech API.

## Requirements

* Python 3.9
* Google Cloud TTS API is enabled
* Set up finished according to [the docs](https://cloud.google.com/text-to-speech/docs/libraries)

## Installation

    GRPC_PYTHON_BUILD_SYSTEM_ZLIB=true pip install -r requirements.txt

## Usage

    python generate-speech.py --language en "This is a test."

The audio file is generated in a directory called `output` in the current
working directory.
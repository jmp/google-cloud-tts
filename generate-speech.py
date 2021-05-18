#!/usr/bin/env python3

from argparse import ArgumentParser
from os import path, makedirs
from pathlib import Path
from re import sub

from google.cloud import texttospeech


OUT_DIR = Path(__file__).resolve().parent / "output"


def parse_args():
    parser = ArgumentParser(description="Convert text to speech using Google Cloud")
    parser.add_argument("--language", metavar="CODE", type=str, default="en", help="a language code")
    parser.add_argument("text", type=str, help="the text to speak")
    return parser.parse_args()


def text_to_filename(text, suffix=".mp3") -> str:
    return sub(r"[-.,?!-/ ]", "", text.lower()) + suffix


def synthesize_speech(text: str, language_code: str) -> bytes:
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput({"text": text})
    voice = texttospeech.VoiceSelectionParams({
        "language_code": language_code,
        "ssml_gender": texttospeech.SsmlVoiceGender.NEUTRAL,
    })
    audio_config = texttospeech.AudioConfig({
        "audio_encoding": texttospeech.AudioEncoding.MP3,
    })
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )
    return response.audio_content


if __name__ == "__main__":
    args = parse_args()
    out_file = OUT_DIR / text_to_filename(args.text)
    audio_content = synthesize_speech(args.text, args.language)
    if not path.exists(OUT_DIR):
        makedirs(OUT_DIR)
    with open(out_file, "wb") as out:
        out.write(audio_content)
        print(f"Audio written to '{out_file}'")

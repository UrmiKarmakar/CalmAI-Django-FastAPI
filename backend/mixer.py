import os
import logging
from pydub import AudioSegment

def mix_background(voice_path: str, bg_name: str) -> str:
    # Resolve absolute path to background file
    project_root = os.path.dirname(os.path.dirname(__file__))
    bg_path = os.path.join(project_root, "static", "backgrounds", f"{bg_name}.mp3")

    if not os.path.exists(bg_path):
        raise FileNotFoundError(f"Background file not found: {os.path.abspath(bg_path)}")

    logging.info(f"Mixing voice: {voice_path} with background: {bg_path}")

    # Load and adjust volumes
    voice = AudioSegment.from_file(voice_path).apply_gain(+3)
    background = AudioSegment.from_file(bg_path).apply_gain(-10)

    # Loop background to match voice duration
    if len(background) < len(voice):
        loops = (len(voice) // len(background)) + 1
        background = background * loops

    # Trim and overlay
    mixed = background[:len(voice)].overlay(voice)

    # Save final mixed audio
    final_path = voice_path.replace("voice_", "final_")
    if final_path == voice_path:
        final_path = voice_path.replace(".mp3", "_final.mp3")

    mixed.export(final_path, format="mp3", bitrate="192k")
    logging.info(f"Final mixed audio saved to: {final_path}")

    return final_path
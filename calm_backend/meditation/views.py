import os, sys, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Add CalmAI/backend to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../../backend"))

from script_generator import generate_script
from tts_engine import synthesize_voice
from mixer import mix_background  # Include background mixing

@csrf_exempt
def generate_session(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            mood = data.get("mood", "")
            voice = data.get("voice", "female")
            background = data.get("background", "")
            answers = data.get("answers", "")

            # Generate meditation script
            tokens = generate_script(mood, answers)

            # Synthesize voice from script
            voice_path = synthesize_voice(tokens, voice)

            # Mix background audio
            final_path = mix_background(voice_path, background)

            # Return final mixed session
            return JsonResponse({
                "file": final_path,
                "script": tokens
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

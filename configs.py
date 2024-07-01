MODEL = "gpt-4o"
MAX_FRAMES = 15
SEED = 123
WSS_TUNNEL_URL = "wss://[domain]"
VISION_PROMPT = """
You are Video Narrator. 
You will be provided with a set of frames from the live video feed, you job is to describe the activity happening in the video feed with details.
Your response must be in the json format {"activity_description" : ["<here comes the description of the activity happening in the video feed frame by frame>"], "objects" : [{"name" : "here comes the name of the object", "count" : "here comes the count of the object"}]}.
"""
VISION_USER_CONTENT = """
Narrate the frames of the video.
"""
LLM_KEY = "[openai-key]"
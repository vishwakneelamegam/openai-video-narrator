# Description
- The code is used to narrate live video stream from the webpage using openai vision.

# Note
- Provide your openai key and domain in the configs.py file
- To update the prompt go to configs.py and update vision_prompt
- To increase the frame size got to configs.py and update max_frames
- To run the server, use the command uvicorn server:app --port 3000
- I have used ngrok to run the code
- To run the ngrok tunnel, use the command ngrok http 3000 --domain here-comes-the-ngrok-domain
- vision.html file is used to stream the live video stream from the client to the server.  Narration will be shown for every 15 frames in the vision.html page itself.
- Paste the ngrok domain in the configs.py
- For a second 1 frame is sent.

# Requirement
- fastapi
- openai

# Future idea
- To implement google gemini vision video feature.
- To handle audio and noises.

# References
- https://github.com/cbh123/narrator
- https://youtu.be/wOEz5xRLaRA?si=yv0d1UBoTB9-hYSz
- https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding

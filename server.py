from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from configs import *
from llm import *
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = FastAPI()

@app.get("/")
async def webpage():
    with open("vision.html", "r") as file:
        html_content = file.read()
        html_content = html_content.replace("[paste_tunnel_url_here]", WSS_TUNNEL_URL)
    return HTMLResponse(content=html_content)

@app.websocket("/vision/")
async def visionEndpoint(websocket: WebSocket):
    llm_obj = llm()
    await websocket.accept()
    try:
        images = []
        count = 0
        while True:
            if count == MAX_FRAMES:
                llm_response = await llm_obj.generate_with_image(VISION_PROMPT, VISION_USER_CONTENT, images)
                if "activity_description" in llm_response:
                    await websocket.send_text("\n".join(llm_response["activity_description"]))
                count = 0
                images = []
            else:
                image_bytes_data = await websocket.receive_text()
                images.append(image_bytes_data)
            count += 1
    except Exception as e:
        logging.info("Vision Web socket [Stopped] - from server")
from openai import AsyncOpenAI
from configs import *
import json

class llm():
    def __init__(self) -> None:
        self.llm_client = AsyncOpenAI(api_key=LLM_KEY)
    async def generate_with_image(self, system_content, user_content, images):
        try:
            messages = [{"role" : "system", "content" : system_content}]
            all_images = [{"type" : "image_url", "image_url" : {"url" : f"data:image/jpeg;base64,{image}"}} for image in images]
            messages.append({
                "role" : "user",
                "content" : [
                    {
                        "type" : "text",
                        "text" : user_content
                    },
                ] + all_images
            })
            llm_response = await self.llm_client.chat.completions.create(messages=messages, model=MODEL,response_format={"type" : "json_object"}, seed=SEED)
            assistant_response = llm_response.choices[0].message.content
            return json.loads(assistant_response)
        except Exception as e:
            raise e

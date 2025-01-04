from fastapi import FastAPI
from io import BytesIO
from image import generate_image
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


class Item(BaseModel):
    users: int
    end: str
    wins: int
    title: str
app = FastAPI()


@app.get("/generate")
def generate(users: int, end: str, wins: int, title: str):
    image = generate_image(
        users=users,
        end=end,
        wins=wins,
        title=title,
    )
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/jpeg")

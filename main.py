from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from database import get_connection

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", description="mqtt messages")
def read_root(request: Request):
  client, database, collection = get_connection()
  docs = collection.find({"end_device_ids.device_id":"bridge-chaumont"})

  # Transformer en liste de dicts simples
  mesures = [ ]
  for doc in docs:
    mesures.append( {
      "date": doc.get( "received_at" ),
      "device": doc.get( "end_device_ids", { } ).get( "device_id" ),
      "haut": doc.get( "uplink_message", { } ).get( "decoded_payload",
                                                    { } ).get( "haut" )
    } )

  return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={ "mesures": mesures }
  )

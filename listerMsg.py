from database import get_connection

client, database, collection = get_connection()

docs = collection.find({"end_device_ids.device_id":"bridge-chaumont"})
for doc in docs:
  print(doc.get("received_at"), doc.get('end_device_ids').get('device_id'), doc.get('uplink_message').get('decoded_payload').get('haut'))
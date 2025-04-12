from azure.cosmos import CosmosClient
from config import COSMOS_URI, COSMOS_KEY, COSMOS_DB_NAME, COSMOS_CONTAINER_NAME

client = CosmosClient(COSMOS_URI, COSMOS_KEY)
db = client.create_database_if_not_exists(id=COSMOS_DB_NAME)
container = db.create_container_if_not_exists(
    id=COSMOS_CONTAINER_NAME,
    partition_key="/userId"
)

def save_feedback(userId, message, sentiment, rating):
    feedback = {
        "id": f"{userId}-{message[:10]}",
        "userId": userId,
        "message": message,
        "sentiment": sentiment,
        "rating": rating
    }
    container.upsert_item(feedback)

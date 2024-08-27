from config.db import db
from bson import ObjectId
from utils.encoders import serializeDict, serializeList


def find_all(collection):
    print("find_all function called")
    return serializeList(db.local[collection].find())


def find_one(collection, id):
    print("find_one function called")
    return serializeDict(db.local[collection].find_one({"_id": ObjectId(id)}))


def create(collection, entity):
    print("create function called")
    print(f"Collection: {collection}")
    print(f"Entity to Insert: {entity}")
    entity_dict = entity.dict() if hasattr(entity, 'dict') else dict(entity)
    db.local[collection].insert_one(entity_dict)
    return serializeList(db.local[collection].find())


def update(collection, id, entity):
    print("update function called")
    entity_dict = entity.dict() if hasattr(entity, 'dict') else dict(entity)
    db.local[collection].find_one_and_update({"_id": ObjectId(id)}, {"$set": entity_dict})
    return serializeDict(db.local[collection].find_one({"_id": ObjectId(id)}))


def soft_delete(collection, id):
    print("soft_delete function called")
    db.local[collection].find_one_and_update({"_id": ObjectId(id)}, {"$set": {"deleted": True}})
    return serializeDict(db.local[collection].find_one({"_id": ObjectId(id)}))


def hard_delete(collection, id):
    print("hard_delete function called")
    return serializeDict(db.local[collection].find_one_and_delete({"_id": ObjectId(id)}))

def calculate_average_rating(product_id: str, supplier_id: str):
    try:
        # Query MongoDB to find reviews for the specified product and supplier
        reviews = list(db.local.reviews.find({"product_id": product_id, "supplier_id": supplier_id}))

        # Check if any reviews were found
        if not reviews:
            return None

        # Calculate the average rating
        total_rating = sum(review["overall_rating"] for review in reviews)
        average_rating = total_rating / len(reviews)

        return average_rating
    except Exception as e:
        # Handle any exceptions or errors here
        print(f"Error calculating average rating: {e}")
        return None

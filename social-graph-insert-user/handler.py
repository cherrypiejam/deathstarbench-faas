import json
import pymongo

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
        JSON string with the field of `user_id`
    """

    payload = json.loads(req)
    if 'user_id' not in payload:
        return ('Error: missing field `user_id`')

    client = pymongo.mongo_client.MongoClient('mongodb://mongo-0.mongo.default')
    db = client.social_graph
    collection = db.social_graph

    new_doc = {'user_id':payload['user_id'],
               'followers':[],
               'followees':[]
              }

    res = collection.insert_one(new_doc)

# from utils.db_functions import initialize_db
# from utils.main_menu import run_main_menu


# DB_FILE = "./db/caffe.sql"


# if __name__ == "__main__":
#     initialize_db(DB_FILE)
#     run_main_menu()


import json


def handler(event, context):
    # TODO implementation
    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Second version",
                            "event": event})
    }

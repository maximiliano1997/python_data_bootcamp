import json
import logging
from .helper_sql import insert_member


def get_selfdev_members(psql_conn):
    # Reads the members from data/selfdev_members and inserts them into the database....
    with open('data/selfdev_members.json') as json_file:
        data = json.load(json_file)
        for member in data['selfdev_members']:
            # print(member['name'])
            logging.info(f"Processing member: {member['name']}")
            insert_member(psql_conn, member)

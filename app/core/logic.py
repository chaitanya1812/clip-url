# app/core/logic.py

import hashlib
import secrets
import os
from app.core.db import execute_query

BASE_URL = "localhost:8500"
base_env = os.getenv("BASE_URL")
if base_env and base_env != "":
    print("found base url : ", base_env)
    BASE_URL = base_env


# BASE_URL = "https://clip.url"  # Update to actual Render domain when deployed

def _generate_short_path(length=8):
    short_path = secrets.token_urlsafe(length)[:length]
    hash = _hash_short_path(short_path)
    res = resolve_shortened_url(hash)
    if res == None: return short_path
    return _generate_short_path()


# def _hash_short_path(short_path):
#     return hashlib.sha256(short_path.encode()).hexdigest()

def _hash_short_path(short_path):
    return hashlib.sha1(short_path.encode()).hexdigest()

def _get_full_short_path(short_path): return f"{BASE_URL}/go/{short_path}"

def create_shortened_url(original_url: str):
    short_path = _generate_short_path()
    shortened_url = _get_full_short_path(short_path)
    hash_value = _hash_short_path(short_path)

    query = """
        INSERT INTO urls (shortened_url, hash, original_url)
        VALUES (%s, %s, %s)
        RETURNING shortened_url, hash;
    """
    try:

        result = execute_query(query, (shortened_url, hash_value, original_url), fetch_one=True)
        return result  # returns dict: { 'shortened_url': ..., 'hash': ... }
    except Exception as e:
        print("unable to insert the row for : ", original_url, " : ", e)

def resolve_shortened_url(hash_value: str):
    query = "SELECT original_url FROM urls WHERE hash = %s"
    result = execute_query(query, (hash_value,), fetch_one=True)
    if result:
        print("found the entry for hash : ", hash_value)
        return result["original_url"]
    return None


def get_all_url_entries():
    query = "SELECT * FROM urls"
    result = execute_query(query, fetch_all=True)
    print("get all url entries : ", result)
    if result != None:
        return result
    return None

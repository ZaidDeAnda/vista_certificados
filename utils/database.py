import pymongo
import urllib
import streamlit as st

@st.cache_resource()
def get_mongo_client(_config):
    """Get the mongo client and store it in cache.

        Params
        ------
        config : Config
            Configuration object containing email details.
        
        Returns
        -------
        client
            The mongo client connected to the database.
        """
    db_mongo = _config.get_config()['db_mongo']
    user = db_mongo["user"]
    password = urllib.parse.quote_plus(db_mongo["password"])
    cluster = db_mongo["cluster"]
    client = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority"
    )
    return client

def get_mongo_client_debug(config):
    """Get the mongo client and store it in cache.

        Params
        ------
        config : Config
            Configuration object containing email details.
        
        Returns
        -------
        client
            The mongo client connected to the database.
        """
    db_mongo = config.get_config()['db_mongo']
    user = db_mongo["user"]
    password = urllib.parse.quote_plus(db_mongo["password"])
    cluster = db_mongo["cluster"]
    client = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority"
    )
    return client

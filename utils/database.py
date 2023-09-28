import pandas as pd
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

def create_dataframe_from_cursor(cursor):
    """Transform the cursor from mongo into a dataframe

        Params
        ------
        cursor : cursor
            Cursor pointing to a mongo collection.
        
        Returns
        -------
        df
            The dataframe made from the mongo cursor.
        """
    df = None
    for document in cursor:
        if df is not None:
            df = df.append(document, ignore_index=True)
        else:
            df = pd.DataFrame(document, index=[0])
    df.drop("_id", axis=1, inplace=True)
    return df

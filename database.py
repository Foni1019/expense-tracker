import os
from deta import Deta
import streamlit as st

from dotenv import load_dotenv

load_dotenv(".env")

DETA_KEY = os.getenv("DETA_KEY")

deta = Deta(DETA_KEY)

db = deta.Base("test")

def insert_transaction(category, dateOfTransaction, amount, comment):
        return db.put({"category": category, "dateOfTransaction": dateOfTransaction, "amount": amount, "comment": comment})

def fetch_all():
        res = db.fetch()
        return res.items

def fetch_period(period):
        res = db.fetch({"dateOfTransaction?r": [str(period[0]), str(period[1])]})
        return res



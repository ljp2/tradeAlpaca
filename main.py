import os
import pandas as pd
import datetime
from time import sleep
import threading

from alpaca_trade_api.rest import REST, TimeFrame

os.environ['APCA_API_KEY_ID'] = 'PKT9KWSZSITIDYGDS2XQ'
os.environ['APCA_API_SECRET_KEY'] = 'KG7Jclj4JdD0cOkzLnFvmdjBAq9FRCmqE6fMX0l6'
os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'

from alpaca_trade_api.stream import Stream

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(<ALPACA_API_KEY>,
                <ALPACA_SECRET_KEY>,
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')  # <- replace to SIP if you have PRO subscription

# subscribing to event
stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')

stream.run()
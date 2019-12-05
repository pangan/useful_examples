from mixpanel import Mixpanel
from mixpanel_async import AsyncBufferedConsumer
import asyncio
import time

import logging

from functools import wraps, partial



# tracks an event with certain properties

_LOG = logging.getLogger(

)
async def my_track():
    mp.track('distinct_id', 'ev name', {'color' : 'black', 'size': 'small'})
    print("Done!")

    # sends an update to a user profile
    #mp.people_set(USER_ID, {'$first_name' : 'Amy', 'favorite color': 'red'})


def fail_silently(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            _LOG.exception(f"MixpanelException: {str(e)} caught, failing silently")

    return wrapper


def background(f):

    @wraps(f)
    def wrapped(*args, **kwargs):
        loop = asyncio.get_event_loop()
        if callable(f):
            try:
                return loop.run_in_executor(None, partial(f, *args, **kwargs))
            except Exception as e:
                print(e)
        else:
            raise TypeError('Task must be a callable')

    return wrapped


class AmirClass:
    PROJECT_TOKEN = "b50e13145d9f44153801d2772580ced9"
    USER_ID = "pangan@gmail.com"

    def __init__(self):
        self.mp = Mixpanel(self.PROJECT_TOKEN, consumer=AsyncBufferedConsumer())

    @fail_silently
    @background
    def my_track_2(self, var_1, var2, amir=""):

        self.mp.track('distinct_id', 'ev name', {'color': 'noon', 'size': 'small'})
        time.sleep(1)
        # raise Exception("Bad!")

        print("Done my track2!")




def main():
    mm = AmirClass()
    mm.my_track_2(var_1=3, var2=4, amir="hello")


if __name__ == "__main__":
    main()
    print("Hello")
    print("Good!")

import random
import time

def sleep(n_secs):
    time.sleep(n_secs)


def get_user_agent():
    user_agent = ["Mozilla/5.0 Autumn", "Mozilla/5.0 Winter", "Mozilla/5.0 Spring", "Mozilla/5.0 Summer"]
    return random.choice(user_agent)

if __name__ == '__main__':
    print(get_user_agent())


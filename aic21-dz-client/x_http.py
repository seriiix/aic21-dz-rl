import requests
import numpy as np
import json


class Http:
    def __init__(self, address="http://127.0.0.1:1616/"):
        self.address = address

    def get_epsilon(self):
        try:
            res = requests.get(url=self.address)
            res = json.loads(res.content.decode())
            epsilon = res['epsilon']
            return epsilon
        except:
            return 0.5

    def send(self, state, action, reward, state_, done, ant_turn_number):
        state = state.reshape(11, 35, 35)
        state_ = state_.reshape(11, 35, 35)

        data = {
            "state":  state.tolist(),
            "action": action,
            "reward": reward,
            "state_": state_.tolist(),
            "done": done
        }
        try:
            res = requests.post(url=self.address, json=data)
            print('[+] Data successfully sent to core agent.')
        except:
            print('[X] Core agent is not running!')


""" # Tests
t = Http()
state = np.random.rand(11, 35, 35)
action = 4
reward = 2.5
state_ = np.random.rand(11, 35, 35)
done = False
t.send(state, action, reward, state_, done)
 """

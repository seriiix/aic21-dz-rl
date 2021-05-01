# DZ-Coffee runner v2

import subprocess
import threading
import os
from time import sleep

from torch import serialization

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_DIR_PATH = os.path.join(CURRENT_DIR, '../aic21-dz-game')
SERVER_JAR_PATH = os.path.join(SERVER_DIR_PATH, 'server.jar')
CLIENT_RUNNER_PATH = os.path.join(SERVER_DIR_PATH, 'cli-runner/runner.exe')

LEARN_CLIENT_PATH = os.path.join(
    CURRENT_DIR, "../aic21-dz-client/Controller.py")
RELEASE_CLIENT_PATH = os.path.join(
    CURRENT_DIR, "../aic21-dz-client-release/Controller.py")


class GameRunner:
    def __init__(
        self,
        runner_id="runner_id_0",
    ):
        self.runner_id = runner_id

    def server(self):
        # TODO: randomize first team and second team as learner and release
        subprocess.run(
            ["java", "-jar", SERVER_JAR_PATH,
             f"--first-team={CLIENT_RUNNER_PATH} {LEARN_CLIENT_PATH}",
             f"--second-team={CLIENT_RUNNER_PATH} {LEARN_CLIENT_PATH}"
             ],
            check=True,
            cwd=SERVER_DIR_PATH)
        # stdout=subprocess.DEVNULL,
        # stderr=subprocess.DEVNULL)

    def run(self):
        self.server()
        #threading.Thread(target=self.server, args=[]).start()


while(True):
    game = GameRunner()
    game.run()
    sleep(3)

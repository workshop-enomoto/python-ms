from flask import Flask
from multiprocessing import Value
import os
import socket

app = Flask(__name__)

@app.route('/hello-python')
def hello():
    with counter.get_lock():
        counter.value += 1
        unique_count = counter.value    

    message = 'Hello World Python: %s -> %s \n' % (socket.gethostname(), str(counter.value))
    app.logger.info(message)
    return message

counter = Value('i', 0)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)
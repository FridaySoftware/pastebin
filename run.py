#!/usr/bin/env python3
# debug

from src import application

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)

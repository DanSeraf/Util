#!/usr/bin/env python3

from config import initConfig, getConfig
from fileop import jsonCheck

def main():
    try:
        jsonCheck()
        initConfig()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()


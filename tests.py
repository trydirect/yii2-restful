#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import docker

client = docker.from_env()
time.sleep(20)  # we expect all containers to be up and running in 20 secs

for c in client.containers.list():
    print("{}: {}" .format(c.name, c.status))
    if 'running' not in c.status:
        print(c.logs())


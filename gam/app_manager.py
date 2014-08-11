#!/usr/bin/env python
# encoding: utf-8

from gam import git_manager

class AppManager:
    def __init__(self):
        pass

    def update(self):
        git = git_manager.GitManager()
        if git.check_update():
            git.update()
        else:
            print("No have updated!")

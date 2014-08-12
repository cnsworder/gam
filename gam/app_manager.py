#!/usr/bin/env python
# encoding: utf-8

from gam import git_manager

class AppManager:
    def __init__(self):
        self.app_list = []

    def update(self):
        """
        check update from github
        """
        git = git_manager.GitManager()
        if git.check_update():
            git.update()
        else:
            print("No have updated!")
    
    def read_app_list(self):
        """
        Read app list from conf/applists.conf
        """
        print("Read app list from conf/applists.conf")
        self.app_list.append("")

    def install_app_list(self):
        """
        Install application from list, install program in conf/<application name>.conf
        """
        print("Install application from list")

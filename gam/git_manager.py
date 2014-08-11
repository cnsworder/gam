#!/usr/bin/env python
# encoding: utf-8

from subprocess import *

class GitManager(Object):
    """
    git管理器,主要实现检查远程分支是否有更新,和执行更新操作
    """
    
    def clone(self, url, subpath=""):
        """
        远程clone项目
        """
        cmd = "git clone {0} {1}".format(url, subpath)
        sub = Popen(cmd)
        out = sub.commuicate()
        print(out)
        return True

    def check_update(self, branch="master"):
        """
        检查更新
        """
        fetch_cmd = "git fetch origin {0}".format(branch)
        code = call(fetch_cmd)
        if not code:
            return False

        status_cmd = "git status"
        sub = Popen(cmd)
        sub.wait()
        print(sub.stdout.read())
        return True

    def update(self, branch="master"):
        """
        更新分支
        """
        branch_cmd = "git checkout {0}".format(branch)
        code = call(branch_cmd)
        if not code :
            return False

        cmd = "git pull origin {0}".format(branch)
        sub = Popen(cmd)
        
        sub.wait()
        return True

#!/usr/bin/env python
# encoding: utf-8

from subprocess import *
import re

class GitManager(object):
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
        fetch_cmd = ["git", "fetch", "origin", branch]
        f_sub = Popen(fetch_cmd)
        if f_sub.wait():
            print("Fetch update info error!")
            return False

        status_cmd = ["git", "status", "--porcelain", "-b"]
        sub = Popen(status_cmd, stdout=PIPE)
        sub.wait()
        binfo = sub.stdout.read()
        reg = re.compile(r".*master$")
        info = binfo.decode()
        result = reg.match(info)
        return True if result else False

    def update(self, branch="master"):
        """
        更新分支
        """
        branch_cmd = ["git", "checkout", branch]
        code = call(branch_cmd, shell=True)
        if not code :
            return False

        cmd = "git pull origin {0}".format(branch)
        sub = Popen(cmd)
        sub.wait()
        return True

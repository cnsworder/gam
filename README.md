gam
===

update your app from github

account
------------------

+ friest time, update your configure file from github，must set your github repo, username and password
+ load update or install app configure
+ update or install your app

中文说明
--------------
+ 首次加载将会从github上加载你的配置文件，需要你设置你的github的仓库、用户名和密码
+ 载入你的需要升级或安装的应用的配置
+ 进行升级和安装操作

TODO
----------------

- [ ] git数据的更新检测  
- [ ] 配置文件的组织和定义  
- [ ] 配置文件的读取  
- [ ] 源码安装的配置方式  


env
----------------

初始化
```
virtualenv env --python=python2.7
```

进入环境

```
source env/bin/activate
```

退出环境
```
deactivate
```

requirements
---------------------

```
pip freeze > requirements.txt
```

```
pip install -r requirements.txt
```

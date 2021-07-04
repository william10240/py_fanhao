# 本分支停止更新,brook代理不好用,请切换main分支继续使用

<p align="center">
	<h1 align="center">番械库</h1>
	<h3 align="center">私人番号收藏</h3>
	<p align="center">
		<a href="http://www.williamyan.cn" target="_blank"><strong>Visit Suncoder &raquo;</strong></a>
	</p>
</p>

## 简介
每个人都有自己喜欢的番号，每个人都想有自己记录番号的小本本。。

当小本本记录了太多之后我们想找到今日想要的哪一部时，究竟哪行神秘代码对应哪部电影，想选择却无从下手

现在有个番号收藏，管理番号，so easy !

添加番号收藏后会自动添加番号对应的封面图片，演员，还可手动标记骑兵步兵

## 注意事项
根目录下"fan.db"文件为数据库文件,请注意存档备份;如有需要后续会推出自动备份功能

## 1编辑配置文件
首次运行前,从 conf.d/config.ini.base 拷贝一份 命名为 config.ini

在 conf.d/config.ini 的 "proxy" 里 "enable" 为true表示使用代理,false表示不使用代理

## 使用brook代理
编辑images里面的start.sh文件,将"000.000.000.000:00000"修改为代理服务的ip和端口

## 部署方式1:docker
编辑 conf.d/shadowsocks.json 文件,增加并修改如下内容
```
{
    "server": "xxxxxxxxxx",
    "server_port": xxxxxxxxxx,
    "local_address": "127.0.0.1",
    "local_port": 1080,
    "password": "xxxxxxxxxx",
    "timeout": 600,
    "method": "chacha20-ietf-poly1305",
    "fast_open": false
}
```
根目录下有docker-compose文件,直接"docker-compose up"

启动后默认端口是27004,在docker-compose.yml中可修改

启动后 <http://127.0.0.1:27004/> 访问


## 部署方法2:手动
确保本地小飞机软件已打开,并设置"允许其他设备接入",

端口设置默认为1080(具体方法请绅士),

在conf.d/config.ini中可配置代理连接信息

运行 app.py

启动后 <http://127.0.0.1:27004/> 访问



## 问题处理
 获取番号信息时报错,
```
1.请检查程序所在环境是否能正常访问到小飞机的代理,

2.如果代理没有问题,则可能是代理环境无法访问配置文件中配置的"dbweb"网址,则把小飞机更换为全局代理模式实施

​3.dbweb地址可能会更换,使用浏览器打开dbweb网址看是否能访问,如果还不能访问请发issue,题主会定期更换
```

## 技术参考
> 系统使用 [python3](https://www.python.org/downloads/) 编写，需要用到的组件有 request, aiohttp, peewee, jinja2
数据库使用sqlite,保存在根目录 "fan.db" 中

### license
> 本作品仅供学习交流使用，对使用后产生的任何后果不承担任何责任; 前方净空,允许进入,祝君武运昌隆

### todo:
> ~~配置项集中到配置文件~~
>
> ~~换用sqlite存储方式~~
>
> 自动化初始脚本

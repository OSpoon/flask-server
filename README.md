# flask-server

使用flask开发整套服务

## 初始化虚拟环境

安装命令: ` pip install pipenv `

**创建环境**: `pipenv --three`

其他命令:

```python
pipenv --three   会使用当前系统的Python3创建环境
pipenv --python 3.6 指定某一Python版本创建环境
pipenv shell 激活虚拟环境
pipenv --where  显示目录信息
pipenv --venv  显示虚拟环境信息
pipenv --py  显示Python解释器信息
pipenv install requests 安装相关模块并加入到Pipfile
pipenv install django==1.11 安装固定版本模块并加入到Pipfile
pipenv graph 查看目前安装的库及其依赖
```

**PyCharm指定虚拟环境**:

1. File->Settings-Project:flask-server->Project Interpreter
2. 选择Show All
3. 点击加号->选择Add Local
4. 选择Existing environment
5. 执行pipenv --venv查看虚拟环境地址并找到`\Scripts\python.exe`
6. 依次点击OK完成



## 使用flask-script启动服务:

`python manage.py runserver -h 127.0.0.1 -p 8090`

## 数据库创建

manage.py添加app,db,model到shell上下文:

```python
def make_shell_context():
    return dict(app=app, db=db, DateModel=DateModel)


manager.add_command("shell", Shell(make_context=make_shell_context))
```



## 使用@manager.command自定义命令 

创建命令:

```python
@manager.command
def create_data():
    print("create_data start")
    all_date_list = getAllDayPerYear("2020")
    for date in all_date_list:
        print('插入 : ', date)
        now_date = datetime.datetime.strptime(date,"%Y-%m-%d")
        if now_date.weekday() == 5 or now_date.weekday() == 6:
            db.session.add(DateModel(now_date, False))
        else:
            db.session.add(DateModel(now_date, True))
        db.session.commit()
    print("create_data end")
```



执行命令: `python manage.py create_data`

## 应用flasgger实现swagger文档查看

` http://127.0.0.1:9999/apidocs/ `




### 简介
基于 Python 3.8 + django 3.0 的博客系统， 仿用了经典的[NextT](https://theme-next.js.org/)主题。

#### 主要功能
- 文章，分类，标签的添加，删除，编辑等。
- 文章支持Markdown，支持代码高亮。
- 有留言板和归档页面。
- 支持开启live2d和播放网易云音乐歌曲。

#### 配置
- 首先文件内命令行输入 `pip install -r requirements.txt ` 安装依赖（Pycharm中点击![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710223301923.png)输入）

- 在 Blog / settings 中：
修改 SECRET_KEY
使用MySQL数据库，请创建一个数据库，并在下列标注的地方修改为自己的配置。   
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',	#修改
        'PASSWORD': '123456', #修改
        'NAME': 'blogs', #修改
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```
#### 迁移数据库

 在Pycharm中 :

<img src="https://img-blog.csdnimg.cn/20200710223348705.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70" width="40%">

打开后输入：

```bash
makemigrations
migrate
```
#### 创建超级用户

```bash
createsuperuser
```
#### 配置主题
完成以上即可运行，点击头像即可进入后台（默认未设置，所以没有加载头像）

增加主题配置：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710224119534.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)

### 效果图
##### 主页：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710223908444.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)
##### 文章页：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710224238702.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)
##### 分类页：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710224344314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)
##### 归档页：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020071022443624.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)
##### 留言页：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710224518694.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)
##### 文章markdown编辑：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710224654654.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)
##### 文章后台管理：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200710224737864.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNjQwMDA5,size_16,color_FFFFFF,t_70)

### PS：
本人是个Django新手，此博客花费了一周时间开发，很多进阶功能没有加入进去，以后更新。

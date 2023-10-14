# windows系统后台程序监听socket

## git push 代码步骤:

1.进入需要提交代码的文件夹

2.右键空白处选择git bash here, 此时会打开git命令行窗口

3.使用git init命令初始化此项目, 此时会自动生成名为.git的文件夹

4.使用git add <file name> 命令添加需要push的文件，使用git add . 则添加所有文件

5.使用git commit -m "本次添加名"

6.使用git status命令查看已添加的文件

7.使用git remote add origin "需要push到的ssh地址"

8.使用git push -u origin master即可提交代码

## github ssh提交代码步骤:

1.首先当然需要安装好git

2.右键空白处打开git bash here

3.输入命令ssh-keygen -t rsa -C "自己的github电子邮箱", 敲三下回车, 此时会自动生成秘钥

4.完成以后，输入cat ~/.ssh/id_rsa.pub查看公钥, 复制秘钥

5.登入github, 点击settings, 再点击SSH keys添加刚才复制的秘钥

6.配置完成

## 创建分支

git branch 分支名

例如: git branch template

## 删除分支

### 删除本地分支

git branch -d 分支名

### 删除远程分支

git push origin --delete 分支名

### 提交代码到其他分支

git push -u origin 分支名

例如: git push -u origin template

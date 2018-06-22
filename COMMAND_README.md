DeerU 内置命令
-------------

install命令
=========
install命令用于安装下载deeru主项目，主题，插件

```bash
deeru install type name
```
参数：
* type:  安装的类型，可选项{project,plugin,theme}，实际上plugin,theme可以相互替换，
他们两的区别仅在于安装完成后是否运行收集静态文件命令
* name:  项目的名字，或插件，主题的名字
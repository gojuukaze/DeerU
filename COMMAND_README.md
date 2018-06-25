DeerU 内置命令
-------------

install命令
=========
install命令用于安装下载deeru主项目，主题，插件

```bash
deeru install type name [--mode] [--branch]
```
参数：
* type:  安装的类型，可选项{project,plugin,theme}
* name:  项目的名字，或插件，主题的名字
* --mode:  下载方式，type为project时默认git，可选项{git,pip}
* --branch:  分支，mode为git时有效
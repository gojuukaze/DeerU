.. _config:

==============
配置
==============

v2版对配置进行了升级，新增了handler代替原来的expression，并使用 `json-editor <https://github.com/json-editor/json-editor>`_ 使配置可视化。  

deeru默认提供了4个配置，"博客配置"，"顶部图标栏配置"，"顶部导航栏配置"，"通用配置"。最后一个 ``通用配置`` 是key-value的配置，
用于给不想写复杂配置的开发者提供一个简单的进行配置的地方。

如何添加新的可视化配置
----------------------------

配置的model
````````````

首先你需要了解下配置的model，其代码在 ``app.app_models.config_model`` 下，有下面几个字段：  

.. py:class:: Config

    .. py:attribute:: name
        
        中文名字

    .. py:attribute:: v2_config
        
        配置的原始数据

    .. py:attribute:: v2_real_config
        
        经过handler处理后的配置数据，v2_config中的配置有的需要经过handler解析后才能使用，  
        保存配置时会自动处理v2_config并把结果保存到这

    .. py:attribute:: v2_schema
        
        json-editor用的参数，这里面的js代码而不是python，
        如果你对js不熟悉，那就写json结构的数据

    .. py:attribute:: v2_script

        js代码，会添加到创建json-editor之后，用于修改json-editor的展示效果

编写可视化配置的schema
``````````````````````````

目前所使用的json-editor是v2.0.0版本，默认使用spectre主题，fontawesome5图标库，swig模板引擎，
虽然你可以自由替换json-editor所使用的主题，图标库，模板引擎，但并不建议你更换。  

你可以查看json-editor的文档，学习如何编写配置。自带的4个配置的schema在 ``app.consts.V2_Config_Schema`` 下，你可以参考他们编写。

下面是一个schema的样例：

.. code-block:: js 
   
   {
    "theme": "spectre",
    "iconlib": "fontawesome5",
    "template": "swig",
    "schema": {
        "type": "object",
        "title": "博客配置",
        "properties": {
            "host": {
                "type": "string",
                "title": "博客域名或ip",
                "format": "url"
            }
        }
    }
   }

.. note:: 

   需要注意的是，内部的schema并不是Config model中的v2_schema，v2_schema是这个结构整体。

   另外，你自定义的配置中不要使用 ``_`` 开头的key，如示例中的 "host"，不要用 "_host"。

如果你想快速实验你编写的schema效果，可以使用下面代码，把 ``o`` 替换为你的代码。  

点击输出结果后会显示保存到 ``v2_config`` 的数据，以及格式化后的schema；建议直接复制这个格式化好的schema到Config model中。

.. code-block:: html 

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>Basic JSON Editor Example</title>
        <link rel='stylesheet' href='https://cdn.staticfile.org/spectre.css/0.5.8/spectre.min.css'>
        <link rel='stylesheet' href='http://cdn.staticfile.org/font-awesome/5.11.2/css/all.min.css'>
        <script src="https://cdn.jsdelivr.net/npm/@json-editor/json-editor@v2.0.0/dist/jsoneditor.min.js"></script>
        <script src="https://cdn.staticfile.org/swig/1.4.2/swig.min.js"></script>
    </head>
    <body>
    <h1>Basic JSON Editor Example</h1>
    <div id='editor_holder'></div>
    <hr>
    <div style="margin-left: 20px;margin-top: 20px">
        <button class="btn " id='submit'>输出结果</button>
        <div style="margin-top: 20px">
            <textarea id="json" style="padding: 5px" cols="50" rows="40"></textarea>
            <textarea id="options" style="padding: 5px;margin-left: 20px" cols="50" rows="40"></textarea>
        </div>
    </div>
    <script>
        // 把 o 替换为你的代码
        var o = {
            theme: 'spectre',
            iconlib: 'fontawesome5',
            template: 'swig',
            schema: {
                type: "object",
                properties: {
                    title:{
                        type:'string'
                    }
                },
            }
        };
    
        var oS = JSON.stringify(o);
        var editor = new JSONEditor(document.getElementById('editor_holder'), o);
        document.getElementById('submit').addEventListener('click', function () {
            document.getElementById('json').innerText = JSON.stringify(editor.getValue(), null, 3);
            document.getElementById('options').innerText = oS;
        });
    </script>
    </body>
    </html>

编写v2_script
````````````````````

v2_script是一段js代码，会添加到创建json-editor之后，用于自定义修改json-editor的展示效果。  

如果你需要用python代码向model中插入v2_script，建议用 ``r`` 前缀的字符串，否则需要处理转义字符。如：

.. code-block:: python 

   js = r'console.log(11)'

配置的handler
-----------------------

有时候还需要对保存的配置进行进一步处理，以获得最终需要的配置，因此引入了handler的概念，关于handler的更多内容查看： :ref:`handler`

在html中使用配置
------------------------
如果你新建了一个新的配置，并希望在前端代码中读取它，那你需要两步操作：

（示例是直接修改app中的代码，实际操作时建议新建一个django的app，然后在新的app中操作）

1. 在apps.py中修改/添加 ``deeru_config_context`` 的值，如app/apps.py文件：

.. code-block:: python 

   class MAppConfig(AppConfig):

       deeru_config_context = 'app.consts.app_config_context'

2. 编辑 ``deeru_config_context`` 指向的对象（app/consts.py中的app_config_context）

.. code-block:: python 

   app_config_context = {
    'top_ico': '顶部图标栏',
    'top_menu': '顶部导航栏',
   }

它是一个字典，key为在前端代码中使用的名字，value为数据库中的名字。

3. 在前端代码中这样使用它：

.. code-block:: html 

   {{ config.top_ico.xxx }}

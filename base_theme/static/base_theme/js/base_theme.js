function createCommentEditor(s) {
    var joditEditor = new Jodit(s, {
        colorPickerDefaultTab: 'color',
        buttons: ['fontsize', 'brush', '|', 'bold', 'strikethrough', 'underline', 'italic', '|', 'link'],
        buttonsMD: ['fontsize', 'brush', '|', 'bold', 'strikethrough', 'underline', 'italic', '|', 'link'],
        buttonsSM: ['fontsize', 'brush', '|', 'bold', 'strikethrough', 'underline', 'italic', '|', 'link'],
        buttonsXS: ['fontsize', 'brush', '|', 'bold', 'strikethrough', 'underline', 'italic', '|', 'link'],
        beautifyHTML: false,
        language: 'zh_cn',
        extraButtons: [
            {
                name: 'code',
                exec: function (editor, current, control) {
                    var node = document.createElement('pre');
                    var currentNode = editor.selection.current();
                    layer.prompt({title: '插入代码', formType: 2},
                        function (text, index) {
                            layer.close(index);
                            node.innerText = text;
                            editor.selection.setCursorIn(currentNode);
                            editor.selection.insertNode(node);
                        });
                }
            },
            {
                name: "emoji",
                popup: function (editor) {
                    var s = '<div class="emoji_tabs" ><a href="javascript:void(0)">😀</a><a href="javascript:void(0)">😁</a><a href="javascript:void(0)">😂</a><a href="javascript:void(0)">😃</a><a href="javascript:void(0)">😄</a><a href="javascript:void(0)">😅</a><a href="javascript:void(0)">😆</a><a href="javascript:void(0)">😇</a><br><a href="javascript:void(0)" title="微笑的脸角">😈</a><a href="javascript:void(0)">😉</a><a href="javascript:void(0)">😊</a><a href="javascript:void(0)">😋</a><a href="javascript:void(0)" title="面对如释重负">😌</a><a href="javascript:void(0)">😍</a><a href="javascript:void(0)">😎</a><a href="javascript:void(0)" title="面对面带笑容">😏</a><br><a href="javascript:void(0)" title="中性面">😐</a><a href="javascript:void(0)" title="面无表情">😑</a><a href="javascript:void(0)">😒</a><a href="javascript:void(0)">😓</a><a href="javascript:void(0)">😔</a><a href="javascript:void(0)" title="面对困惑">😕</a><a href="javascript:void(0)" title="该死的脸">😖</a><a href="javascript:void(0)" title="面对接吻">😗</a><br><a href="javascript:void(0)" title="面对投掷一个吻">😘</a><a href="javascript:void(0)" title="接吻脸，含笑的眼睛">😙</a><a href="javascript:void(0)" title="接吻的脸闭着眼睛">😚</a><a href="javascript:void(0)" title="面对伸出舌头">😛</a><a href="javascript:void(0)">😜</a><a href="javascript:void(0)">😝</a><a href="javascript:void(0)" title="面对失望">😞</a><a href="javascript:void(0)" title="面对担心">😟</a><br><a href="javascript:void(0)" title="愤怒的脸">😠</a><a href="javascript:void(0)" title="面对噘嘴">😡</a><a href="javascript:void(0)" title="哭泣的脸">😢</a><a href="javascript:void(0)" title="怎奈脸">😣</a><a href="javascript:void(0)" title="面带看的胜利">😤</a><a href="javascript:void(0)">😥</a><a href="javascript:void(0)">😦</a><a href="javascript:void(0)" title="面对痛苦">😧</a><br><a href="javascript:void(0)" title="可怕的脸">😨</a><a href="javascript:void(0)" title="面对厌倦">😩</a><a href="javascript:void(0)" title="面对困">😪</a><a href="javascript:void(0)" title="疲惫的脸">😫</a><a href="javascript:void(0)" title="狰狞的脸">😬</a><a href="javascript:void(0)" title="大声哭脸">😭</a><a href="javascript:void(0)">😮</a><a href="javascript:void(0)">😯</a><br><a href="javascript:void(0)" title="脸上露出嘴巴和冷汗">😰</a><a href="javascript:void(0)" title="面对张开嘴，一身冷汗">😱</a><a href="javascript:void(0)" title="面对惊讶">😲</a><a href="javascript:void(0)" title="红扑扑的脸蛋">😳</a><a href="javascript:void(0)" title="熟睡的脸">😴</a><a href="javascript:void(0)" title="面对眩">😵</a><a href="javascript:void(0)" title="脸上没有嘴">😶</a><a href="javascript:void(0)">😷</a></div>';
                    var div = document.createElement('div');
                    div.innerHTML = s;
                    div.onclick = function (e) {
                        console.log(e.target);
                        var emoji = $(e.target);
                        editor.selection.insertHTML(emoji.text());
                        emoji.parent().parent().parent().remove();
                    };
                    return div;
                }
            }
            , 'eraser'
        ],
        events: {
            getIcon: function (name, control, clearName) {
                var code = clearName;
                switch (clearName) {
                    case 'fontsize':
                        code = 'fas fa-font';
                        break;
                    case 'brush':
                        code = 'fas fa-paint-brush';
                        break;
                    case 'bold':
                        code = 'fas fa-bold';
                        break;
                    case 'strikethrough':
                        code = 'fas fa-strikethrough';
                        break;
                    case 'underline':
                        code = 'fas fa-underline';
                        break;
                    case 'italic':
                        code = 'fas fa-italic';
                        break;
                    case 'quote':
                        code = 'fas fa-quote-left';
                        break;
                    case 'emoji':
                        code = 'far fa-smile';
                        break;
                    case 'code':
                        code = 'far fa-copyright';
                        break;
                    case 'eraser':
                        code = 'fas fa-eraser';
                        break;
                    case 'link':
                        code = 'fas fa-link';
                        break;
                }
                return '<i style="font-size:14px" class="' + code + '"></i>';
            }
        }
    });

    return joditEditor;

}


/*
工具集
 */


// 判断字符串长度，非ASCII算两个长度
function getStringLen(str) {
    if (str === null) return 0;
    if (typeof str !== "string"){
        str += "";
    }
    return str.replace(/[^\x00-\xff]/g,"01").length;
}

// dom及jquery对象
function isDomObject(obj){
    return ( typeof HTMLElement === 'object' ) ?
            function(obj){
                return obj instanceof HTMLElement;
            } :
            function(obj){
                return obj && typeof obj === 'object'
                    && obj.nodeType === 1
                    && typeof obj.nodeName === 'string';
            };
}
function isJQueryObject(obj){
    return obj instanceof jQuery;
}
function getJQueryObject(obj){
    obj = typeof obj === 'string' ? $(obj) : obj;
    if(isDomObject(obj)) {
        return  $(obj);
    } else if (isJQueryObject(obj)) {
        return obj;
    }
    return null;
}
function getDomObject(obj){
    //
    if (typeof obj === 'string') {
        if (obj.split(' ').length === 1 && obj.indexOf('.') === 0) {
            obj = document.getElementById(obj)
        }
    } else if (isDomObject(obj)) {
        return  obj;
    } else if (isJQueryObject(obj)) {
        return obj.get(0);
    }
    return null;
}

/*
给任意元素添加Material tooltip
例
showTooltip({
            target: $usernameOrEmail,
            tooltip: '用户名/邮箱不能为空'
        })
 */
function showTooltip(settings) {
    console.log(settings);
    var defaultSetting={
        target: null,
        tooltip: '',
        position: 'bottom',
        html: false,
        delay: 350
    };
    var _properties = ['target', 'tooltip', 'position', 'html', 'delay'];
    $.each(Object.keys(settings), function (i, item) {
        if ($.inArray(item, _properties) < 0) {
            throw 'Invalid settings key "' + item + '"';
        }
    });
    $.extend(defaultSetting, settings);
    var $obj = getJQueryObject(settings.target);
    if (!$obj) {
        throw 'target is unknown';
    }
    $obj.tooltip({
        tooltip: settings.tooltip,
        delay: settings.delay,
        position: settings.position,
        html: settings.html
    });

    // remove
    // $obj.tooltip('remove');", 2000);
}
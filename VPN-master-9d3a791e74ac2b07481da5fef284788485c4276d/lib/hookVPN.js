// const fs = require('fs');

function getFunc(_className, ifsave) {
    Java.perform(function () {
        var class_obj = Java.use(_className);
        var methods = class_obj.class.getDeclaredMethods();
        for (var j = 0; j < methods.length; j++) {
            var method_str = methods[j].toString()
            var re = new RegExp("(\\(.*?\\))");
            var overload_type = re.exec(method_str)[1]
            let func_name = methods[j].getName();
            if (func_name.slice(0, 1).indexOf("-") != -1 || func_name.slice(0, 1).indexOf("$") != -1) {
                continue
            }

            if (method_str.search("void") == -1 && (return_type(method_str, _className, overload_type))) {
                eval(textFunc(_className, func_name, overload_type, ifsave));
                // console.log(method_str)
                // console.log(overload_type)
                // console.log(func_name)
                // console.log("android heap search instances " + _className);
                // break
            }

            // console.log("**************************************************************************************************************")
        }
    })
}

function return_type(method_str, _className, overload_type) {
    var overload = overload_type.slice(1, -1)
    if (overload.indexOf(",") != -1) {
        var args_list = overload.split(',');
        for (var j = 0; j < args_list.length; j++) {
            var arg = args_list[j];
            if (arg != "int" && arg != "boolean") {
                return true
            }
        }
    } else {
        if (overload != '' && overload != "int" && overload != "boolean") {
            return true
        }
    }
    var rtype = method_str.split(_className)[0];
    if (rtype.search("int") == -1 && rtype.search("boolean") == -1) {
        return true
    } else {
        return false
    }
}

function textFunc(_className, func_name, overload_type, ifsave) {
    var overload = overload_type.slice(1, -1);
    var args = process_args(overload);
    var overload_pro = process_voerload(overload);
    // var func_name_pro = process_funcname(func_name);

    var TextFunc = `
        var class_obj = Java.use("_className");
        class_obj.func_name.overload(overloads).implementation = function (args) {
            var res = this.func_name(args);
            hook_res_process(ifsave, "_className", "func_name", res, [args]);
            return res
        }
        `;
    TextFunc = replaceAll(TextFunc, "ifsave", ifsave);
    TextFunc = replaceAll(TextFunc, "_className", _className);
    TextFunc = replaceAll(TextFunc, "func_name", func_name);
    TextFunc = replaceAll(TextFunc, "overloads", overload_pro);
    TextFunc = replaceAll(TextFunc, "args", args);
    // console.log(TextFunc);
    return TextFunc

}

function process_funcname(funcname) {
    if (funcname.indexOf("-") != -1) {
        funcname = funcname.slice(1);
    }
    return funcname
}

function hook_res_process(ifsave, _className, func_name, res, argsArray) {
    var return_tostring
    if (res) {
        return_tostring = res.toString();
    } else {
        return_tostring = '';
    }

    var atgs_tostring = log_array(argsArray)
    var return_bool = re_keywords(return_tostring)
    var args_bool = re_argsArray(atgs_tostring)
    // console.log("return_bool: ", return_bool, ",     args_bool: ", args_bool);
    // console.log("****class_func:", _className, func_name, "    ****return:", return_tostring, "    ****arg(args):", atgs_tostring);
    if (return_bool || args_bool) {
        console.log("****class_func:", _className, func_name, "    ****return:", return_tostring, "    ****arg(args):", atgs_tostring);
        var a = ["****class_func:", _className, func_name, "    ****return:", return_tostring, "    ****arg(args):", atgs_tostring].join(' ')
        send(a);
        // if (ifsave) {
        //     var message = ["****class_func:", _className, func_name, "    ****return:", return_tostring, "    ****arg(args):", atgs_tostring].join()
        //     save_data(message)
        // }
    }

}

function log_array(argsArray) {
    if (argsArray && argsArray != '') {
        var args_array = []
        for (var j = 0; j < argsArray.length; j++) {
            if (argsArray[j]) {
                args_array.push(argsArray[j].toString())
            }
        }
        return args_array.join(', ')
    }
    return ''

}

function re_keywords(str) {
    var reArray = ["\\d+\\.\\d+\\.\\d+\\.\\d+", "password"]
    for (var j = 0; j < reArray.length; j++) {
        var re = new RegExp(reArray[j], "i")
        var r = re.exec(str)
        // console.log(r);
        if (r) {
            return true
        }
    }
    return false
}

function re_argsArray(argsArray) {
    for (var j = 0; j < argsArray.length; j++) {
        if (re_keywords(argsArray[j].toString())) {
            return true
        }
    }
    return false
}

function re_class_instance(string1) {
    console.log("string1: ", string1);
    var re = new RegExp("$className: (.*?)>", "g")
    var className = re.exec(string1)
    console.log("className1:", className);
    if (!className) {
        re = new RegExp("instance: (.*?)>", "g");
        className = re.exec(string1);
        console.log("className2:", className);
    }
    if (className) {
        var JavaByte = Java.use(className[1]);
        var buffer = Java.cast(x, JavaByte);
        var result = Java.array('byte', buffer);
    }
    return result
}

function process_voerload(overload_type) {
    if (overload_type.indexOf("byte[]") != -1) {
        overload_type = overload_type.replace("byte[]", "[B");
    }
    var voerload = Array();
    if (overload_type.indexOf(",") != -1) {
        var args_list = overload_type.split(',');
        for (var j = 0; j < args_list.length; j++) {
            var arg = '"' + args_list[j] + '"';
            voerload.push(arg);
        }
        return voerload.join(',');
    } else {
        if (overload_type == '') {
            return ''
        }
        return '"' + overload_type + '"';
    }
}

function process_args(overload_type) {
    overload_type = overload_type.replace("byte[]", "byte");
    var args = Array();
    if (overload_type.indexOf(",") != -1) {
        var args_list = overload_type.split(',');
        for (var j = 0; j < args_list.length; j++) {
            var arg = args_list[j];
            if (arg.indexOf(".") != -1) {
                var arr_arg = arg.split('.');
                var arr_lenth = arr_arg.length;
                arg = arr_arg[arr_lenth - 1];
            }
            args.push(arg + j);
        }
        return args.join(',');
    } else {
        if (overload_type.indexOf(".") != -1) {
            var arr_arg = overload_type.split('.');
            var arr_lenth = arr_arg.length;
            overload_type = arr_arg[arr_lenth - 1];
        }
        return overload_type;
    }
}

function replaceAll(value, pattern, reg) {
    return value.replace(new RegExp(pattern, "g"), reg);
}

function save_data(message) {
    fs.appendFile('data', message + "\n", function (err) {
        if (err) {
            return console.log('文件写入失败！' + err.message);
        }
        console.log(message);
    })

}

function hookClass(_className) {
    getFunc(_className, true)
    console.log("[*] class enuemration complete");
}

function FridaJava() {
    Java.perform(function () {
            console.log("\n[*] enumerating classes...");
            Java.enumerateLoadedClasses({
                onMatch: function (_className) {
                    var strArray = ["vpn", "VPN", "Vpn", "proxy", "socks", "Config", "Node", "Server", "Mgr"];
                    for (var i = 0; i < strArray.length; i++) {
                        if (_className.indexOf(strArray[i]) != -1) {
                            if (_className.indexOf("android.") == -1 && _className.indexOf("[L") == -1 && _className.indexOf("java.") == -1 && _className.indexOf("javax.") == -1) {
                                // console.log("[*] found instance of '" + _className + "'");
                                // console.log(_className);
                                var count_ss = 0;
                                Java.choose(_className, {
                                    "onMatch": function (ist) {
                                        count_ss = count_ss + 1;
                                    },
                                    "onComplete": function () {
                                        if (count_ss > 0) {
                                            // console.log(_className, "found count is:" + count_ss);
                                            getFunc(_className);
                                        }

                                    }
                                });
                                // getFunc(_className);

                            }
                        }
                    }
                },
                onComplete: function () {
                    console.log("[*] class enuemration complete");
                }
            });
        }
    );

}
function ttt() {
    Java.perform(function () {
        var class_obj = Java.use("android.util.Log");
        class_obj.d.overload("java.lang.String", "java.lang.String").implementation = function (str1, str2) {
            var resss = this.d(str1, str2);
            console.log("str2: ", str2)
            return resss
        }
})
}

// java.io.FileOutputStream
function main() {
    // FridaJava()
    // ttt()
    hookClass("")
}
// frida -U com.work.naiyou -l hookVPN.js --no-pause
// objection -g com.work.naiyou explore
// android hooking watch class okhttp3.Response --dump-args --dump-backtrace --dump-return
// android hooking watch class_method okhttp3.Response.networkResponse --dump-args --dump-backtrace --dump-return
// android.util.Log
setTimeout(main, 1500);

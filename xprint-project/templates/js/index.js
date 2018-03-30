
//时间部分
//补位函数。  
function extra(x) {
    //如果传入数字小于10，数字前补一位0。  
    if (x < 10) {
        return "0" + x;
    }
    else {
        return x;
    }
}
//获取系统时间，将时间以指定格式显示到页面。  
function systemTime() {
    //获取系统时间。  
    var now = new Date();
    var year = now.getFullYear();       //年  
    var month = now.getMonth() + 1;     //月  
    var day = now.getDate();            //日   
    var hh = now.getHours();            //时  
    var mm = now.getMinutes();          //分  
    var ss = now.getSeconds();            //秒       
    //一位数字，在数字前补0。  
    month = extra(month);
    day = extra(day);
    hh = extra(hh);
    mm = extra(mm);
    ss = extra(ss);
    //将时间显示到ID为time的位置
    document.getElementById("time").innerHTML = year + "-" + month + "-" + day + "   " + hh + ":" + mm + ":" + ss;
}
//打印部分
function showAndhidden() {
    var print = document.getElementById("printPage");  //获取打印区域
    print.style.display = "";  //让其显示
    var show = document.getElementById("show");  //获取原先的页面区域
    show.style.display = "none";     //让其隐藏
    printpage("printPage");    //调用方法 让要打印的内容显示
}
function printpage(m_printpage1) {
    var newstr = document.getElementById(m_printpage1).innerHTML;  //获取要打印的内容
    var oldstr = document.body.innerHTML; //保存原先的页面内容
    document.body.innerHTML = newstr;  //将打印内容给页面
    window.print(); // 调用浏览器里的打印功能
    document.body.innerHTML = oldstr;  //打印完成后 重新将原先的内容给页面
    backHidden();   //调用函数  使其还原原有内容页
    return false;
}
function backHidden() {
    var print = document.getElementById("printPage");   //获取要打印的区域
    print.style.display = "none";               //让其隐藏
    var show = document.getElementById("show");   //获取原先的页面显示内容
    show.style.display = "";       //让其显示
}
function printPage() {
    $("#bt").css("display", "none");
    self.print();
    $("#bt").css("display", "");
    return false;
}
//身份证部分显示
function cardNumber() {
    var _Id_Card = document.getElementById("number").innerHTML;
    var _str_Start = _Id_Card.substr(0, 3);
    var _str_End = _Id_Card.substr(14, 4);
    var _ss = function () { var s = ""; for (var i = 0; i < 18 - 7; i++) s += "*"; return s; };
    var _str_Res = _str_Start + _ss() + _str_End;
    document.getElementById("number").innerHTML = _str_Res;
}
//生日部分显示
function birthday() {
    var birthday = document.getElementById("birthday").innerHTML;
    var _str1 = birthday.substr(0, 5);
    var _str2 = birthday.substring(7, 8);
    var _ss1 = function () { var m = ""; for (var i = 0; i < 2; i++) m += "*"; return m; };
    var _str3 = birthday.substr(10, 11);
    var _ss2 = function () { var n = ""; for (var i = 0; i < 2; i++) n += "*"; return n; };
    var _str_Birth = _str1 + _ss1() + _str2 + _ss2() + _str3;
    document.getElementById("birthday").innerHTML = _str_Birth;
}




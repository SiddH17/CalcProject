// jquery code
// code for sidebar
$(document).ready(function(){
    $(".closebtn").hide();
    $(".openbtn").click(function(){
        $(".openbtn").hide();
        $(".closebtn").show();
    });
    $(".closebtn").click(function(){
        $(".closebtn").hide();
        $(".openbtn").show();
    });
});
// code for kinematics content
$(document).ready(function(){
    $("#eqmtnid").hide();
    $("#dispbtn").hide();
    $("#timebtn").hide();
    $("#initvelbtn").hide();
    $("#finvelbtn").hide();
    $("#accbtn").hide();
    
    $("#blank1").click(function(){
        $("#eqmtnid").hide();
        $("#dispbtn").hide();
        $("#timebtn").hide();
        $("#initvelbtn").hide();
        $("#finvelbtn").hide();
        $("#accbtn").hide();
    });
    $("#disp").click(function(){
        $("#eqmtnid").show();
        $("#dispbtn").show();
        $("#timebtn").hide();
        $("#initvelbtn").hide();
        $("#finvelbtn").hide();
        $("#accbtn").hide();
    });
    $("#time").click(function(){
        $("#eqmtnid").show();
        $("#timebtn").show();
        $("#dispbtn").hide();
        $("#initvelbtn").hide();
        $("#finvelbtn").hide();
        $("#accbtn").hide();
    });
    $("#initvel").click(function(){
        $("#eqmtnid").show();
        $("#initvelbtn").show();
        $("#dispbtn").hide();
        $("#timebtn").hide();
        $("#finvelbtn").hide();
        $("#accbtn").hide();
    });
    $("#finvel").click(function(){
        $("#eqmtnid").show();
        $("#finvelbtn").show();
        $("#dispbtn").hide();
        $("#timebtn").hide();
        $("#initvelbtn").hide();
        $("#accbtn").hide();
    });
    $("#acc").click(function(){
        $("#eqmtnid").show();
        $("#accbtn").show();
        $("#dispbtn").hide();
        $("#timebtn").hide();
        $("#initvelbtn").hide();
        $("#finvelbtn").hide();
    });
});

// javascript code
// code for sidebar
function openNav()  {
    document.getElementById('physidebar').style.width = "250px";
    document.getElementById('main').style.marginLeft = "250px";
    document.getElementById('physidebar').style.height = "1000px";
}
function closeNav() {
    document.getElementById('physidebar').style.width = "0";
    document.getElementById('main').style.marginLeft = "0";
}

// code for kinematics
function funcDispSec()  {
    let u = prompt("Enter initial velocity: ", 0);
    let t = prompt("Enter time: ", 0)
    let a = prompt("Enter acceleration: ", 0)
    s = u*t + 0.5*a*(t**2)
    document.getElementById("eqmtnans").innerHTML = "Displacement = "+ s;
}
function funcDispTrd()   {
    let u = prompt("Enter Initial Velocity: ", 0);
    let v = prompt("Enter Final Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    s = (v**2 - u**2)/2*a;
    document.getElementById("eqmtnans").innerHTML = "Displacement = "+ s;
}
function funcTimeFst()  {
    let u = prompt("Enter Initial Velocity: ", 0);
    let v = prompt("Enter Final Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    t = (v-u)/a
    if(t>=0)    {
        document.getElementById("eqmtnans").innerHTML = "Time = "+ t;
    }
    else    {
        document.getElementById("eqmtnans").innerHTML = "Time cannot be negative!";
    }
}
function funcTimeSec()  {
    let s = prompt("Enter Displacement: ", 0);
    let u = prompt("Enter Initial Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    t = (-u+((u**2)+(2*a*s))**(1/2))/a
    let dec = Math.floor(t*1000)/1000;
    if(dec>=0)    {
        document.getElementById("eqmtnans").innerHTML = "Time = "+ dec;
    }
    else    {
        document.getElementById("eqmtnans").innerHTML = "Time cannot be negative!";
    }
}
function funcInitFst()  {
    let t = prompt("Enter Time: ", 0);
    let v = prompt("Enter Final Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    u = v-(a*t)
    document.getElementById("eqmtnans").innerHTML = "Initial Velocity = "+ u;
}
function funcInitSec()  {
    let t = prompt("Enter Time: ", 0);
    let s = prompt("Enter Displacement: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    u = (s-(0.5*a*(t**2)))/t
    document.getElementById("eqmtnans").innerHTML = "Initial Velocity = "+ u;
}
function funcInitTrd()  {    
    let s = prompt("Enter Displacement: ", 0);
    let v = prompt("Enter Final Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    u = ((v**2)-(2*a*s))**(1/2);
    let dec = Math.floor(u*1000)/1000;
    document.getElementById("eqmtnans").innerHTML = "Initial Velocity = "+ dec;
}
function funcFinFst()   {
    let t = prompt("Enter Time: ", 0);
    let u = prompt("Enter Initial Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    v = u+(a*t);
    document.getElementById("eqmtnans").innerHTML = "Final Velocity = "+ v;
}
function funcFinTrd()   {
    let s = prompt("Enter Displacement: ", 0);
    let u = prompt("Enter Initial Velocity: ", 0);
    let a = prompt("Enter Acceleration: ", 0);
    v = ((u**2)+(2*a*s))**(1/2)
    let dec = Math.floor(v*1000)/1000;
    document.getElementById("eqmtnans").innerHTML = "Final Velocity = "+ dec;
}
function funcAccFst()   {
    let t = prompt("Enter Time: ", 0);
    let u = prompt("Enter Initial Velocity: ", 0);
    let v = prompt("Enter Final Velocity: ", 0);
    a = (v-u)/t
    document.getElementById("eqmtnans").innerHTML = "Acceleration = "+ a;
}
function funcAccSec()   {
    let s = prompt("Enter Displacement: ", 0);
    let t = prompt("Enter Time: ", 0);
    let u = prompt("Enter Initial Velocity: ", 0);  
    a = 2*((s-(u*t))/(t**2))
    let dec = Math.floor(a*1000)/1000;
    document.getElementById("eqmtnans").innerHTML = "Acceleration = "+ dec;
}
function funcAccTrd()   {
    let s = prompt("Enter Displacement: ", 0);
    let u = prompt("Enter Initial Velocity: ", 0);
    let v = prompt("Enter Final Velocity: ", 0);
    a = ((v**2)-(u**2))/(2*s)
    document.getElementById("eqmtnans").innerHTML = "Acceleration = "+ a;
}





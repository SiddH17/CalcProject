// jquery code
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

// javascript code
function openNav()  {
    document.getElementById('physidebar').style.width = "250px";
    document.getElementById('main').style.marginLeft = "250px";
    document.getElementById('physidebar').style.height = "100vh";
    document.getElementById('phybody').style.marginLeft = '245px';
}
function closeNav() {
    document.getElementById('physidebar').style.width = "0";
    document.getElementById('main').style.marginLeft = "0";
    document.getElementById('phybody').style.marginLeft = '0';
}
function openMathNav()  {
    document.getElementById('mathsidebar').style.width = '250px';
    document.getElementById('main').style.marginLeft = '250px';
    document.getElementById('mathsidebar').style.height = '100vh';
}
function closeMathNav() {
    document.getElementById('mathsidebar').style.width = '0';
    document.getElementById('main').style.marginLeft = '0';
}
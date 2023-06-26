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
    document.getElementById('chemsidebar').style.width = "250px";
    document.getElementById('main').style.marginLeft = "250px";
    document.getElementById('chemsidebar').style.height = "1000px";
}
function closeNav() {
    document.getElementById('chemsidebar').style.width = "0";
    document.getElementById('main').style.marginLeft = "0";
}
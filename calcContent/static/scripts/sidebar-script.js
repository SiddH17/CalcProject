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
// Opening physics sidebar
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

// Opening maths sidebar
function openMathNav()  {
    document.getElementById('mathsidebar').style.width = '250px';
    document.getElementById('main').style.marginLeft = '250px';
    document.getElementById('mathsidebar').style.height = '100vh';
}
function closeMathNav() {
    document.getElementById('mathsidebar').style.width = '0';
    document.getElementById('main').style.marginLeft = '0';
}

// Opening chemistry sidebar
function openChemNav()  {
    document.getElementById('chemsidebar').style.width = "250px";
    document.getElementById('main').style.marginLeft = "250px";
    document.getElementById('chemsidebar').style.height = "100vh";
    document.getElementById('chembody').style.marginLeft = '245px';
}
function closeChemNav() {
    document.getElementById('chemsidebar').style.width = "0";
    document.getElementById('main').style.marginLeft = "0";
    document.getElementById('chembody').style.marginLeft = '0';
}
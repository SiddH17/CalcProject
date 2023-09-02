window.onload = function()    {
    console.log("Inside the window onload function!!");

    // Resetting all dropdowns to default value 'Select'
    document.getElementById('eqsmtn').value = 'Select';
    document.getElementById('dispbtn').value = 'Select';
    document.getElementById('timebtn').value = 'Select';
    document.getElementById('initvelbtn').value = 'Select';
    document.getElementById('finvelbtn').value = 'Select';
    document.getElementById('accbtn').value = 'Select';
    document.getElementById('proj').value = 'Select';
    document.getElementById('rangebtn').value = 'Select';
    document.getElementById('heightbtn').value = 'Select';
    document.getElementById('tofbtn').value = 'Select';
    document.getElementById('horverbtn').value = 'Select';
    document.getElementById('projangbtn').value = 'Select';
    document.getElementById('projvelbtn').value = 'Select';
    document.getElementById('tadbtn').value = 'Select';
};
// setting selected Div tag to null for resetting dropdowns
var activeDiv = null;

// Equations of motion
// Showing methods to select for options
function showMethods(methodToShow)  {
    console.log("Entered showMethods function");
    var Displacement = document.getElementById('dispbtn');
    var Time = document.getElementById('timebtn');
    var header = document.getElementById('eqmtnid')
    var Initial_Velocity = document.getElementById('initvelbtn');
    var Final_Velocity = document.getElementById('finvelbtn');
    var Acceleration = document.getElementById('accbtn');

    console.log(methodToShow);
    if(methodToShow == 'Select')    {
        console.log("Selected Nothing");
    }
    else if(methodToShow == 'disp') {
        console.log(methodToShow);
        Displacement.value = 'Select';
        header.style.display = 'block';
        Displacement.style.display = 'block';
        Time.style.display = 'none';
        Initial_Velocity.style.display = 'none';
        Final_Velocity.style.display = 'none';
        Acceleration.style.display = 'none';
    }
    else if(methodToShow == 'time') {
        Time.value = 'Select';
        header.style.display = 'block';
        Time.style.display = 'block';
        Displacement.style.display = 'none';
        Initial_Velocity.style.display = 'none';
        Final_Velocity.style.display = 'none';
        Acceleration.style.display = 'none';
    }
    else if(methodToShow == 'initvel')  {
        Initial_Velocity.value = 'Select';
        header.style.display = 'block';
        Initial_Velocity.style.display = 'block';
        Displacement.style.display = 'none';
        Time.style.display = 'none';
        Final_Velocity.style.display = 'none';
        Acceleration.style.display = 'none';
    }
    else if(methodToShow == 'finvel')   {
        Final_Velocity.value = 'Select';
        header.style.display = 'block';
        Final_Velocity.style.display = 'block';
        Displacement.style.display = 'none';
        Time.style.display = 'none';
        Initial_Velocity.style.display = 'none';
        Acceleration.style.display = 'none';
    }
    else if(methodToShow == 'acc')  {
        Acceleration.value = 'Select';
        header.style.display = 'block';
        Acceleration.style.display = 'block';
        Displacement.style.display = 'none';
        Time.style.display = 'none';
        Initial_Velocity.style.display = 'none';
        Final_Velocity.style.display = 'none';
    }
}

// On changing to different methods of calculation
function methodChange(methodField, dropdownID)  {
    var submitButton = document.getElementById('kinSubmit');
    var answers = document.getElementById('eqmtnans');

    if(activeDiv!=null) {
        activeDiv.style.display = 'none';
        answers.innerHTML = "";
    }

    if(methodField == 'first')  {
        if(dropdownID == 'time')    {
            activeDiv = document.getElementById('firsttime');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'u')  {
            activeDiv = document.getElementById('firstinitvel');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'v')  {
            activeDiv = document.getElementById('firstfinvel');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'acc')  {
            activeDiv = document.getElementById('firstacc');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(methodField == 'second')    {
        if(dropdownID == 'disp')    {
            activeDiv = document.getElementById('seconddisp');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'time') {
            activeDiv = document.getElementById('secondtime');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'u') {
            activeDiv = document.getElementById('secondinitvel');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'acc') {
            activeDiv = document.getElementById('secondacc');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(methodField == 'third') {
        if(dropdownID == 'disp')    {
            activeDiv = document.getElementById('thirddisp');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'u')  {
            activeDiv = document.getElementById('thirdinitvel');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'v')  {
            activeDiv = document.getElementById('thirdfinvel');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(dropdownID == 'acc')  {
            activeDiv = document.getElementById('thirdacc');
            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(methodField == 'Select')    {
        console.log("Used Select Tag");
    }
}

// Projectile motion
// Methods to calculate for different variables selected
function projMethods(projShowMethod)    {
    console.log("Entered the projMethods function!!");
    var range = document.getElementById('rangebtn');
    var maxheight = document.getElementById('heightbtn');
    var tof = document.getElementById('tofbtn');
    var velcomps = document.getElementById('horverbtn');
    var projang = document.getElementById('projangbtn');
    var projinitvel = document.getElementById('projvelbtn');
    var tad = document.getElementById('tadbtn');
    var header = document.getElementById('projid');
    
    if(projShowMethod == 'Select')  {
        console.log("Nothing to see here, move on....");
    }
    else if(projShowMethod == 'range')  {
        header.style.display = 'block';
        range.value = 'Select';
        range.style.display = 'block';
        maxheight.style.display = 'none';
        tof.style.display = 'none';
        velcomps.style.display = 'none';
        projang.style.display = 'none';
        projinitvel.style.display = 'none';
        tad.style.display = 'none';
    }
    else if(projShowMethod == 'maxheight')  {
        header.style.display = 'block';
        maxheight.value = 'Select';
        maxheight.style.display = 'block';
        range.style.display = 'none';
        tof.style.display = 'none';
        velcomps.style.display = 'none';
        projang.style.display = 'none';
        projinitvel.style.display = 'none';
        tad.style.display = 'none';
    }
    else if(projShowMethod == 'tof')    {
        header.style.display = 'block';
        tof.value = 'Select';
        tof.style.display = 'block';
        range.style.display = 'none';
        maxheight.style.display = 'none';
        velcomps.style.display = 'none';
        projang.style.display = 'none';
        projinitvel.style.display = 'none';
        tad.style.display = 'none';
    }
    else if(projShowMethod == 'velcomps')   {
        header.style.display = 'block';
        velcomps.value = 'Select';
        velcomps.style.display = 'block';
        range.style.display = 'none';
        maxheight.style.display = 'none';
        tof.style.display = 'none';
        projang.style.display = 'none';
        projinitvel.style.display = 'none';
        tad.style.display = 'none';
    }
    else if(projShowMethod == 'projang')    {
        header.style.display = 'block';
        projang.value = 'Select';
        projang.style.display = 'block';
        range.style.display = 'none';
        maxheight.style.display = 'none';
        velcomps.style.display = 'none';
        tof.style.display = 'none';
        projinitvel.style.display = 'none';
        tad.style.display = 'none';
    }
    else if(projShowMethod == 'projinitvel')    {
        header.style.display = 'block';
        projinitvel.value = 'Select';
        projinitvel.style.display = 'block';
        range.style.display = 'none';
        maxheight.style.display = 'none';
        velcomps.style.display = 'none';
        projang.style.display = 'none';
        tof.style.display = 'none';
        tad.style.display = 'none';
    }
    else if(projShowMethod == 'tad')    {
        header.style.display = 'block';
        tad.value = 'Select';
        tad.style.display = 'block';
        range.style.display = 'none';
        maxheight.style.display = 'none';
        velcomps.style.display = 'none';
        projang.style.display = 'none';
        projinitvel.style.display = 'none';
        tof.style.display = 'none';
    }
}

// Changing between different methods for projectile motion
function ProjChange(projField, projDropdown)    {
    var projButton = document.getElementById('projSubmit');
    var answers = document.getElementById('eqmtnans');

    if(activeDiv!=null) {
        activeDiv.style.display = 'none';
        answers.innerHTML = "";
    }

    if(projField == 'first')    {
        if(projDropdown == 'tof')  {
            activeDiv = document.getElementById('fsttof');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        else if(projDropdown == 'projang')  {
            activeDiv = document.getElementById('fstprojang');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        else if(projDropdown == 'projinitvel')  {
            activeDiv = document.getElementById('fstprojinitvel');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'second')  {
        if(projDropdown == 'maxheight') {
            activeDiv = document.getElementById('secheight');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        else if(projDropdown == 'projang')  {
            activeDiv = document.getElementById('secprojang');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        else if(projDropdown == 'projinitvel')  {
            activeDiv = document.getElementById('secprojinitvel');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'third')   {
        if(projDropdown == 'range') {
            activeDiv = document.getElementById('trdrange');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        else if(projDropdown == 'projang')  {
            activeDiv = document.getElementById('trdprojang');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        else if(projDropdown == 'projinitvel')  {
            activeDiv = document.getElementById('trdprojinitvel');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'fourth')  {
        if(projDropdown == 'velcomps')  {
            activeDiv = document.getElementById('fourthhorver');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'fifth')   {
        if(projDropdown == 'velcomps')  {
            activeDiv = document.getElementById('fifthhorver');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'seventh') {
        if(projDropdown == 'projang')   {
            activeDiv = document.getElementById('seventhprojang');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'eighth')  {
        if(projDropdown == 'tad')   {
            activeDiv = document.getElementById('eigthtad');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'ninth')  {
        if(projDropdown == 'tad')   {
            console.log(projDropdown, "PRojectile function dropdown");
            activeDiv = document.getElementById('ninthtad');
            answers.style.display = 'block';
            projButton.style.display = 'block';
        }
        activeDiv.style.display = 'block';
    }
    else if(projField == 'Select')  {
        console.log('Used select tag');
    }
}
window.onload = function()    {
    // defining activeDiv variable for hiding previously active Divs
    var activeDiv = null;

    // Resetting all dropdowns to default value 'Select'
    document.getElementById('eqsmtn').value = 'Select';
    document.getElementById('dispbtn').value = 'Select';
    document.getElementById('timebtn').value = 'Select';
    document.getElementById('initvelbtn').value = 'Select';
    document.getElementById('finvelbtn').value = 'Select';
    document.getElementById('accbtn').value = 'Select';

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
        var answers1 = document.getElementById('eqmtnans1');
        var answers2 = document.getElementById('eqmtnans2');

        if(activeDiv!=null) {
            activeDiv.style.display = 'none';
            answers.innerHTML = answers1.innerHTML = answers2.innerHTML = "";
        }

        if(methodField == 'first')  {
            if(dropdownID == 'time')    {
                activeDiv = document.getElementById('firsttime');
            }
            else if(dropdownID == 'u')  {
                activeDiv = document.getElementById('firstinitvel');
            }
            else if(dropdownID == 'v')  {
                activeDiv = document.getElementById('firstfinvel');
            }
            else if(dropdownID == 'acc')  {
                activeDiv = document.getElementById('firstacc');
            }
            activeDiv.style.display = 'block';

            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(methodField == 'second')    {
            if(dropdownID == 'disp')    {
                activeDiv = document.getElementById('seconddisp');
                answers.style.display = 'none';
                answers1.style.display = 'block';
            }
            else if(dropdownID == 'time') {
                activeDiv = document.getElementById('secondtime');
            }
            else if(dropdownID == 'u') {
                activeDiv = document.getElementById('secondinitvel');
            }
            else if(dropdownID == 'acc') {
                activeDiv = document.getElementById('secondacc');
            }
            activeDiv.style.display = 'block';

            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(methodField == 'third') {
            if(dropdownID == 'disp')    {
                activeDiv = document.getElementById('thirddisp');
                answers.style.display = 'none';
                answers2.style.display = 'block';
            }
            else if(dropdownID == 'u')  {
                activeDiv = document.getElementById('thirdinitvel');
            }
            else if(dropdownID == 'v')  {
                activeDiv = document.getElementById('thirdfinvel');
            }
            else if(dropdownID == 'u')  {
                activeDiv = document.getElementById('thirdacc');
            }
            activeDiv.style.display = 'block';

            answers.style.display = 'block';
            submitButton.style.display = 'block';
        }
        else if(methodField == 'Select')    {
            console.log("Used Select Tag");
        }
    }

    // Projectile motion
    // Methods to calculate for different variables selected
    function projMethods(projShowMethod)    {
        var range = document.getElementById('range');
        var maxheight = document.getElementById('maxheight');
        var tof = document.getElementById('tof');
        var velcomps = document.getElementById('velcomps');
        var projang = document.getElementById('projang');
        var projinitvel = document.getElementById('projinitvel');
        var tad = document.getElementById('tad');
        
        if(projShowMethod == 'Select')  {
            console.log("Nothing to see here, move on....");
        }
        else if(projShowMethod == 'range')  {
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

        if(projField == 'first')    {
            if(projDropdown == 'tof')  {
                document.getElementById('t1').value = '';
                document.getElementById('fsttof').style.display = 'block';
                projButton.style.display = 'block';
            }
            else if(projDropdown == 'projang')  {
                document.getElementById('x1').value = '';
                document.getElementById('fstprojang').style.display = 'block';
                projButton.style.display = 'block';
            }
            else if(projDropdown == 'projinitvel')  {
                document.getElementById('u1').value = '';
                document.getElementById('fstprojinitvel').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'second')  {
            if(projDropdown == 'maxheight') {
                document.getElementById('h1').value = '';
                document.getElementById('secheight').style.display = 'block';
                projButton.style.display = 'block';
            }
            else if(projDropdown == 'projang')  {
                document.getElementById('x2').value = '';
                document.getElementById('secprojang').style.display = 'block';
                projButton.style.display = 'block';
            }
            else if(projDropdown == 'projinitvel')  {
                document.getElementById('u2').value = '';
                document.getElementById('secprojinitvel').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'third')   {
            if(projDropdown == 'range') {
                document.getElementById('r1').value = '';
                document.getElementById('trdrange').style.display = 'block';
                projButton.style.display = 'block';
            }
            else if(projDropdown == 'projang')  {
                document.getElementById('x3').value = '';
                document.getElementById('trdprojang').style.display = 'block';
                projButton.style.display = 'block';
            }
            else if(projDropdown == 'projinitvel')  {
                document.getElementById('u3').value = '';
                document.getElementById('trdprojinitvel').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'fourth')  {
            if(projDropdown == 'velcomps')  {
                document.getElementById('uc1').value = '';
                document.getElementById('fourthhorver').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'fifth')   {
            if(projDropdown == 'velcomps')  {
                document.getElementById('us1').value = '';
                document.getElementById('fifthhorver').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'seventh') {
            if(projDropdown == 'projang')   {
                document.getElementById('x7').value = '';
                document.getElementById('seventhprojang').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'eighth')  {
            if(projDropdown == 'tad')   {
                document.getElementById('ta1').value = '';
                document.getElementById('eighthtad').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
        else if(projField == 'ninth')  {
            if(projDropdown == 'tad')   {
                document.getElementById('td1').value = '';
                document.getElementById('ninthtad').style.display = 'block';
                projButton.style.display = 'block';
            }
        }
    }
};
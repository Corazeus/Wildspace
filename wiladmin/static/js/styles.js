/**Booking Form**/

var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form ...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    // ... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        $("#nextBtn").hide();
        $("#p_coins").show();
        $("#p_points").show();
        $.ajax({
            url: 'ajax/book',
            async: false,
            data: {
                'venue': venue,
                'description': $("#desc").val(),
                'purpose': $("#purpose option:selected").val(),
                'attendees': $("#ids").val(),
                'computers': $("#computers").val(),
                'starts': bookStarts.toString(),
                'ends': bookEnds.toString(),
                'hours_booked_timeslots_a': hours_booked_timeslots_a,
                'hours_booked_timeslots_b': hours_booked_timeslots_b,
                'hours_booked_timeslots_a_curr': hours_booked_timeslots_a_curr,
                'hours_booked_timeslots_b_curr': hours_booked_timeslots_b_curr,
            },
            dataType: 'json',
            success: function(data) {
                $("#fin_attendees tbody tr").remove(); 
                $("#fin_date tbody tr").remove(); 

                $("#fin_refNo").val(data.refNo);
                var all_names = $("#names").val();
                var names = all_names.split(",");
                for (let i = 0; i < names.length - 1; i++) {
                    $("#fin_attendees tbody").append("<tr><td>" + names[i] + "</td></tr>");
                }
                /*$("#fin_attendees").val($("#names").val());*/
                $("#fin_facilities").val(venue);
                var all_st = data.starts.toString();
                var all_ed = data.ends.toString();

                var st = all_st.split(",");
                var ed = all_ed.split(",");
                for(let i = 0; i < st.length; i++){

                    var start_date = new Date(st[i])
                    var end_date = new Date(ed[i])
                    var start_day = moment(start_date).format("YYYY-MM-DD").toString();
                    var start_time = moment(start_date).format("HH:mm").toString();
                    var end_day = moment(end_date).format("YYYY-MM-DD").toString();
                    var end_time = moment(end_date).format("HH:mm").toString();
                    var display_string = start_day + " " + start_time + " - ";
                    if(start_day != end_day){
                        display_string = display_string.concat(end_day);
                    }
                    display_string = display_string.concat(" ", end_time)

                    $("#fin_date tbody").append("<tr><td>" + display_string + "</td></tr>");
                }
                $("#fin_time").val(data.time);
                $("#fin_cost").val(data.cost);
            }
        });
    } else {
        $("#nextBtn").show();
        $("#p_coins").hide();
        $("#p_points").hide();
    }
    // ... and run a function that displays the correct step indicator:
    fixStepIndicator(n)
}

function showBookingAttendees(refNum){
    var attendees;
    $.ajax({
        'url': 'ajax/show_booking_attendees',
        async: false,
        data: {
            'refNum': refNum,
        },
        dataType: 'json',
        success: function(data) {
            attendees = data.attendees.split(",");
        },
    });
    return attendees;
}

function getBookingPurpose(refNum){
    var purpose;
    $.ajax({
        'url': 'ajax/show_booking_purpose',
        async: false,
        data: {
            'refNum': refNum,
        },
        dataType: 'json',
        success: function(data) {
            purpose = data.purpose;
        },
    });
    return purpose;
}
function deleteBooking(refNum, hoursBreak, hoursNonBreak){
    $.ajax({
        'url': 'ajax/delete_booking',
        async: false,
        data: {
            'delNum': refNum,
            'hoursBreak': hoursBreak,
            'hoursNonBreak': hoursNonBreak,
        },
        dataType: 'json',
        success: function(data) {
            alert("Cancelled booking: " + data.delNum);
        },
    });
}
function convertH2M(timeInHour){
    var timeParts = timeInHour.split(":");
    return Number(timeParts[0]) * 60 + Number(timeParts[1]);
}

function pay(method) {
    $.ajax({
        'url': 'ajax/pay_booking',
        'data': {
            'method': method,
        },
        success: function(data) {
            if (data.err == '') {
                alert("Booking successful!");
                $("#book").modal("hide");
                location.reload();
            } else {
                alert(data.err);
            }
        },
    });
}

function resetView() {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Hide the current tab:
    x[1].style.display = "none";
    x[2].style.display = "none";
    currentTab = 0;
    showTab(0);
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    if (currentTab + n + 1 === x.length) {
        console.log("Validity Check Active");
        var err = "";
        $.ajax({
            async: false,
            url: 'ajax/validity_check',
            data: {
                'venue': venue,
                'attendees': $("#ids").val(),
                'computers': $("#computers").val(),
                'starts': bookStarts.toString(),
                'ends': bookEnds.toString(),
            },
            success: function(data) { 
                err = data.err;
                console.log(err);
                $("#error").val(data.err);
            }
        });
        if (err == "") {
            currentTab = currentTab + n;
        }
        else {
            alert(err);
        }
        console.log("Check done");
    } 
    else if (currentTab === 0){
        if($("#desc").val() === ""){
            alert("Please enter a description.");
        }
        else{
            currentTab = currentTab + n;
        }
    }
    else {
        currentTab = currentTab + n;
    }
    // if you have reached the end of the form... :
    if (currentTab >= x.length) {
        //...the form gets submitted:
        // document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function checkIfValid() {
    console.log("VALIDITY CHECK ACTIVE");
    var err = "";
    return err;
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        console.log(y[i]);
        if (y[i].value == "" && y[i].required) {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false:
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class to the current step:
    x[n].className += " active";
}
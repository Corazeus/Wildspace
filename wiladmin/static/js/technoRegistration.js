$(document).ready(function(){

var current_fs, next_fs, previous_fs;

// No BACK button on first screen
if($(".show").hasClass("first-screen")) {
$(".prev").css({ 'display' : 'none' });
}

// Next button
/*$(".next-button1").click(function(){
    current_fs = $(this).parent().parent();
    next_fs = $(this).parent().parent().next();

    $(".prev").css({ 'display' : 'block' });

    $(current_fs).removeClass("show");
    $(next_fs).addClass("show");

    $("#progressbar li").eq($(".card2").index(next_fs)).addClass("active");

    current_fs.animate({}, {
        step: function() {

             current_fs.css({
                 'display': 'none',
                 'position': 'relative'
             });

             next_fs.css({
                 'display': 'block'
             });
        }
    });
});*/

$("#next-button1").click(function(){
    $("#step1").addClass("active");
    $("#second-screen").show();
    $("#first-screen").hide();
});

$("#next-button2").click(function(){
    $("#step2").addClass("active");
    $("#third-screen").show();
    $("#second-screen").hide();
});

$("#prev-button1").click(function(){
    $("#step1").removeClass("active");
    $("#first-screen").show();
    $("#second-screen").hide();
});

$("#prev-button2").click(function(){
    $("#step2").removeClass("active");
    $("#second-screen").show();
    $("#third-screen").hide();
});

// Previous button
/*$(".prev").click(function(){

    current_fs = $(".show");
    previous_fs = $(".show").prev();

    $(current_fs).removeClass("show");
    $(previous_fs).addClass("show");

    $(".prev").css({ 'display' : 'block' });

    if($(".show").hasClass("first-screen")) {
        $(".prev").css({ 'display' : 'none' });
    }

    $("#progressbar li").eq($(".card2").index(current_fs)).removeClass("active");

    current_fs.animate({}, {
        step: function() {
            current_fs.css({
                'display': 'none',
                'position': 'relative'
            });

            previous_fs.css({
                'display': 'block'
            });
        }
    });
});*/

});
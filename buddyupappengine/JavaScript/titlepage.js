$(document).ready(function(){


  $('#Signin').mouseenter(function(){
    $("#Signin").stop(true);
    $('#Signin').animate({"padding-top": "0.7%",
    'padding-bottom': '0.7%', "background-color": "black"}, {duration:420})
  });

  $('#Signin').mouseleave(function(){
    $("#Signin").stop(true);
    $('#Signin').css({"padding-top": "0%",
    'padding-bottom': '0%', "background-color": "#ffd700"})
  });



});

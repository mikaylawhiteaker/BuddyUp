$(document).ready(function(){


  $('#Signin').mouseenter(function(){
    $("#Signin").stop(true);
    $('#Signin').animate({"padding-top": "0.8%",
    'padding-bottom': '0.8%', "background-color": "black"}, {duration:420})
  });

  $('#Signin').mouseleave(function(){
    $("#Signin").stop(true);
    $('#Signin').css({"padding-top": "0%",
    'padding-bottom': '0%', "background-color": "#e5c100"})
  });



});

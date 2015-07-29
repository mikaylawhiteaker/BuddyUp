$(document).ready(function(){

  $("#logo").mouseenter(function(){
    $("#logo").css({"font-size": "20px", "color": "#00ff00"})
});

      $("#logo").mouseleave(function(){
        $("#logo").css({"font-size": "17px", "color":"white"})
      });

  $('#Create').mouseenter(function(){
    $('#Create').css({"padding-top": "5%",
    'padding-bottom': '5%',
    'padding-left': '7%',
    'padding-right': '7%'})
  });

  $('#Create').mouseleave(function(){
    $('#Create').css({"padding-top": "2%",
    'padding-bottom': '2%',
    'padding-left': '4%',
    'padding-right': '4%'})
  });

  $('#View').mouseenter(function(){
    $('#View').css({"padding-top": "5%",
    'padding-bottom': '5%',
    'padding-left': '7%',
    'padding-right': '7%'})
  });

  $('#View').mouseleave(function(){
    $('#View').css({"padding-top": "2%",
    'padding-bottom': '2%',
    'padding-left': '4%',
    'padding-right': '4%'})
  });
});

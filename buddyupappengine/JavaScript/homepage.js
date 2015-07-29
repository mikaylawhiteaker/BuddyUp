$(document).ready(function(){

  $("#logo").mouseenter(function(){
    $("#logo").css({"font-size": "20px", "color": "#FA1423"})
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

  $("#logout_url").mouseenter(function(){
    $("#logout_url").css({"font-size": "220%", "color": "#FA1423"})
  });

      $("#logout_url").mouseleave(function(){
        $("#logout_url").css({"font-size": "100%", "color": "white"})
      });
});

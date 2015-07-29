$(document).ready(function(){

  $("#logo").mouseenter(function(){
    $("#logo").css({"font-size": "150%", "color": "#FA1423"})
});

      $("#logo").mouseleave(function(){
        $("#logo").css({"font-size": "100%", "color":"white"})
      });

  $('#Create').mouseenter(function(){
    $("#Create").stop(true);
    $('#Create').animate({"padding-top": "5%",
    'padding-bottom': '5%',
    'padding-left': '7%',
    'padding-right': '7%'}, {duration: 800})
  });

  $('#Create').mouseleave(function(){
    $("#Create").stop(true);
    $('#Create').animate({"padding-top": "2%",
    'padding-bottom': '2%',
    'padding-left': '4%',
    'padding-right': '4%'}, {duration: 800})
  });

  $('#View').mouseenter(function(){
    $("#View").stop(true);
    $('#View').animate({"padding-top": "5%",
    'padding-bottom': '5%',
    'padding-left': '7%',
    'padding-right': '7%'}, {duration:800})
  });

  $('#View').mouseleave(function(){
    $("#View").stop(true);
    $('#View').animate({"padding-top": "2%",
    'padding-bottom': '2%',
    'padding-left': '4%',
    'padding-right': '4%'}, {duration:800})
  });

  $("#logout_url").mouseenter(function(){
    $("#logout_url").css({"font-size": "150%", "color": "#FA1423"})
  });

      $("#logout_url").mouseleave(function(){
        $("#logout_url").css({"font-size": "100%", "color": "white"})
      });

      $('#Buddies').mouseenter(function(){
        $("#Buddies").stop(true);
        $('#Buddies').animate({"padding-top": "5%",
        'padding-bottom': '5%',
        'padding-left': '7%',
        'padding-right': '7%'}, {duration: 800})
      });

      $('#Buddies').mouseleave(function(){
        $("#Buddies").stop(true);
        $('#Buddies').animate({"padding-top": "2%",
        'padding-bottom': '2%',
        'padding-left': '4%',
        'padding-right': '4%'}, {duration: 800})
      });
});

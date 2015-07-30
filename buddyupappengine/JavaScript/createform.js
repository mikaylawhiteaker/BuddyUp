$(document).ready(function(){

  $("#logo").mouseenter(function(){
    $("#logo").css({"font-size": "250%", "color": "#00ff00"})
});

      $("#logo").mouseleave(function(){
        $("#logo").css({"font-size": "140%", "color":"white"})
      });

  $("#logout_url").mouseenter(function(){
    $("#logout_url").css({"font-size": "250%", "color": "#00ff00"})
  });

      $("#logout_url").mouseleave(function(){
        $("#logout_url").css({"font-size": "140%", "color": "white"})
      });


      $(function() {
        var today = new Date().toISOString().split('T')[0];
        document.getElementsByName("date")[0].setAttribute('min', today);

        });




});
console.log("Hello");

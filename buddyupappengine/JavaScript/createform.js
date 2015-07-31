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

        $(function() {
          var defaultBounds= new google.maps.LatLngBounds(
            new google.maps.LatLng(37.77493, -122.41942),
            new google.maps.LatLng(40.71278, -74.00594));
            var input = document.getElementById('searchTextField');
            var options = {
              bounds: defaultBounds};

            var input = document.getElementById('pac-input');

            var autocomplete = new google.maps.places.Autocomplete(input, options
                );





          });






});
console.log("Hello");

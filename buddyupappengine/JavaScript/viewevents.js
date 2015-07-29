$(document).ready(function(){

  $("#logo").mouseenter(function(){
    $("#logo").css({"font-size": "150%", "color": "#FF0303"})
});

      $("#logo").mouseleave(function(){
        $("#logo").css({"font-size": "100%", "color":"white"})
      });

  $("#logout_url").mouseenter(function(){
    $("#logout_url").css({"font-size": "150%", "color": "#FF0303"})
  });

      $("#logout_url").mouseleave(function(){
        $("#logout_url").css({"font-size": "100%", "color": "white"})
      });


      $('#myform').submit(function() {
          var c = confirm("Are you sure?");
          return c; //you can just return c because it will be true or false
      });


});


// $(document).ready(function(){
//
// 	//Check to see if the window is top if not then display button
// 	$(window).scroll(function(){
// 		if ($(this).scrollTop() > 100) {
// 			$('.scrollToTop').fadeIn();
// 		} else {
// 			$('.scrollToTop').fadeOut();
// 		}
// 	});
//
// 	//Click event to scroll to top
// 	$('.scrollToTop').click(function(){
// 		$('html, body').animate({scrollTop : 0},800);
// 		return false;
// 	});
//
// });
// console.log("Hello");

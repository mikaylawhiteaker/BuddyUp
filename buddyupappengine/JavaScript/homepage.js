$('#Create').hover(
  // Mouse Over
  function(){
    $(this).animate({width: 75,height: 75}, 1000);
  },
  // Mouse Out
  function(){
      $(this).animate({width: 50,height: 50}, 1000);
});

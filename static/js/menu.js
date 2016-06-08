$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(500).fadeIn(0);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(500).fadeOut(0);
});

$(document).ready(function() {
  $(".home-link").click(function() {
    $('html,body').animate({scrollTop: $('#jumbo-header').offset().top - 80}, 1000, "easeInOutCubic");
  });
  $(".abstract-link").click(function() {
    $('html,body').animate({scrollTop: $('#abstract-header').offset().top - 80}, 1000, "easeInOutCubic");
  });
  $(".results-link").click(function() {
    $('html,body').animate({scrollTop: $('#results-header').offset().top - 80}, 1500, "easeInOutCubic");
  });
  $(".report-link").click(function() {
    $('html,body').animate({scrollTop: $('#report-header').offset().top - 80}, 1500, "easeInOutCubic");
  });
});

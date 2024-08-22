$(function () {
  function animateSkills() {
      $(".skill-progress span").each(function () {
          $(this).animate({
              'width': $(this).data("width")
          }, 1000);
      });
  }

  // Animate skills on initial page load
  animateSkills();

  // Re-animate skills when navigating back to the page or after form submission
  $(window).on('pageshow', function(event) {
      if (event.originalEvent.persisted) {
          animateSkills();
      }
  });
});
import jQuery from 'jquery'
const $ = jQuery
let LastScrollTop = 0

$(window).scroll(function (event) {
  var scroll = $(window).scrollTop()
  function fade () {
    if (scroll < LastScrollTop) {
      $('#site-header').fadeIn('slow').addClass('show')
      $('#site-footer').fadeOut('slow').removeClass('show')
      LastScrollTop = scroll
    } else if (scroll > LastScrollTop) {
      $('#site-header').fadeOut('slow').removeClass('show')
      $('#site-footer').fadeIn('slow').addClass('show')
      LastScrollTop = scroll
    }
    clearTimeout($.data(this, 'scrollTimer'))
    $.data(this, 'scrollTimer', setTimeout(function () {
      if ($('#site-header').is(':hover') || $('#site-footer').is(':hover')) {
        fade()
      } else {
        $('#site-header').fadeOut('slow')
        $('#site-footer').fadeOut('slow')
      }
    }, 2000))
  }
  fade()
})

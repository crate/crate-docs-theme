$(function() {
  var path = window.location.pathname;

  var scrollToSection = function(name) {
    var posTop = $('#'+name).offset().top;
    var offset = Math.max(posTop-60, 0);
    window.setTimeout(function(){
      $(window).scrollTop(offset);
    }, 100);
  };

  $('table').attr("border","0").addClass('table');
  $('.search').addClass('list-unstyled');
  $('.toctree ul').addClass('nav');
  $('.localtoc ul').addClass('nav');
  $('.toctree li a').click(function(e){
    var urlParts = this.href.split('#');
    if (urlParts[0].indexOf(path, urlParts[0].length-path.length) > -1 && urlParts.length == 2) {
      scrollToSection(urlParts[1]);
    }
  });

  $('body').scrollspy({
    'target': '.toctree',
    'offset': 101
  });

  (function(){
    var urlParts = window.location.hash.split('#');
    if (urlParts.length == 2) {
      scrollToSection(urlParts[1]);
    }
  }());

});

/**
 * This JS file is for additional new JS built over the existing theme
 * ...so as to avoid breaking anything unexpectedly
 */
(function ($) {
  function headerSize() {
    var doc = document.documentElement;
    var w = window;

    var curScroll;
    var prevScroll = w.scrollY || doc.scrollTop;
    var curDirection = 0;
    var prevDirection = 0;

    var header = document.getElementById("top");
    var toggled;
    var threshold = 200;

    var menuHeight = $("#top").outerHeight();
    var notifbarHeight = $(".notification-banner").outerHeight();
    var totalHeight = menuHeight + notifbarHeight;

    if ($("body.notif-bar-enabled")) {
      $(".notif-bar-enabled .body-container-wrapper").css(
        "padding-top",
        totalHeight + "px"
      );
      $(".notif-bar-enabled .w-canvas").css("padding-top", totalHeight + "px");
      $(".notif-bar-enabled header.header").css(
        "margin-top",
        notifbarHeight + "px"
      );
      $(".notif-bar-enabled header.header-nav").css(
        "margin-top",
        notifbarHeight + "px"
      );
    }

    var checkScroll = function () {
      curScroll = w.scrollY || doc.scrollTop;
      if (curScroll > prevScroll) {
        // scrolled down
        curDirection = 2;
      } else {
        //scrolled up
        curDirection = 1;
      }

      if (curDirection !== prevDirection) {
        toggled = toggleHeader();
      }

      prevScroll = curScroll;
      if (toggled) {
        prevDirection = curDirection;
      }
    };

    var toggleHeader = function () {
      toggled = true;
      promobar = document.getElementById("top");
      if (curDirection === 2 && curScroll > threshold) {
        //header.classList.add('disappear');
        if (promobar) {
          promobar.style.top = "-" + menuHeight + "px";
        }
      } else if (curDirection === 1) {
        //header.classList.remove('disappear');
        if (promobar) {
          document.getElementById("top").style.top = "0px";
        }
      } else {
        toggled = false;
      }
      return toggled;
    };

    window.addEventListener("scroll", checkScroll);
  }

  jQuery(function ($) {
    // Register for window resize
    $(window).resize(headerSize);
    // Do initial resize
    headerSize();
  });

  $(document).ready(function () {
    if (window.location.hash) {
      setTimeout(function checkHash() {
        var menuHeight = document.querySelector("#top").offsetHeight;
        document.getElementById("top").style.top = "-" + menuHeight + "px";
      }, 1000);
    }
  });

})(jQuery);

var Cookies = require('js-cookie');

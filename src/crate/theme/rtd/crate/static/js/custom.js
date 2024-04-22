/**
 * This JS file is for additional new JS built over the existing theme
 * ...so as to avoid breaking anything unexpectedly
 */
(function ($) {
  $(document).ready(function () {
    /**
     * Dropdown menu
     */
    var triggers = document.querySelectorAll(
      ".main-nav li.menu-item-has-children"
    );
    var background = document.querySelector(".dropdownBackground");
    var nav = document.querySelector(".main-nav");

    function handleEnter() {
      this.classList.add("trigger-enter");
      setTimeout(
        () =>
          this.classList.contains("trigger-enter") &&
          this.classList.add("trigger-enter-active"),
        150
      );
      background.classList.add("open");

      var dropdown = this.querySelector(".main-nav .sub-menu");
      var dropdownCoords = dropdown.getBoundingClientRect();
      var navCoords = nav.getBoundingClientRect();

      var coords = {
        height: dropdownCoords.height,
        width: dropdownCoords.width,
        top: dropdownCoords.top - navCoords.top + 5,
        left: dropdownCoords.left - navCoords.left,
      };

      background.style.setProperty("width", `${coords.width}px`);
      background.style.setProperty("height", `${coords.height}px`);
      background.style.setProperty(
        "transform",
        `translate(${coords.left}px, ${coords.top}px)`
      );
    }

    function handleLeave() {
      this.classList.remove("trigger-enter", "trigger-enter-active");
      background.classList.remove("open");
    }

    triggers.forEach((trigger) =>
      trigger.addEventListener("mouseenter", handleEnter)
    );
    triggers.forEach((trigger) =>
      trigger.addEventListener("mouseleave", handleLeave)
    );

    /**
     * Set height on sidebar
     */
    var viewportHeight = Math.max(
      document.documentElement.clientHeight,
      window.innerHeight || 0
    );
    var $sidebar = $(".bs-docs-sidebar");
    $sidebar.css("max-height", `${viewportHeight - 40}px`);
  });

  $(document).ready(function () {
    $("form#ratingForm").submit(function (e) {
      e.preventDefault(); // prevent the default click action from being performed
      if ($("#ratingForm :radio:checked").length == 0) {
        $("#ratingStatus").html("Select rating");
        return false;
      } else {
        $("#ratingStatus").html("Thank you for your feedback!");
        $("#ratingVote").prop("disabled", true);
        analytics.track(
          "Stars Rating: " + $("input:radio[name=rating]:checked").val()
        );
      }
    });
  });

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

jQuery(window).load(function() {
  jQuery(".status").fadeOut(),
    jQuery(".preloader")
      .delay(200)
      .fadeOut("slow");
}),
  $(document).ready(function() {
    $("#back-top").hide(),
      $(function() {
        $(window).scroll(function() {
          $(this).scrollTop() > 100
            ? $("#back-top").fadeIn()
            : $("#back-top").fadeOut();
        }),
          $("#back-top a").click(function() {
            return $("body,html").animate({ scrollTop: 0 }, 800), !1;
          });
      });
  }),
  !(function() {
    function e() {
      var e = !1;
      e && c("keydown", a), v.keyboardSupport && !e && u("keydown", a);
    }
    function t() {
      if (document.body) {
        var t = document.body,
          o = document.documentElement,
          n = window.innerHeight,
          a = t.scrollHeight;
        if (
          ((S = document.compatMode.indexOf("CSS") >= 0 ? o : t),
          (w = t),
          e(),
          (x = !0),
          top != self)
        )
          y = !0;
        else if (a > n && (t.offsetHeight <= n || o.offsetHeight <= n)) {
          var r = !1,
            i = function() {
              r ||
                o.scrollHeight == document.height ||
                ((r = !0),
                setTimeout(function() {
                  (o.style.height = document.height + "px"), (r = !1);
                }, 500));
            };
          if (
            ((o.style.height = "auto"), setTimeout(i, 10), S.offsetHeight <= n)
          ) {
            var l = document.createElement("div");
            (l.style.clear = "both"), t.appendChild(l);
          }
        }
        v.fixedBackground ||
          b ||
          ((t.style.backgroundAttachment = "scroll"),
          (o.style.backgroundAttachment = "scroll"));
      }
    }
    function o(e, t, o, n) {
      if ((n || (n = 1e3), d(t, o), 1 != v.accelerationMax)) {
        var a = +new Date(),
          r = a - C;
        if (r < v.accelerationDelta) {
          var i = (1 + 30 / r) / 2;
          i > 1 && ((i = Math.min(i, v.accelerationMax)), (t *= i), (o *= i));
        }
        C = +new Date();
      }
      if (
        (M.push({
          x: t,
          y: o,
          lastX: 0 > t ? 0.99 : -0.99,
          lastY: 0 > o ? 0.99 : -0.99,
          start: +new Date()
        }),
        !T)
      ) {
        var l = e === document.body,
          u = function() {
            for (var a = +new Date(), r = 0, i = 0, c = 0; c < M.length; c++) {
              var s = M[c],
                d = a - s.start,
                f = d >= v.animationTime,
                h = f ? 1 : d / v.animationTime;
              v.pulseAlgorithm && (h = m(h));
              var p = (s.x * h - s.lastX) >> 0,
                w = (s.y * h - s.lastY) >> 0;
              (r += p),
                (i += w),
                (s.lastX += p),
                (s.lastY += w),
                f && (M.splice(c, 1), c--);
            }
            l
              ? window.scrollBy(r, i)
              : (r && (e.scrollLeft += r), i && (e.scrollTop += i)),
              t || o || (M = []),
              M.length ? N(u, e, n / v.frameRate + 1) : (T = !1);
          };
        N(u, e, 0), (T = !0);
      }
    }
    function n(e) {
      x || t();
      var n = e.target,
        a = l(n);
      if (
        !a ||
        e.defaultPrevented ||
        s(w, "embed") ||
        (s(n, "embed") && /\.pdf/i.test(n.src))
      )
        return !0;
      var r = e.wheelDeltaX || 0,
        i = e.wheelDeltaY || 0;
      return (
        r || i || (i = e.wheelDelta || 0),
        !v.touchpadSupport && f(i)
          ? !0
          : (Math.abs(r) > 1.2 && (r *= v.stepSize / 120),
            Math.abs(i) > 1.2 && (i *= v.stepSize / 120),
            o(a, -r, -i),
            void e.preventDefault())
      );
    }
    function a(e) {
      var t = e.target,
        n =
          e.ctrlKey ||
          e.altKey ||
          e.metaKey ||
          (e.shiftKey && e.keyCode !== H.spacebar);
      if (
        /input|textarea|select|embed/i.test(t.nodeName) ||
        t.isContentEditable ||
        e.defaultPrevented ||
        n
      )
        return !0;
      if (s(t, "button") && e.keyCode === H.spacebar) return !0;
      var a,
        r = 0,
        i = 0,
        u = l(w),
        c = u.clientHeight;
      switch ((u == document.body && (c = window.innerHeight), e.keyCode)) {
        case H.up:
          i = -v.arrowScroll;
          break;
        case H.down:
          i = v.arrowScroll;
          break;
        case H.spacebar:
          (a = e.shiftKey ? 1 : -1), (i = -a * c * 0.9);
          break;
        case H.pageup:
          i = 0.9 * -c;
          break;
        case H.pagedown:
          i = 0.9 * c;
          break;
        case H.home:
          i = -u.scrollTop;
          break;
        case H.end:
          var d = u.scrollHeight - u.scrollTop - c;
          i = d > 0 ? d + 10 : 0;
          break;
        case H.left:
          r = -v.arrowScroll;
          break;
        case H.right:
          r = v.arrowScroll;
          break;
        default:
          return !0;
      }
      o(u, r, i), e.preventDefault();
    }
    function r(e) {
      w = e.target;
    }
    function i(e, t) {
      for (var o = e.length; o--; ) $[A(e[o])] = t;
      return t;
    }
    function l(e) {
      var t = [],
        o = S.scrollHeight;
      do {
        var n = $[A(e)];
        if (n) return i(t, n);
        if ((t.push(e), o === e.scrollHeight)) {
          if (!y || S.clientHeight + 10 < o) return i(t, document.body);
        } else if (
          e.clientHeight + 10 < e.scrollHeight &&
          ((overflow = getComputedStyle(e, "").getPropertyValue("overflow-y")),
          "scroll" === overflow || "auto" === overflow)
        )
          return i(t, e);
      } while ((e = e.parentNode));
    }
    function u(e, t, o) {
      window.addEventListener(e, t, o || !1);
    }
    function c(e, t, o) {
      window.removeEventListener(e, t, o || !1);
    }
    function s(e, t) {
      return (e.nodeName || "").toLowerCase() === t.toLowerCase();
    }
    function d(e, t) {
      (e = e > 0 ? 1 : -1),
        (t = t > 0 ? 1 : -1),
        (k.x !== e || k.y !== t) && ((k.x = e), (k.y = t), (M = []), (C = 0));
    }
    function f(e) {
      if (e) {
        (e = Math.abs(e)), D.push(e), D.shift(), clearTimeout(z);
        var t = D[0] == D[1] && D[1] == D[2],
          o = h(D[0], 120) && h(D[1], 120) && h(D[2], 120);
        return !(t || o);
      }
    }
    function h(e, t) {
      return Math.floor(e / t) == e / t;
    }
    function p(e) {
      var t, o, n;
      return (
        (e *= v.pulseScale),
        1 > e
          ? (t = e - (1 - Math.exp(-e)))
          : ((o = Math.exp(-1)),
            (e -= 1),
            (n = 1 - Math.exp(-e)),
            (t = o + n * (1 - o))),
        t * v.pulseNormalize
      );
    }
    function m(e) {
      return e >= 1
        ? 1
        : 0 >= e
        ? 0
        : (1 == v.pulseNormalize && (v.pulseNormalize /= p(1)), p(e));
    }
    var w,
      g = {
        frameRate: 150,
        animationTime: 800,
        stepSize: 120,
        pulseAlgorithm: !0,
        pulseScale: 8,
        pulseNormalize: 1,
        accelerationDelta: 20,
        accelerationMax: 1,
        keyboardSupport: !0,
        arrowScroll: 50,
        touchpadSupport: !0,
        fixedBackground: !0,
        excluded: ""
      },
      v = g,
      b = !1,
      y = !1,
      k = { x: 0, y: 0 },
      x = !1,
      S = document.documentElement,
      D = [120, 120, 120],
      H = {
        left: 37,
        up: 38,
        right: 39,
        down: 40,
        spacebar: 32,
        pageup: 33,
        pagedown: 34,
        end: 35,
        home: 36
      },
      v = g,
      M = [],
      T = !1,
      C = +new Date(),
      $ = {};
    setInterval(function() {
      $ = {};
    }, 1e4);
    var z,
      A = (function() {
        var e = 0;
        return function(t) {
          return t.uniqueID || (t.uniqueID = e++);
        };
      })(),
      N = (function() {
        return (
          window.requestAnimationFrame ||
          window.webkitRequestAnimationFrame ||
          function(e, t, o) {
            window.setTimeout(e, o || 1e3 / 60);
          }
        );
      })(),
      E = /chrome/i.test(window.navigator.userAgent),
      K = "onmousewheel" in document;
    K && E && (u("mousedown", r), u("mousewheel", n), u("load", t));
  })();
!(function() {
  "use strict";
  if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
    var e = document.createElement("style");
    e.appendChild(
      document.createTextNode("@-ms-viewport{width:auto!important}")
    ),
      document.querySelector("head").appendChild(e);
  }
})();

var element_position = $(".nav li").offset().top;

var element_position = $(".nav li").offset().top;

//$("#MenuUl li").eq(0).addClass('active');
//console.log(element_position);
$(window).scroll(function() {
  var scroll = $(window).scrollTop();
  if (scroll <= 450) {
    $("#MenuUl li")
      .eq(0)
      .addClass("active");
  }
});

$("#dropdown-first").click(function() {
  $(".sticky-nav").addClass("pos-class");
});

$("a.topopup").click(function() {
  //loading(); // loading
  setTimeout(function() {
    // then show popup, deley in .5 second
    loadPopup(); // function show popup
  }, 200); // .2 second
  return false;
});

$("a.close").click(function() {
  disablePopup(); // function close pop up
});

// $(this).keyup(function(event) {
// if (event.which == 27) { // 27 is 'Ecs' in the keyboard
// disablePopup();  // function close pop up
// }
// });
/************** start: functions. **************/
function loading() {
  $("div.loader").show();
}

function closeloading() {
  $("div.loader").fadeOut("normal");
}

var popupStatus = 0; // set value

function loadPopup() {
  if (popupStatus == 0) {
    // if value is 0, show popup
    closeloading(); // fadeout loading
    $("#toPopup").fadeIn(0500); // fadein popup div
    $("#backgroundPopup").css("opacity", "0.7"); // css opacity, supports IE7, IE8
    $("#backgroundPopup").fadeIn(0001);
    popupStatus = 1; // and set value to 1
  }
}

function disablePopup() {
  if (popupStatus == 1) {
    // if value is 1, close popup
    $("#toPopup").fadeOut("normal");
    $("#backgroundPopup").fadeOut("normal");
    popupStatus = 0; // and set value to 0
  }
}

//var city_popup = false;

// var now = new Date();
// var time = now.getTime();
// time += 3600 * 1000;
// now.setTime(time);

var date = new Date();
date.setTime(date.getTime() + 60 * 60 * 1000);

//if(Cookies.get('city_popup') != 'cityname'){
//console.log(Cookies.get());
//	$(function(){
//		$('a[onload]').trigger('onload');
//	});
//	Cookies.set('city_popup', 'cityname',{expires: null }, { path: 'https://www.sporloc.com/' });
//}

// window.onbeforeunload = function() {
// $.cookie("city_popup", null);
// };

$(document).ready(function() {
  //loadPopup();
  $(".navbar-nav li.dropdown").click(function() {
    $(this).hasClass("fgdfgdf")
      ? ($(".fgdfgdf").removeClass("fgdfgdf"), $(".drdp-bg").remove())
      : ($(".fgdfgdf").removeClass("fgdfgdf"),
        $(this).addClass("fgdfgdf"),
        $("div.drdp-bg").remove(),
        $(".navbar-wrapper").after($('<div class="drdp-bg"> </div>'))),
      clickon();
  });
});

function clickon() {
  $(".drdp-bg,.testimonial,.inner-top-image,.inner-bred-menu").on(
    "click",
    function() {
      $(".fgdfgdf").removeClass("fgdfgdf"), $(".drdp-bg").remove();
    }
  );
}

$(
  "a.video-topopup, a.topopup, .testimonial-fixed-floating-icon-13aug, a.vdi-popup"
).click(function() {
  if (
    navigator.userAgent.match(
      /(iPhone|iPod|iPad|android|iemobile|Trident|msie|webOS|Windows Phone|BlackBerry)/i
    )
  ) {
    $("html, body").animate({ scrollTop: $("body").offset().top }, "fast");
  }
});

$(function() {
  $("div.inner-bred-menu a[href*=#],#industries-we-serve a[href*=#]").click(
    function() {
      if (
        location.pathname.replace(/^\//, "") ==
          this.pathname.replace(/^\//, "") &&
        location.hostname == this.hostname
      ) {
        var $target = $(this.hash);
        $target =
          ($target.length && $target) || $("[name=" + this.hash.slice(1) + "]");
        if ($target.length) {
          var targetOffset = $target.offset().top;
          $("html,body").animate({ scrollTop: targetOffset - 120 }, 1000);
          return false;
        }
      }
    }
  );
});

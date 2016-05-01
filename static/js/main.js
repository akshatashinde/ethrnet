

//Roof Social Icons Tooltip
$('.social-link').tooltip();

// Page Loader
$(window).load(function() {
  "use strict";
  $('#loader').fadeOut();
});
/*----------------------------------------------------*/
/*	Slick Nav 
/*----------------------------------------------------*/
$('.wpb-mobile-menu').slicknav({
  prependTo: '.navbar-header',
  parentTag: 'liner',
  allowParentLinks: true,
  duplicate: true,
  label: '',
  closedSymbol: '<i class="fa fa-angle-right"></i>',
  openedSymbol: '<i class="fa fa-angle-down"></i>',
});

//Search
  /*-------------------------------------------------*/
  /* =  search toogle
  /*-------------------------------------------------*/

  var openSearch = $('.open-search'),
    SearchForm = $('.full-search'),
    closeSearch = $('.close-search');

    openSearch.on('click', function(event){
      event.preventDefault();
      if (!SearchForm.hasClass('active')) {
        SearchForm.fadeIn(300, function(){
          SearchForm.addClass('active');
        });
      }
    });

    closeSearch.on('click', function(event){
      event.preventDefault();

      SearchForm.fadeOut(300, function(){
        SearchForm.removeClass('active');
        $(this).find('input').val('');
      });
    });


//WOW Scroll Spy
var wow = new WOW({
    //disabled for mobile
    mobile: false
});
wow.init();


//Owl Carousel
$('#clients-scroller').owlCarousel({
    items:4,
    itemsTablet:3,
    margin:90,
    stagePadding:90,
    smartSpeed:450,
    itemsDesktop : [1199,4],
    itemsDesktopSmall : [980,3],
    itemsTablet: [768,3],
    itemsTablet: [767,2],
    itemsTabletSmall: [480,2],
    itemsMobile : [479,1],
});

 //About owl carousel Slider
  $(document).ready(function(){
    /*=== About us ====*/
    $('#carousel-about-us').owlCarousel({   
        navigation: true, // Show next and prev buttons
        navigationText : ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
        slideSpeed: 800,
        paginationSpeed: 400,
        autoPlay: true,
        singleItem: true,
        pagination : false,
        items : 1,
        itemsCustom : false,
        itemsDesktop : [1199,4],
        itemsDesktopSmall : [980,3],
        itemsTablet: [768,2],
        itemsTabletSmall: false,
        itemsMobile : [479,1],
    });

});
  //About owl carousel Slider
  $(document).ready(function(){
    /*=== About us ====*/
    $('#carousel-full').owlCarousel({   
          navigation: true, // Show next and prev buttons
          navigationText : ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
          slideSpeed: 800,
          paginationSpeed: 400,
          autoPlay: true,
          singleItem: true,
          pagination : false,
          items : 1,
          itemsCustom : false,
          itemsDesktop : [1199,4],
          itemsDesktopSmall : [980,3],
          itemsTablet: [768,2],
          itemsTabletSmall: false,
          itemsMobile : [479,1],
      });

  });
  //About owl carousel Slider
  $(document).ready(function(){
    /*=== About us ====*/
    $('#carousel-text').owlCarousel({   
        navigation: false, // Show next and prev buttons
        slideSpeed: 800,
        paginationSpeed: 400,
        autoPlay: true,
        singleItem: true,
        pagination : true,
        items : 1,
        itemsCustom : false,
        itemsDesktop : [1199,4],
        itemsDesktopSmall : [980,3],
        itemsTablet: [768,2],
        itemsTabletSmall: false,
        itemsMobile : [479,1],
    });

});

//Tab
$(document).ready(function() {
    $("div.tab-menu>div.list-group>a").click(function(e) {
        e.preventDefault();
        $(this).siblings('a.active').removeClass("active");
        $(this).addClass("active");
        var index = $(this).index();
        $("div.tab>div.tab-content").removeClass("active");
        $("div.tab>div.tab-content").eq(index).addClass("active");
    });
});

//Bootsrap slider carousel
$('#carousel-slider').carousel();

$('a[data-slide="prev"]').click(function () {
    $('#carousel-slider').carousel('prev');
});

$('a[data-slide="next"]').click(function () {
    $('#carousel-slider').carousel('next');
});

//MixitUp
$(function(){
  $('#portfolio-items').mixItUp();
});

// Testimonial
$('testimonial-carousel').carousel();
$('a[data-slide="prev"]').click(function () {
    $('#testimonial-carousel').carousel('prev');
});

$('a[data-slide="next"]').click(function () {
    $('#testimonial-carousel').carousel('next');
});


//CounterUp
    jQuery(document).ready(function( $ ) {
        $('.counter').counterUp({
            delay: 1,
            time: 800
        });
    });


//Dropdown Menus
$(".dropdown").hover(
  function () {
    $(this).addClass('open');
  }, 
  function () {
    $(this).removeClass('open');
  }
  );


// Testimonial
$('carousel-about-us').carousel();
$('a[data-slide="prev"]').click(function () {
    $('#carousel-about-us').carousel('prev');
});

$('a[data-slide="next"]').click(function () {
    $('#carousel-about-us').carousel('next');
});

// Styles Switcher JS
function setActiveStyleSheet(title) {
  var i, a, main;
  for (i = 0;
    (a = document.getElementsByTagName("link")[i]); i++) {
    if (a.getAttribute("rel").indexOf("style") != -1 && a.getAttribute("title")) {
      a.disabled = true;
      if (a.getAttribute("title") == title) a.disabled = false;
    }
  }
}

function getActiveStyleSheet() {
  var i, a;
  for (i = 0;
    (a = document.getElementsByTagName("link")[i]); i++) {
    if (a.getAttribute("rel").indexOf("style") != -1 && a.getAttribute("title") && !a.disabled) return a.getAttribute("title");
  }
  return null;
}

function getPreferredStyleSheet() {
  var i, a;
  for (i = 0;
    (a = document.getElementsByTagName("link")[i]); i++) {
    if (a.getAttribute("rel").indexOf("style") != -1 && a.getAttribute("rel").indexOf("alt") == -1 && a.getAttribute("title")) return a.getAttribute("title");
  }
  return null;
}

function createCookie(name, value, days) {
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    var expires = "; expires=" + date.toGMTString();
  } else expires = "";
  document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}
window.onload = function(e) {
  var cookie = readCookie("style");
  var title = cookie ? cookie : getPreferredStyleSheet();
  setActiveStyleSheet(title);
}
window.onunload = function(e) {
  var title = getActiveStyleSheet();
  createCookie("style", title, 365);
}
var cookie = readCookie("style");
var title = cookie ? cookie : getPreferredStyleSheet();
setActiveStyleSheet(title);

// Styles Switcher
$(document).ready(function() {
  $('.open-switcher').click(function() {
    if ($(this).hasClass('show-switcher')) {
      $('.switcher-box').css({
        'left': 0
      });
      $('.open-switcher').removeClass('show-switcher');
      $('.open-switcher').addClass('hide-switcher');
    } else if (jQuery(this).hasClass('hide-switcher')) {
      $('.switcher-box').css({
        'left': '-140px'
      });
      $('.open-switcher').removeClass('hide-switcher');
      $('.open-switcher').addClass('show-switcher');
    }
  });
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$('#id_area').blur(function(){
    console.log('blur');

//    a = $(this).parent().siblings();
//    c = $('>.prices', a[3]);
//    c.val(10);

    get_plan_list($(this).val(), this);
});

function get_plan_list(branch_id, obj) {
    console.log(branch_id)
    var options = "";
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url : "/plan/get/list/", // the endpoint
        type : "POST", // http method
        beforeSend: function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data : {
            area : branch_id,
         }, // data sent with the post request
        // handle a successful response
        success : function(response) {
                console.log(response)
                $('#id_plan').empty();
                $.each( response, function( key, value ) {
                    options = options + '<option value="' + key + '">' + value + '</option>'
                 });
                 $('#id_plan').append(options);
        },
        error: function(response) {

                $.toaster({ priority : 'danger', title : 'Error', message : 'Select valid Plan or Device or keep it blank.'});
            },
        // handle a non-successful response
    });
};
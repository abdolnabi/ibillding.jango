AOS.init();


// ------------ Header ------------
  $(function () {
    $(window).scroll(function () {
      var scroll = $(window).scrollTop();
      if (scroll >= 200) {
        $("#header").addClass('smaller');
      } else {
        $("#header").removeClass("smaller");
      }
    });
  });


// ------------ Sidr Mobile -----------------
$(document).ready(function(){
  $(".openMobSide").click(function(){
    $("body").toggleClass("open_menu");
  });
});


// ------------ Menu -----------------

  $(document).ready(function () {
    $(document).on("scroll", onScroll);
    
    //smoothscroll
    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        $(document).off("scroll");
        
        $('a').each(function () {
            $(this).removeClass('active');
        })
        $(this).addClass('active');
      
        var target = this.hash,
            menu = target;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top+2
        }, 500, 'swing', function () {
            window.location.hash = target;
            $(document).on("scroll", onScroll);
        });
    });
});

function onScroll(event){
    var scrollPos = $(document).scrollTop();
    $('.nav a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('.nav li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });
}

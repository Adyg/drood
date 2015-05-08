(function($){
    var $navigation = $('nav.navigation'),
        $navigationTrigger = $('header a.menu-trigger');

    $navigationTrigger.on('click', function(e) {
        e.preventDefault();
        $navigation.toggleClass('navigation-active');
    });

})(jQuery);
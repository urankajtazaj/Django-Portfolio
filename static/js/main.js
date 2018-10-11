var content = $(".tab");
var tab = $(".icons img");

tab.each(function(i, el) {
    var e = $(el);

    e.click(function() {
        $(content).addClass("hide");
        $(content[i]).removeClass("hide");

        tab.removeClass("active");
        $(this).addClass("active");

        $(".side.right").scrollTop(0)
    });
});
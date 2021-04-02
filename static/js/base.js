$(document).ready(function () {

    // Enables sort selection box to function
    $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    })

    // Copyright date will be automatically updated every year without user input.
    $("#copyright").text(new Date().getFullYear());

    // When 'To Top Button' is clicked: Scroll to top of page in 800ms.
    $("a[href='#top']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 800);
        return false;
    });

    // If position of vertical scroll is above 200px, to top button will disappear.
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.to-top').fadeIn();
        } else {
            $('.to-top').fadeOut();
        }
    });

    // Hide toast messages after set period
    $(document).ready(function () {
        setTimeout(function () {
            $('.toast').hide('fade');
        }, 5000)
    });
})
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

    // Disable -/+ buttons outside 1-99 range
    function manageEnableDisable(itemId) {
        var currValue = parseInt($(`#id_qty_${itemId}`).val());
        var removeDisabled = currValue < 2;
        var addDisabled = currValue > 98;
        $(`#dec-quantity_${itemId}`).prop('disabled', removeDisabled);
        $(`#inc-quantity_${itemId}`).prop('disabled', addDisabled);
    }

    // Make sure proper enabling/disabling of inputs on page load
    var allQuantityInputs = $('.qty_input');
    for(var i = 0; i < allQuantityInputs.length; i++){
        var itemId = $(allQuantityInputs[i]).data('item_id');
        manageEnableDisable(itemId);
    }

    // Check enable/disable every time input changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        manageEnableDisable(itemId);
    });

    // Increment quantity of flowers
    $('.inc-quantity').click(function(e) {
       e.preventDefault();
       var closeInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currValue = parseInt($(closeInput).val());
       $(closeInput).val(currValue + 1);
       var itemId = $(this).data('item_id');
       manageEnableDisable(itemId);
    });

    // Decrement quantity of flowers
    $('.dec-quantity').click(function(e) {
       e.preventDefault();
       var closeInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currValue = parseInt($(closeInput).val());
       $(closeInput).val(currValue - 1);
       var itemId = $(this).data('item_id');
       manageEnableDisable(itemId);
    });
})

$('document').ready(
    function() {
    $("#search-input").keyup(function (e) { 
        $("#btn-search").removeAttr("disabled");
    });

});

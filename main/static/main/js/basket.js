$("document").ready(
    function () {
    $(".btn-plus").click(function (e) { 
        var id= $(this).attr("pid").toString();
        console.log('pid',id);
        var count = $(this).parent().find(".basket-count");
        
        $.ajax({
            type: "GET",
            url: "/plusbasket",
            data: {
                "prod_id" : id
            },
            dataType: "json",
            success: function (data) {
                count.text(data['quantity']);
                $("#totalamount").text(data['totalamount']);
                
            }
        });
    });

    $(".btn-minus").click(function (e) { 
        var id= $(this).attr("pid").toString();
        console.log('pid',id);
        var count = $(this).parent().find(".basket-count");
        $.ajax({
            type: "GET",
            url: "/minusbasket",
            data: {
                "prod_id" : id
            },
            dataType: "json",
            success: function (data) {
                count.text(data['quantity']);
                $("#totalamount").text(data['totalamount']);
            }
        });
    });


    $(".basket-delete-link").click(function (e) { 
        var id= $(this).attr("pid").toString();
        var cart = $(this).parent();
        $.ajax({
            type: "GET",
            url: "/deletebasket",
            data: {
                "prod_id" : id
            },
            dataType: "json",
            success: function (data) {
                cart.parent().find(".line-top").remove()
                cart.remove();
                $("#totalamount").text(data['totalamount']);
                $(".badge").text(data['cart_count'])
                
            }
        });
    });
});
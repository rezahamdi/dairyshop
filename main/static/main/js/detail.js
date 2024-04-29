$("document").ready(
  function () {
    $("#detail-add-btn").click(function (e) { 
      var id= $(this).attr("pid").toString();
      
      $.ajax({
          type: "GET",
          url: "/addtobasket",
          data: {
              "prod_id" : id
          },
          dataType: "json",
          success: function (data) {
            var btn_quantity =  data['quantity'] +" "+ "عدد"
            $(".detail-quantity").text(btn_quantity)
            $(".badge").text(data['cart_count'])
          }
      });
  });
});
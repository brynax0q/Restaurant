
// 预约
$('.click-order .order_submit').on('click',function(){
  var name = $.trim($('#order-item-name').val());
  var phone = $.trim($('#order-item-phone').val());
  var num = $.trim($('#order-item-num option:selected').val());
  var day = $.trim($('#order-day-time').val());
  var arrival = $('#order-item-arrival-tiem option:selected').text();
  var time = $.trim($('#order-item-leave-time option:selected').text());
  var table = $.trim($('#order-item-table option:selected').val());
  $.ajax({
        cache: false,
        type: "POST",
        url: "../reservation/",
        data:{'name': name ,
              'phone':phone,
            'num':num,
            'day':day,
            'arrival':arrival,
            'time':time,
            'table':table
        },
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
            success:function (res) {
                if(res.status == 1)
                {
                  window.confirm(res.msg);
                  window.location = window.location="../index?date=" + res.day;
                }
                else if(res.status == 0)
                  window.confirm(res.msg);
            }
    });
  $('.click-order').css('visibility','hidden');
});

// 取消预约
$('.click-cancel .cancel_submit').on('click',function(){
    var name = $.trim($('#cancel-item-name').val());
    var day = $.trim($('#cancel-item-day').val());
  $.ajax({
        cache: false,
        type: "POST",
        url: "../cancel_reservation/",
        data:{'name': name ,
              'day':day
        },
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
            success:function (res) {
              if(res.status == 0)
                window.confirm(res.msg);
              else if(res.status == 2)
                window.confirm(res.msg);
                else if(res.status == 1){
                  window.confirm(res.msg);
                  window.location = window.location="../index?date=" + res.day;
              }

            }
    });

  $('.click-cancel').css('visibility','hidden');
});

// 换桌
$('.click-change .change_submit').on('click',function(){
   var name = $.trim($('#change-item-name').val());
   var day = $.trim($('#chage-item-new-day').val());
    var new_table = $.trim($('#chage-item-new-table option:selected').val());
  $.ajax({
        cache: false,
        type: "POST",
        url: "../change_table/",
        data:{'name': name ,
            'day':day,
            'new_table':new_table
        },
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
            success:function (res) {
              if(res.status == 2)
                window.confirm(res.msg);
                else if(res.status == 1){
                  window.confirm(res.msg);
                  window.location = window.location="../index?date=" + res.day;

              }

            }
    });

  $('.click-change').css('visibility','hidden');
});

// 就餐
$('.click-dinner .dinner_submit').on('click',function(){
  var name = $.trim($('#dinner-item-name').val());
  var phone = $.trim($('#dinner-item-phone').val());
  var num = $.trim($('#dinner-item-num option:selected').val());
  var arrival = $.trim($('#dinner-item-arrival-tiem option:selected').val());
  var time = $.trim($('#dinner-item-leave-time option:selected').val());
  var table = $.trim($('#dinner-item-table option:selected').val());
  $.ajax({
        cache: false,
        type: "POST",
        url: "../walk_in/",
        data:{'name': name ,
              'phone':phone,
              'num':num,
              'arrival':arrival,
              'time':time,
            'table':table
        },
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
            success:function (res) {
                if(res.status == 1)
                {
                  window.confirm(res.msg);
                  window.location="../index?date=" + res.day;
                }
                else if(res.status == 0)
                  window.confirm(res.msg);
            }
    });

  $('.click-dinner').css('visibility','hidden');
});


$('.order').on('click',function(){
  $('.click-order').css('visibility','visible');
});


$('.click-order .abandon').on('click',function(){
  $('.click-order').css('visibility','hidden');
});

$('.cancel-order').on('click',function(){
  $('.click-cancel').css('visibility','visible');
});
$('.click-cancel .abandon').on('click',function(){
  $('.click-cancel').css('visibility','hidden');
});

$('.change').on('click',function(){
  $('.click-change').css('visibility','visible');
});

$('.click-change .abandon').on('click',function(){
  $('.click-change').css('visibility','hidden');
});

$('.eat').on('click',function(){
  $('.click-dinner').css('visibility','visible');
});

$('.click-dinner .abandon').on('click',function(){
  $('.click-dinner').css('visibility','hidden');
});







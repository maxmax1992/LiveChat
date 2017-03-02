// Note that the path doesn't matter right now; any WebSocket
// connection gets bumped over to WebSocket consumers

$('document').ready(function () {
    $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
    // window.location.pathname
    // Note that the path doesn't matter right now; any WebSocket
    // connection gets bumped over to WebSocket consumers
    socket = new ReconnectingWebSocket("ws://" + window.location.host + window.location.pathname);
    console.log("ws://" + window.location.host + window.location.pathname);
    socket.onmessage = function (e) {


        var user = $("#user").val();
        var msgUser = JSON.parse(e.data);

        if(msgUser.message !== '') {
            if (user === msgUser.username) {
                var $div = $(".templateMSG").clone().removeClass("templateMSG");
                var text = msgUser.message;
                var d = new Date();

                var month = d.getMonth() + 1;
                var day = d.getDate();
                $div.append("<span style='color: black; font-size: 20px'>" + user + " </span>" + "<span>" + " " + formatDate(d) + "</span>" + "<br><br>" + text);

                $(".Content").append($div);
                $div.fadeIn(0);
                $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);


            } else {


                var $div = $(".templateMSG2").clone().removeClass("templateMSG2");
                var text = msgUser.message;
                var d = new Date();

                var month = d.getMonth() + 1;
                var day = d.getDate();
                $div.append("<span style='color: black; font-size: 20px'>" + user + " </span>" + "<span>" + " " + formatDate(d) + "</span>" + "<br><br>" + text);
                // var div = $('<div>').addClass("panel panel-default").css({
                //     'background-color': 'lightblue',
                //     'text-align': 'right',
                // });
                //

                //
                //
                // var text = msgUser.message;
                // div.append("<p>" + text + "   " + formatDate(d) + "</p>");
                $(".Content").append($div);
                $div.fadeIn(0);
                $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);

                //
                // var d = new Date();
                //
                // var month = d.getMonth() + 1;
                // var day = d.getDate();
                //
                //
                // var text = msgUser.message;
                // div.append("<p>" + text + "   " + formatDate(d) + "</p>");
                // $(".Content").append(div);
                // $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
                // console.log("not a same user")
            }
            $('#msg').val('');
        }

    }
    socket.onopen = function () {
        $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
    }
    if (socket.readyState == WebSocket.OPEN) socket.onopen();

    $("#chatform").submit(function(event) {
        sendEvent(event);
    });
    $("#go").click(function(event) {
        sendEvent(event);
    });

    function sendEvent(event) {
        $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
        var data = {
            'username': $("#user").val(),
            'message': $("#msg").val()
        }
        // socket.send(data.str);
        socket.send(JSON.stringify(data));

        event.preventDefault();
    }

});

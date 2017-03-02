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

        if (user === msgUser.username) {
            var div = $('<div>').addClass("panel panel-default").css({
                'background-color': 'lightblue',
                'text-align': 'right',
            });

            var d = new Date();

            var month = d.getMonth() + 1;
            var day = d.getDate();


            var text = msgUser.message;
            div.append("<p>" + text + "   " + formatDate(d) + "</p>");
            $(".Content").append(div);
            $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);


        } else {

            var d = new Date();

            var month = d.getMonth() + 1;
            var day = d.getDate();


            var text = msgUser.message;
            div.append("<p>" + text + "   " + formatDate(d) + "</p>");
            $(".Content").append(div);
            $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
            console.log("not a same user")
        }
    }
    socket.onopen = function () {
        // socket.send("hello world");
    }
    if (socket.readyState == WebSocket.OPEN) socket.onopen();


    //sends to consumers the text with attribute 'Text' the shit.
    $("#chatform").submit(function (event) {

        $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
        var data = {
            'username': $("#user").val(),
            'message': $("#msg").val()
        }
        // socket.send(data.str);
        socket.send(JSON.stringify(data));

        event.preventDefault();
    });

});

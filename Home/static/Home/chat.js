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
        alert(e.data);

        var user = $("#user").val();
        var msgUser = JSON.parse(e.data);


        //if user == msgUser create div with text to the left
        //append div to a $('#hatWidnow') div with a chat bubble to a left
        // console.log(user + "," + msgUser.username);
        if (user === msgUser.username) {

            console.log('same user');
        } else {
            //append div to a $('#hatWidnow') div with a chat bubble to a right

            console.log("not a same user")
        }


        // $("textarea").append("\n" + e.data);
    }
    socket.onopen = function () {
        // socket.send("hello world");
    }
    // Call onopen directly if socket is already open
    if (socket.readyState == WebSocket.OPEN) socket.onopen();


    //sends to consumers the text with attribute 'Text' the shit.
    $("#chatform").submit(function (event) {
        // console.log($("#chatform input").val());
        // var titles = [];
        // $('input[name^=titles]').each(function(){
        //     titles.push($(this).val());
        // });
        // data = {
        //     "str": $("#chatform #text").val().toString();
        //
        // };
            $('#chatWindow').scrollTop($('#chatWindow')[0].scrollHeight);
        var data = {
            'username': $("#user").val(),
            'message': $("#msg").val()
        }
        // socket.send(data.str);
        socket.send(JSON.stringify(data));

        event.preventDefault();
    });

    // Hook up send button to send a message
    // roomdiv.find("form").on("submit", function () {
    //     socket.send(JSON.stringify({
    //         "command": "send",
    //         "room": data.join,
    //         "message": roomdiv.find("input").val()
    //     }));
    //     roomdiv.find("input").val("");
    //     return false;
    // });
    // $("#chats").append(roomdiv);
});

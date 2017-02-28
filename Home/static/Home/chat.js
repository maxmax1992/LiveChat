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


        //if user == msgUser create div with text to the left
        //append div to a $('#hatWidnow') div with a chat bubble to a left
        // console.log(user + "," + msgUser.username);

        // <div class="panel panel-default" style="background-color: lightblue; text-align: right">
        //                             </p>
        //                             {{ message.text }} <span class="datetime">{{ message.getTime }}</span>
        //                             </p>
        //                         </div>
        if (user === msgUser.username) {
            var div = $('<div>').addClass("panel panel-default").css({
                'background-color': 'lightblue',
                'text-align': 'right',
            });
            //             function formatDate(date) {
            //     var hours = date.getHours();
            //     var minutes = date.getMinutes();
            //     var ampm = hours >= 12 ? 'pm' : 'am';
            //     hours = hours % 12;
            //     hours = hours ? hours : 12; // the hour '0' should be '12'
            //     minutes = minutes < 10 ? '0' + minutes : minutes;
            //     var strTime = hours + ':' + minutes + ' ' + ampm;
            //     return date.getDate() + 1 + "/" + date.getMonth() + "/" + date.getFullYear() + "  " + strTime;
            // }
            //
            // $(document).ready(function () {
            //     $('.datetime').text(function () {
            //         var date = new Date(parseInt($(this).text()));
            //         {#                console.log(formatDate(date));#}
            //         $(this).text(formatDate(date));
            //         $('body').fadeIn();
            //     });
            // });
            var text = msgUser.message;
            var p = $('<p>').appendData([text]);
            div.appendChild(p);


            console.log('same user');
        } else {
            //                 <div class="panel panel-default">
            //                     <p>
            //                         {{ message.text }} <span class="datetime">{{ message.getTime }}</span>
            //                     </p>
            //                 </div>
            //             </div>
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

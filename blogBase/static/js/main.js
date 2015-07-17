// Submit post on submit
$(document).ready(function() {
var content_detail = $('.content_detail');
var comment_cont = $('.comment-cont');
var urlW = window.location.href;
var pathname = window.location.pathname;


$('#comment-form').on('submit', function(event){
    event.preventDefault();
    $.ajax({ // create an AJAX call...
            url : "", // the endpoint
            type : "POST", // http method
            data : $(this).serialize(), // data sent with the post request

            success: function(data) {
              $('#content_detail').html(data);
            }




//            data : { comment : $('#comment_text').val() },
//
//            success : function(json) {
//            $('#comment_text').val(''); // remove the value from the input
//            console.log(json); // log the returned json to the console
//            console.log("success"); // another sanity check
//        },
//
//        // handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//        }
    });
//
//    (function worker() {
//          $.ajax({
//            url: "/blog/2/",
//            success: function(data) {
//              $('#content_detail').html(data);
//            }
////            complete: function(data) {
////                $('.content_detail').html(data);
////            }
//          });
//        })();


});
});
jQuery(document).ready( function($) {
  /*
      On submiting the form, send the POST ajax
      request to server and after successfull submission
      display the object.
  */
  $("#access-form").submit(function (e) {
      // preventing from page reload and default actions
      e.preventDefault();
      var cellphone = $("#id_cellphone").val();
      var name = $("#id_name").val();
      alert(cellphone);
      // make POST ajax call
      $.ajax({
          type: 'POST',
          url: "{% url 'post_visitor' %}",
          data: {
            cellphone:cellphone,
            name:name,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            dataType: "json",
          },
          success: function (response) {
              // 1. clear the form.
              // console.log("Created")
              $("#access-form").trigger('reset');
              // 2. focus to nickname input
          },
          error : function(xhr,errmsg,err) {
                  console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
      })
  })


  /*
   On focus out on input nickname,
   call AJAX get request to check if the nickName
   already exists or not.
   */
   $("#id_cellphone").change(function (e) {
       e.preventDefault();
       // get the nickname
       var cellphone = $(this).val();
       // GET AJAX request
       $.ajax({
           type: 'GET',
           url: "{% url 'check_cell' %}",
           data: {"cellphone": cellphone,
           success: function (response) {
               // if not valid user, alert the user
               if(!response["valid"]){
                   // alert("You cannot create a friend with same nick name");
                   // var nickName = $("#id_nick_name");
                   // nickName.val("")
                   // nickName.focus()
                   $("id_name").hide()
                   alert("Welcome Back!");
               }
           },
           error: function (response) {
               console.log(response)
           }
       })
   })
}

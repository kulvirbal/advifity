$(document).ready(function(){
    /*
    * Login form modal
    */
    $(".login").click(function(){
        $("#login-modal").modal();
        $("input[type='text']").val("");
        $("label.error").remove();
    });
    /*
    * Register form modal
    */
    $(".register").click(function(){
        $("#register-modal").modal();
        $("input[type='text']").val("");
        $("label.error").remove();
    });
    /*
    * Initialize form validation on the login form
    */
    $("#login-form").validate({
        // Specify validation rules
        rules: {
            email: {
                required: true
            },
            password: {
                required: true,
                maxlength: 20
            }
        },
        submitHandler: function(form) {
            $("#login-form").submit();
        }
    });
    $('input[type="reset"]').click(function(){
        $('label.error').remove();
    });
    /*
    * additional methods
    */
    jQuery.validator.addMethod("accept", function(value, element, param) {
        return value.match(new RegExp("." + param + "$"));
    });

    /*
    * Initialize form validation on the login form
    */
    $("#register-form").validate({
        // Specify validation rules
        rules: {
            firstname: {
                required: true,
                minlength: 3,
                maxlength: 20,
                accept: "[a-zA-Z]+"
            },
            lastname: {
                required: true,
                minlength: 3,
                maxlength: 20,
                accept: "[a-zA-Z]+"
            },
            email: {
                required: true,
                email: true,
                remote: '/checkuser/'
            },
            password: {
                required: true,
                maxlength: 20,
                minlength: 5
            },
            cpassword: {
                required: true,
                equalTo: "#reg_password"
            },
            gender:{
                required: true
            },
            usertype:{
                required: true
            }

        },
        messages: {
            firstname: {
                accept: "Please Enter Alphabets Only"
            },
            email:{
                remote: "Email Id already exists"
            }
        },
        submitHandler: function(form) {
            
            $("#register-form").submit();
        }
    });
});
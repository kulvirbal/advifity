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
    //set session on page load
	setTimeout(function() {
		if(typeof(Storage) !== "undefined") {
	        if (localStorage.remember) {
                $('#login-form #email-login').attr("value", localStorage.email);
                $('#login-form #email-login').attr("placeholder", localStorage.email);
                $('#login-form #password').attr("value", localStorage.password);
                $('#login-form #password').attr("placeholder", localStorage.password);
	            $('#remember').attr('checked','checked');
	        }  
	    } else {
	       alert("Sorry, your browser does not support web storage...");
	    }
	    $('.userNav').show();
	}, 400);

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
            if(document.getElementById('remember').checked)	{
                localStorage.remember = $("#remember").val();
                localStorage.email = $("#email-login").val();
                localStorage.password = $("#password").val();
            } else {
                localStorage.clear();
            }	       			        
           
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
    /*
    * Initialize form validation on the update form
    */
    $("#update-form").validate({
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
            password: {
                maxlength: 20,
                minlength: 5
            },
            cpassword: {
                equalTo: "#u-password"
            },
            gender:{
                required: true
            },
            usertype:{
                required: true
            },
            pic:{
                extension: "png|jpeg|gif|jpg"
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
            
            $("#update-form").submit();
        }
    });

    
    $(".read-more").on("click", function () {
        var txt = $(this).prev('.post-desc-hidden').is(':visible') ? 'Read More' : 'Read Less';
        $(this).text(txt);
        $(this).prev('.post-desc-hidden').prev(".post-desc").slideToggle(200);
        $(this).prev('.post-desc-hidden').slideToggle(200);
    });
});
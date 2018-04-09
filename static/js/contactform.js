jQuery(document).ready(function($) {
  "use strict";

  
  $("form.contactForm").validate({
    // Specify validation rules
    rules: {
        name: {
            required: true,
            minlength: 3,
            maxlength: 20,
            accept: "[a-zA-Z]+"
        },
        subject: {
            required: true,
            minlength: 3,
            maxlength: 20
        },
        email: {
            required: true,
            email: true
        },
        message:{
            required: true
        }

    },
    messages: {
        firstname: {
            accept: "Please Enter Alphabets Only"
        }
    },
    submitHandler: function(form) {
        
        $("form.contactForm").submit();
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
   var geocoder = new google.maps.Geocoder();
   var address = "121 Brunel Rd, Mississauga, ON L4Z 3E9";
   var latitude = '';
   var longitude = '';
   geocoder.geocode( { 'address': address}, function(results, status) {
 
     if (status == google.maps.GeocoderStatus.OK) {
       latitude = results[0].geometry.location.lat();
       longitude = results[0].geometry.location.lng();
       var myLatLng = {lat: latitude, lng: longitude};
       var mapOptions = {
         zoom: 15, 
         center: myLatLng, 
         mapTypeId: google.maps.MapTypeId.ROADMAP
       };
       var infowindow = new google.maps.InfoWindow({
         content: address
       });
       var map = new google.maps.Map($("#google-map").get(0), mapOptions);
       var marker = new google.maps.Marker({
           position: myLatLng,
           map: map,
           title: '121 Brunel Rd, Mississauga, ON L4Z 3E9'
       }); 
       infowindow.open(map, marker);
     } 
   });
});

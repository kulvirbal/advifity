function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var geocoder = new google.maps.Geocoder();
    var address = document.getElementById('post_address').value;

    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();
            var map = new google.maps.Map(document.getElementById('google-map'), {
                zoom: 6,
                center: {lat: latitude, lng: longitude}
            });
            if($('#user_address').length > 0) {
                calculateAndDisplayRoute(directionsService, directionsDisplay);
            } else {
                var marker = new google.maps.Marker({
                    position: {lat: latitude, lng: longitude},
                    map: map,
                    title: address
                }); 
                var infowindow = new google.maps.InfoWindow({
                    content: address
                });
                infowindow.open(map, marker);
            }

            directionsDisplay.setMap(map);
        } 
    });
}
  
function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    var waypts = [];     
    directionsService.route({
        origin: document.getElementById('user_address').value,
        destination: document.getElementById('post_address').value,
        waypoints: waypts,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
    }, function(response, status) {
        if (status === 'OK') {
            directionsDisplay.setDirections(response);
            var route = response.routes[0];
            var summaryPanel = document.getElementById('directions-panel');
            summaryPanel.innerHTML = '';
            // For each route, display summary information.
            for (var i = 0; i < route.legs.length; i++) {
                var routeSegment = i + 1;
                summaryPanel.innerHTML += '';
                summaryPanel.innerHTML += '<b>Distance: </b>'+route.legs[i].distance.text + '<br><br>';
            }
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}     
$(document).ready(function(){
    /*
    * Initialize form validation on apply post form
    */
   $("#apply-post").validate({
        // Specify validation rules
        rules: {
            resume:{
                required: true,
                extension: "doc|docx|pdf"
            }
        },
        messages: {
           
        },
        submitHandler: function(form) {
            $("#apply-post").submit();
        }
    });
});
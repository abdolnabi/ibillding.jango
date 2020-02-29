/**
 * Created by Asus on 09/02/2020.
 */
window.onload = function() {
    var latlng = new google.maps.LatLng(35.7509,51.4141);
    var map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        zoom: 11,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: 'Set lat/lon values for this property',
        draggable: true
    });
    google.maps.event.addListener(marker, 'dragend', function (a) {
        console.log(a);
        // var latitudes = document.getElementById('id_coordinate');
        // latitudes.value = a.latLng.lat().toFixed(4) + '-' + a.latLng.lng().toFixed(4);
        var latitude = document.getElementById('id_latitude');
        var longitude = document.getElementById('id_longitude');
        latitude.value = a.latLng.lat().toFixed(4);
        longitude.value = a.latLng.lng().toFixed(4);
    });
};


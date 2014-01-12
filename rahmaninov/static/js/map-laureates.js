/**
 * Created by nani on 11/7/13.
 */
var map;
var info;

var json = (function () {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': '/achievements/locations',
        'dataType': 'json',
        'success': function (data) {
            json = data;
        }
    });
    return json;
})();

function initialize() {
    var newa = 47.026858;
    var myLatlng = new google.maps.LatLng(newa, 28.841550);
    var mapOptions = {
        zoom: 4,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    info = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    google.maps.event.addListenerOnce(map, 'tilesloaded', addMarkers);
}

function addMarkers() {
    for (var i = 0; i < json.locations.length; i++) {
        var location = json.locations[i];

        var content = "<div><h3>" + location.country + "</h3><h4>" + location.city + "</h4><ul>";
        for (var j = 0; j < location.laureates.length; j++) {
            content = content + "<li>" + location.laureates[j] + "</li>";
        }
        content = content + "</ul></div>";

        addMarker(location.lat, location.lng, content);
    }

}

function addMarker(x, y, infoContent) {
    var marker = new google.maps.Marker({
        map: map,
        icon: 'http://s3-eu-west-1.amazonaws.com/rachmaninoff/static/img/maps/cup.png',
        position: new google.maps.LatLng(x, y),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(10, 37)
    });

    google.maps.event.addListener(marker, 'click', function () {
        info.setContent(infoContent);
        info.open(map, marker);
    });
}
google.maps.event.addDomListener(window, 'load', initialize);

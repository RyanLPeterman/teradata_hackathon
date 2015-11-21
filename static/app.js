var map, heatmap;

// temp
var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var labelIndex = 0;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: {lat: 37.775, lng: -122.434},
    mapTypeId: google.maps.MapTypeId.MAP
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getCrimeData(),
    map: map,
    radius: 30
  });

  // addHousingData(getHousingData(), map);
  
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
  heatmap.set('radius', heatmap.get('radius') ? null : 30);
}

function changeOpacity() {
  heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

function addHousingData(houses, map) {
    var num_houses = houses.length;

    // init infoWindow for use when setting content
    var infoWindow = new google.maps.InfoWindow();

    for(i = 0; i < num_houses; i++) {
        // adds a marker to the map where listing is
        var marker = new google.maps.Marker({
            position: houses[i].location,
            label: labels[labelIndex++ % labels.length],
            map: map
        });

        //Attach click event to the marker.
        (function (marker, rent) {
            google.maps.event.addListener(marker, "click", function (e) {
                //Wrap the content inside an HTML DIV in order to set height and width of InfoWindow.
                infoWindow.setContent("<div style = 'width:200px;min-height:40px'> The rent for this house is:" + rent + "</div>");
                infoWindow.open(map, marker);
            });
        })(marker, houses[i].rent);
    }
}

// gets the housing JSON
// lat, long, rent, #rooms
function getHousingData() {
    return [ {location: new google.maps.LatLng(37.782551, -122.445368), rent : 100},
    {location: new google.maps.LatLng(37.782551, -122.44), rent : 42},
    {location: new google.maps.LatLng(37.78, -122.445368), rent : 68}
    ];
}

// Heatmap data: 500 Points
function getCrimeData() {

    var my_data = JSON.parse(crimes);
    var result = new Array();

    for(i = 0; i < my_data.max; i++) {
        // fix this latitude and longitude switched in json
        result.push(new google.maps.LatLng(my_data.data[i].lng, my_data.data[i].lat));
    }

    return result;
}

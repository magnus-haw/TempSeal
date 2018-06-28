var dataurl = 'data.geojson';
var foodurl = 'food.geojson';

var HOT= "#ec5a29";
var WARM = "#ef8e27";
var JUSTRIGHT = "#94bc46";
var COOL = "#5fc8e8";
var COLD = "#10788e";

function getColor(d) {
        return d > 1 ? HOT :
               d > 0  ? WARM :
               d > -1  ? JUSTRIGHT :
               d > -2  ? COOL :
               d > -3   ? COLD :
                            JUSTRIGHT;
    }

//#################### POPUP CONTENT #########################
function buildingFeature(feature, layer) {
  var props = feature.properties;
  var blen = 200;
  var str = props.name.replace(/\s/g, "_");
  var content = `<a href="${str}/"><h3>${props.name}</h3></a>`;
  content+= `<svg class="chart" width="300" height="105">`;
  var hot = props.hotvotes;
  var warm= props.warmvotes;
  var ok  = props.okvotes;
  var cool= props.coolvotes;
  var cold= props.coldvotes;
  var total = hot+warm+ok+cool+cold;
  
  content  += `<g transform="translate(0,0)"><text x="0" y="10" dy=".35em">Hot:</text><text x="60" y="10" dy=".35em" text-anchor="end">${hot}</text>`;
  content  += `<rect x="65" width="${blen*hot/total+1}" height="19" style="fill: rgb(236, 90, 41);"></rect></g>`;
  content  += `<g transform="translate(0,20)"><text  x="0" y="10" dy=".35em">Warm:</text><text  x="60" y="10" dy=".35em" text-anchor="end">${warm}</text>`;
  content  += `<rect x="65" width="${blen*warm/total+1}" height="19" style="fill: rgb(239, 142, 39);"></rect></g>`;
  content  += `<g transform="translate(0,40)"><text x="0" y="10" dy=".35em">Alright:</text><text x="60" y="10" dy=".35em" text-anchor="end">${ok}</text>`;
  content  += `<rect x="65" width="${blen*ok/total+1}" height="19" style="fill: rgb(148,188,70);"></rect></g>`;
  content  += `<g transform="translate(0,60)"><text x="0" y="10" dy=".35em">Cool:</text><text x="60" y="10" dy=".35em" text-anchor="end">${cool}</text>`;
  content  += `<rect x="65" width="${blen*cool/total+1}" height="19" style="fill: rgb(95,200,232);"></rect></g>`;
  content  += `<g transform="translate(0,80)"><text x="0" y="10" dy=".35em">Cold:</text><text x="60" y="10" dy=".35em" text-anchor="end">${cold}</text>`;
  content  += `<rect x="65" width="${blen*cold/total+1}" height="19" style="fill: rgb(16,120,142);"></rect></g></svg>`;
  content+= `<button class="btn btn-info btn-sm" type="button" data-toggle="modal" data-target="#temp-form" data-whatever="${feature.id}">Submit Temp Feedback</button>`;
  layer.bindPopup(content);
}

function foodFeature(feature, layer) {
  var props = feature.properties;
  var content = props.food;
  layer.bindPopup(content);
}


//##################### MARKER PROPERTIES ######################
function buildingPoint(feature, latlng) {
    var props = feature.properties;
    var mycolor = getColor(props.temp);
    return L.circleMarker(latlng, {
            radius: 7,
            fillColor: mycolor,
            color: "#000",
            weight: 1,
            opacity: 0,
            fillOpacity: 0.9
    });
}

var PizzaIcon = L.icon({
              iconUrl: '/static/polls/images/pizza.png',
              //shadowUrl: 'images/leaf-shadow.png',
              iconSize: new L.Point(25, 25),
              //shadowSize: new L.Point(68, 95),
              iconAnchor: new L.Point(12, 12),
              //popupAnchor: new L.Point(-3, -76)
});

function foodMarker(feature, latlng) {
    var props = feature.properties;
    return L.marker(latlng, {icon: PizzaIcon});
}


//##################### LEGEND #################################
var legend = L.control({position: 'topright'});
legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [2,1,0,-1,-2],
        labels = ['Hot','Warm','Just right','Cool','Cold'],
        lines=[],
        food="",
        from, to;

    for (var i = 0; i < grades.length; i++) {
        lines.push('<i style="background:' + getColor(grades[i]) + '"></i> ' + labels[i]+ ' ' + food);
    }
    
    lines.push('');
    lines.push("<span style='display:block !important; width: 73px; text-align: center; font-size: 15px;'>Pasadena <br><a href='http://www.wunderground.com/cgi-bin/findweather/getForecast?query=Pasadena, CA' title='Pasadena, CA Weather Forecast'><img src='http://weathersticker.wunderground.com/weathersticker/smalltemp/language/english/US/CA/Pasadena.gif' alt='Find more about Weather in Pasadena, CA' /></a><br></span>")

    div.innerHTML = lines.join('<br>');
    return div;
};

//######################### Buttons ###############################
var tempbutton = L.control({position:"bottomleft"});
    tempbutton.onAdd = function(map){
        var div = L.DomUtil.create('div','info legend');
        var content = `<button class="btn btn-info btn-lg" type="button" data-toggle="modal" data-target="#temp-form"><img src='/static/polls/images/thermometer.png' width='30'></button>`
        div.innerHTML = content;
        return div;
    };

var foodbutton = L.control({position:"bottomleft"});
    foodbutton.onAdd = function(map){
        var div = L.DomUtil.create('div','info legend');
        var content = `<button class="btn btn-info btn-lg" type="button" data-toggle="modal" data-target="#food-form"><img src='/static/polls/images/pizza.png' width='30'></button>`
        div.innerHTML = content;
        return div;
    };

//########################## LOGO ###############################
var logo = L.control({position: 'bottomright'});
    logo.onAdd = function(map){
        var div = L.DomUtil.create('div', 'myclass');
        div.innerHTML= "<a href='http://tsf.caltech.edu'> <img src='/static/polls/images/logo.png' height='70'> </a>";
        return div;
    };

//################### ADD ALL FEATURES TO MAP ###################
//Add points for each building
window.addEventListener("map:init", function (event) {
    var map = event.detail.map;
    map.zoomControl.remove();
    legend.addTo(map);
    logo.addTo(map);
    tempbutton.addTo(map);
    foodbutton.addTo(map);
    map.options.maxZoom = 18;
    map.options.minZoom = 16;
    // Download GeoJSON data with Ajax
    fetch(dataurl).then(function(resp) {
        return resp.json();
    }).then(function(data) {
    
        var buildingLayer = L.layerGroup([L.geoJson(data, {  
            onEachFeature: buildingFeature, //popup for each point
            pointToLayer: buildingPoint //point properties (e.g. color)
        })] ).addTo(map);
    });

    fetch(foodurl).then(function(resp) {
        return resp.json();
    }).then(function(data) {
    
        var foodLayer = L.layerGroup([L.geoJson(data, {                                                  
            onEachFeature: foodFeature, //popup for each point
	    pointToLayer: foodMarker //point properties (e.g. color)
        })] );

        var overlayMaps = {"Food":foodLayer};
        L.control.layers(null, overlayMaps).addTo(map);
    });

    //var baseMaps= {};
    //var overlayMaps = {"Temp": buildingLayer,"Food":foodLayer};
    //L.control.layers(null, overlayMaps).addTo(map);
});


$(document).ready(function(){
  $('#temp-form').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var building = button.data('whatever'); // Extract info from data-* attributes
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('#id_building').val(building);
  })
});


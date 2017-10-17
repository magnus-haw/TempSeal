var dataurl = 'data.geojson';

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
function onEachFeature(feature, layer) {
                        var props = feature.properties;
                        var content = `<h3>${props.name}</h3><p>${props.temp}</p>`;
                        layer.bindPopup(content);
                    }

//##################### MARKER PROPERTIES ######################
function pointToLayer(feature, latlng) {
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

function weather(o){
document.getElementById("weather").innerHTML= (o.main.temp-273.15).toFixed(2) +'C'
}

//##################### LEGEND #################################
var legend = L.control({position: 'topright'});
legend.onAdd = function (map) {

	var div = L.DomUtil.create('div', 'info legend'),
		grades = [-2,-1,0,1,2],
		labels = ['Cold','Cool','Just right','Warm','Hot'],
		lines=[],
		from, to;

	for (var i = 0; i < grades.length; i++) {
		lines.push('<i style="background:' + getColor(grades[i]) + '"></i> ' + labels[i]);
	}
	
	lines.push('');
	lines.push("<span style='display:block !important; width: 73px; text-align: center; font-size: 15px;'>Pasadena <br><a href='http://www.wunderground.com/cgi-bin/findweather/getForecast?query=Pasadena, CA' title='Pasadena, CA Weather Forecast'><img src='http://weathersticker.wunderground.com/weathersticker/smalltemp/language/english/US/CA/Pasadena.gif' alt='Find more about Weather in Pasadena, CA' /></a><br></span>")

	div.innerHTML = lines.join('<br>');
	return div;
};

//########################## LOGO ###############################
var logo = L.control({position: 'bottomright'});
    logo.onAdd = function(map){
        var div = L.DomUtil.create('div', 'myclass');
        div.innerHTML= "<a href='http://tsf.caltech.edu'> <img src='/static/polls/images/logo.png' height='70'> </a>";
        return div;
    }

//################### ADD ALL FEATURES TO MAP ###################
//Add points for each building
window.addEventListener("map:init", function (event) {
    var map = event.detail.map;
    legend.addTo(map);
    logo.addTo(map);
    // Download GeoJSON data with Ajax
    fetch(dataurl).then(function(resp) {
        return resp.json();
    }).then(function(data) {
    
        L.geoJson(data, {  
            onEachFeature: onEachFeature, //popup for each point
            pointToLayer: pointToLayer //point properties (e.g. color)
        }).addTo(map);
        
    });
});



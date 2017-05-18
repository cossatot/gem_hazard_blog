Title: GEM Global Active Faults
Slug: global-active-fault-viewer

<script src='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.js'></script>
<link href='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.css' rel='stylesheet' />


<div id="mapid" style="width: 800px; height: 600px;"></div>
<script>

  var mymap = L.map('mapid').setView([31.1, 83.3], 4);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

  var faultColors = {
    "Normal": "red",
    "Sinistral-Normal": "#b936ff",
    "Normal-Sinistral": "red",
    "Reverse": "black",
    "Anticline": "grey",
    "Sinistral-Reverse": "#b936ff",
    "Blind Thrust": "black",
    "Sinistral": "#b936ff",
    "Reverse-Sinistral": "black",
    "Dextral-Reverse": "blue",
    "Dextral": "blue",
    "Dextral-Normal": "blue",
    "Thrust": "black",
    "Dextral Normal": "blue",
    "Sinistral Normal": "#b936ff",
    "Strike-Slip": "yellow",
    "Reverse strike-slip": "black",
    "Thrust strike-slip": "black",
    "Sinistral-reverse": "#b936ff",
    "Strike-slip": "yellow",
    "Strike-slip thrust": "yellow",
    "Strike-slip reverse": "yellow",
    "Dextral-reverse": "blue",
    "Syncline": "grey",
    "Strike-Slip-Normal": "yellow",
    "Normal-Dextral": "red",
    "Reverse-Dextral": "black",
    "Strike-Slip-Reverse": "yellow",
    "Strike Slip": "yellow",
    "Reverse-Strike-Slip": "black",
    "": "green"
  };

  var faults = L.mapbox.featureLayer()
    .loadURL("https://raw.githubusercontent.com/cossatot/gem-global-active-faults/master/geojson/gem_active_faults.geojson")
    .on('ready', function() {
      faults.eachLayer(function(layer) {
        //layer.bindPopup(layer.feature.properties.fz_name);
        var out = [];
        for(key in layer.feature.properties){
          if (layer.feature.properties[key] != null){
            out.push(key+": "+layer.feature.properties[key]);
            }
          }
        layer.bindPopup(out.join("<br />"));
        //  layer.bindPopup(key+": "+feature.properties[key]+"<br />")
        });
      })
      .on('ready', function() {
      faults.eachLayer(function(layer) {
        if (layer.feature.properties.slip_type != null){
        //  layer.feature["marker-color"] = "blue";
        //console.log("slip type \n");
          layer.setStyle({"color": faultColors[layer.feature.properties.slip_type]});
        } else {
        // console.log("no slip type \n")
          //layer.feature["marker-color"] = "green";
          layer.setStyle({"color": "green"});
        };
      });
    })
    .addTo(mymap);


</script>

Thanks to USAID for sponsoring the Global Active Faults Project.

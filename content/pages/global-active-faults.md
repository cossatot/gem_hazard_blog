Title: GEM Global Active Faults
Slug: global-active-fault-viewer

<script src='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.js'></script>
<link href='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.css' rel='stylesheet' />


<div id="mapid" style="width: 800px; height: 600px;"></div>
<script>

  var mymap = L.map('mapid').setView([31.1, 83.3], 8);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

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
    .addTo(mymap);


</script>

I wanna see the faults!

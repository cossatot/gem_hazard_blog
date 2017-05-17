Title: New GEM dataset of active faults in the Caribbean and Central America
Date: 2017-05-16
Slug: c-am-car-faults
Author: Richard Styron

The [Global Active Faults][gem-gaf] project of the [GEM Foundation][gem] aims 
to produce a globally complete, reasonably homogeneous dataset of active faults 
on the Earth's surface for seismic hazard assessment. While most deforming 
regions of the world have some publicly available active fault datasets that I 
can stitch together, there are a few significant data gaps. The Central 
American and Caribbean region is one of these regions, despite the great number 
of rapidly-slipping faults and large vulnerable population. 


With help from my colleague Julio Garcia, I have put together a dataset of
active faults in the region, as my contribution to the [Caribbean-Central 
American Risk Assessment (CCARA)][ccara] program. The dataset is hosted on 
[GEM's github page][gem-gh] and is publicly available with a Creative Common 
attribution license. There are currently over 200 fault traces in the database. 
These faults span the range from distributed, *relatively* slow intraplate 
deformation to major plate boundary faults. The diversity of faulting here 
reflects the highly variable style of tectonic deformation in the region: many 
styles of deformation are present, with the only consistent theme being that 
these faults slip quite fast.

## Faulting in Central America and the Caribbean

<script src='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.js'></script>
<link href='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.css' rel='stylesheet' />


<div id="mapid" style="width: 800px; height: 500px;"></div>
<script>

  var mymap = L.map('mapid').setView([15., -75.], 4.5);

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
    .loadURL("https://raw.githubusercontent.com/cossatot/central_am_carib_faults/master/geojson/central_am_caribbean.geojson")
    .on('ready', function() {
      faults.eachLayer(function(layer) {
        var out = [];
        for(key in layer.feature.properties){
          // get tooltip
          if (layer.feature.properties[key] != null){
            out.push(key+": "+layer.feature.properties[key]);
            }
          }
        layer.bindPopup(out.join("<br />"));
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
*GEM Central American and Caribbean active fault data*

Faulting in the region blah blah blah

[![Active faults of northern Central 
America](/images/2017/c_am_fault_map_lo.png)](/images/2017/c_am_fault_map.png)

## About the GEM Central American and Caribbean fault database

The GEM Central American and Caribbean fault database was created with the 
immediate goal of providing data for a fault source model for [Probabilistic 
Seismic Hazard Analysis (PSHA)][psha], as well as serving as a resource for 
characterizing local or regional tectonics for research, education and general 
interest. As such, a minimal set of geologic attributes for the faults in the 
dataset are included that are important in PSHA modeling. These attributes 
primarily describe the fault geometry, kinematics and slip rates of the faults, 
with some additional information such as the primary data source and the 
paleoseismic history of the fault. Though fascinating, the region is 
chronically understudied and much of this information is unavailable for most 
structures, particularly the slip rates and earthquake histories of the faults.

Fault coverage is reasonably good. The bounds of the map area are from Chiapas, 
Mexico through Panama in the west, across the North American-Caribbean plate 
boundary in the north to Cuba, Hispaniola and Puerto Rico, and then south 
through the Lesser Antilles. The southern margin of the region, the South 
American-Caribbean plate boundary, is covered by a few other datasets including 
the [South American Risk Assessment (SARA)][SARA] project and the [Active 
Tectonics of the Andes (ATA)][ata] fault maps, which are included in the GEM 
Global Active Faults dataset.

A few areas need additional mapping. Southern Costa Rica is a hard area to 
work, given the rugged terrain, dense tropical vegetation, and polyphase 
deformation history; mapping here is somewhat incomplete and it's very 
difficult to tell which structures may be active in the current tectonic 
regime. The Lesser Antilles have yet to receive sufficient attention, in part 
because many of the probable active structures are offshore. Both of these 
areas are priority areas for GEM, however, so expect more progress on this 
front in the coming months.

Nonetheless, the dataset is definitely usable, for purposes ranging from 
seismic hazard to testing of tectonic hypotheses.

## Contributing

While the Central American and Caribbean active fault dataset has been 
developed by GEM, we welcome contributions from users, whether it is actively 
contributing fault mapping, discussing potential changes to particular 
structures or regions, or providing feedback in terms of what we can do to make 
the data more useful.

The best way to contribute is through the [github page][gem-gh]; simply go to 
the ['Issues'][cam-issues] page and file one (see [here][gh-issues] for an 
explanation of issues). If this isn't an option (for example, you don't have a 
GitHub account), you can reach me by email at 
richard.styron[at]globalquakemodel.org



[gem]: www.globalquakemodel.org
[gem-gh]: github.com/cossatot/central_am_carib_faults
[psha]: http://www.earthquakes.bgs.ac.uk/hazard/haz_guide/psha.html
[gem-gaf]: https://www.globalquakemodel.org/what/seismic-hazard/active-faults-database/

[SARA]: https://www.globalquakemodel.org/what/regions/south-america/
[ata]: https://github.com/ActiveTectonicsAndes/ATA
[ccara]: https://www.globalquakemodel.org/what/regions/caribbean_c_america/
[gh-issues]: https://guides.github.com/features/issues/
[cam-issues]: https://github.com/cossatot/central_am_carib_faults/issues
[rs]: mailto:richard.styron@globalquakemodel.org

var USMap = L.map("map", {
  center: [37.0902, -95.7129],
  zoom: 4
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(USMap);

// var url = "https://data.sfgov.org/resource/cuks-n6tp.json?$limit=10000";
var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";

d3.json(url, function(response) {
  console.log(response.features[1])

  var locations;


  for(i=0; i<response.features.length; i++){
    locations = response.features[i].geometry.coordinates;
    coordinates = [locations[1],locations[0]];
    Magnitude = response.features[i].properties.mag;
    
    var circle = L.circle(coordinates,{
        color:getColor(Magnitude),
        fillColor:getColor(Magnitude),
        fillOpacity:"0.5",
        radius:getRadius(Magnitude),
        Magnitude:Magnitude,
        Place: coordinates
      }).bindPopup("Magnitude:"+Magnitude).addTo(USMap);    
  }


  var legend = L.control({position:"bottomright"});
  legend.onAdd = function(map){
    var div = L.DomUtil.create("div","legend");
    var labels = ["0-1","1-2","2-3","3-4","4-5","5-6","6-7","8-9","9+"];
    var sections = [1,2,3,4,5,6,7,8,9];
    div.innerHTML = `<p><h1> Magnitude Chart </h1></p>`
    for (var i=0; i<sections.length; i++){
      div.innerHTML+= `<p style ="background: ${getColor(i)}">${labels[i]}</p>`
    }
    return div;
  }

  legend.addTo(USMap);
});


function getColor(Magnitude)
{
  if(Magnitude>9){
    return "#ff4000";
  }
  else if(Magnitude>8){
    return "#ff5500";
  }
  else if(Magnitude>7){
    return "#ff6a00";
  }
  else if(Magnitude>6){
    return "#ff8000";
  }
  else if(Magnitude>5){
    return "#ff9500";
  }
  else if(Magnitude>4){
    return "#ffaa00";
  }
  else if(Magnitude>3){
    return "#ffbf00";
  }
  else if(Magnitude>2){
    return "#ffd400";
  }
  else if(Magnitude>1){
    return "#ffea00";
 }
  else{
    return "#ffff00";
  }    
}

function getRadius(Magnitude){
  if(Magnitude>9){
    return 90000 + (Magnitude*1000);
  }
  else if(Magnitude>8){
    return 80000 + (Magnitude*1000);
  }
  else if(Magnitude>7){
    return 70000 + (Magnitude*1000);
  }
  else if(Magnitude>6){
    return 60000 + (Magnitude*1000);
  }
  else if(Magnitude>5){
    return 50000 + (Magnitude*1000);
  }
  else if(Magnitude>4){
    return 40000 + (Magnitude*1000);
  }
  else if(Magnitude>3){
    return 30000 + (Magnitude*1000);
  }
  else if(Magnitude>2){
    return 20000 + (Magnitude*1000);
  }
  else if(Magnitude>1){
    return 10000 + (Magnitude*1000);
  }
  else{
    return Magnitude*1000;
  }    
}
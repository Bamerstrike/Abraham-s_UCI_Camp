// from data.js
var tableData = data;

// YOUR CODE HERE!

// Grab button object 
var button = d3.select("#filter-btn");

// Grab tbody tag
var tbody = d3.select("tbody");

// On click event on the button, do...
button.on("click",function() {

    d3.event.preventDefault();

    // Grab input object from input box and take them in as values
    var dateInput = d3.select("#datetime").property("value");
    var cityInput = d3.select("#city").property("value");
    var stateInput = d3.select("#state").property("value");
    var countryInput = d3.select("#country").property("value");
    var shapeInput = d3.select("#shape").property("value");

    // Creates a fresh list of unfiltered data
    var filteredData = tableData;

    // If the string has any value, it will filter out to find the matching data.
    // Ignores if no value
    if (dateInput){
        filteredData = filteredData.filter(Data => Data.datetime === dateInput);
    }

    if(cityInput){
        filteredData = filteredData.filter(Data => Data.city === cityInput);
    }

    if(stateInput){
        filteredData = filteredData.filter(Data => Data.state === stateInput);
    }

    if(countryInput){
        filteredData = filteredData.filter(Data => Data.country === countryInput);
    }

    if(shapeInput){
        filteredData = filteredData.filter(Data => Data.shape === shapeInput);
    }

    // Clears the current information stored in the tbody tag
    tbody.html("");

    // For each filtered data value
    filteredData.forEach((Data) => {
        // Create a new row on the table body
        var newRow = tbody.append("tr");
        // For each key and value in the object filteredData
        Object.entries(Data).forEach(([key,value]) => {
            // Create a new data box
            var newCell = newRow.append("td");
            // Input the text value for each key into the databox.
            newCell.text(value);
        });
    });

});
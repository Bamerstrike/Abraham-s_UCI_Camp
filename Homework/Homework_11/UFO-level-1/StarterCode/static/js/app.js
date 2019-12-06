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
    // Grab input object from input box with the id "datetime"
    var input = d3.select("#datetime");
    // Grab the text value from the object input
    var inputValue = input.property("value");
    
    // Filters out the date input from the data.js file with the date in the input box
    var filteredData = tableData.filter(Data => Data.datetime === inputValue);

    // Clears out any information in tbody if it exists.
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
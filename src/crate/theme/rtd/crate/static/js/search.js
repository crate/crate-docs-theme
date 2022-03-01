//Handler for response from google.
function hndlr(response) {
  if (response.items == null) {
    //Sometimes there is a strange thing with the results where it says there are 34 results/4 pages, but when you click through to 3 then there is only 30, so page 4 is invalid now.
    //So if we get to the invalid one, send them back a page.
    //window.location.replace("search.html?start=" + (start - 10) + "&q=" + query);
    return;
  }

  //Search results load time
  document.getElementById("cr-search-result-info").innerHTML =
    "About " +
    response.searchInformation.formattedTotalResults +
    " results (" +
    response.searchInformation.formattedSearchTime +
    " seconds)";

  //Clear the div
  document.getElementById("cr-search-results").innerHTML = "";

  //Loop through each item in search results
  for (var i = 0; i < response.items.length; i++) {
    var item = response.items[i];
    var content = "";

    content += "<li class='cr-search-result'>";
    content +=
      "<a class='cr-search-title' href='" +
      item.link +
      "'>" +
      item.htmlTitle +
      "</a><br/>";
    //description text and URL text.
    content +=
      item.htmlSnippet.replace("<br>", "") +
      "<br/><div class='cr-search-url'>Source: " +
      item.link +
      "" +
      "</li>";
    document.getElementById("cr-search-results").innerHTML += content;
  }
  //Page Controls
  var totalPages = Math.ceil(response.searchInformation.totalResults / 10);
  //console.log(totalPages);
  var currentPage = Math.floor(start / 10 + 1);
  //console.log(currentPage);
  var pageControls = "<div class='cr-search-pagination'>";
  //Page change controls, 10 max.
  for (var x = 1; x <= totalPages && x <= 10; x++) {
    pageControls += "<div class='cr-search-page";
    if (x === currentPage) pageControls += " cr-search-current-page";
    var pageLinkStart = x * 10 - 9;
    pageControls +=
      "'><a href='search.html?start=" +
      pageLinkStart +
      "&q=" +
      query +
      "'>" +
      x +
      "</a></div>";
  }
  pageControls += "</div>";
  document.getElementById("cr-search-results").innerHTML += pageControls;
}

//Get search text from query string.
//var query = document.URL.substr(document.URL.indexOf("q=") + 2);
var checkUrl = window.location.search;
var urlParams = new URLSearchParams(checkUrl);
var query = urlParams.get("q");

// add keywords to the form
if (query && query.length != 0) {
  var searchBox = document.getElementById("cr-search-query");
  searchBox.value = query;

  var start = document.URL.substr(document.URL.indexOf("start=") + 6, 2);
  if (start === "1&" || document.URL.indexOf("start=") === -1) start = 1;

  //Load the script src dynamically to load script with query to call.
  // DOM: Create the script element
  var jsElm = document.createElement("script");
  // set the type attribute
  jsElm.type = "application/javascript";
  // make the script element load file
  jsElm.src =
    `https://www.googleapis.com/customsearch/v1/siterestrict?key=${google_search_api_key}&cx=${google_search_cx_id}&start=` +
    start +
    "&q=" +
    query +
    "&callback=hndlr";
  // finally insert the element to the body element in order to load the script
  document.body.appendChild(jsElm);
}

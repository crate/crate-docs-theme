$(document).ready(function () {
  /* check if there are parameters in the url (i.e. search queries, if so, invoke search) */
  function paraChecker() {
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let searchString = urlParams.get("s");
    let firstLaunch = false;
    if (searchString && searchString.length !== 0) {
      let firstLaunch = true;
      search(firstLaunch);
    }
  }
  paraChecker();
});

// google search
function search(firstLaunch) {

  let firstLaunchTrigger = firstLaunch;
  let queryString = window.location.search;
  let urlParams = new URLSearchParams(queryString);
  let searchString = urlParams.get("s");

  /* select the parameter or input element  */
  if (searchString && searchString.length !== 0 && firstLaunchTrigger) {
    input = searchString;
  } else {
    inputfield = document.getElementById("cr-search-query");
    input = inputfield.value;
  }
  let output = document.getElementById("cr-search-results");

  /* fetch the following URL that includes apikey, cx and the value of input */
  fetch(
    `https://www.googleapis.com/customsearch/v1?key=${google_search_api_key}&cx=${google_search_cx_id}&q=${input}`
  )
    .then((response) => response.text())
    .then((text) => {
      let result = JSON.parse(text);
      let txt = "";
      result.items.forEach((item) => {
        /* add it to your results div */
        txt += "<li>";
        txt += '<a href="' + item.link + '">' + item.title + "</a>";
        txt += '<p class="context">';
        txt += item.htmlSnippet;
        txt += "</p>";
        txt += "</li>";

        //item.link, item.title, ...etc
      });

      output.innerHTML = txt;
    })
    .catch((error) => {
      let txt = "";
      txt +=
        '<li style="background-image: none !important;padding: 0 !important;">';
      txt += '<p style="font-weight: bold;">';
      txt +=
        "Your search did not match any documents. Please make sure that all words are spelled correctly.";
      txt += "<p>";
      txt += "</li>";

      output.innerHTML = txt;
    });

  /* add search parameter to the url */
  var baseURL = window.location.origin + window.location.pathname;
  if (history.pushState) {
    var newUrl = baseURL + "?s=" + input;
    window.history.pushState({ path: newUrl }, "", newUrl);
  }

  /* set trigger to false so it doesn't interfere with the input field */
  firstLaunchTrigger = false;

  /* make sure the form isn't actually submitted by returning false */
  return false;
}

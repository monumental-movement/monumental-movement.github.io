/* ===========================================================
   Lunr Search Engine – Multi-language Version (ja/en)
   Compatible with monumental-movement.jp structure
   =========================================================== */

var idx;
var documents = [];
var currentLang = window.location.pathname.startsWith('/en/') ? 'en' : 'ja';
var searchPath = currentLang === 'en' ? '/en/search.html' : '/search.html';

/* -----------------------------------------------------------
   Load the search index dynamically (embedded Liquid data)
----------------------------------------------------------- */
function loadDocuments() {
  return fetch(searchPath)
    .then((response) => {
      if (!response.ok) throw new Error("search.html not found");
      return response.text();
    })
    .then((html) => {
      // Extract the embedded JS variable "var documents = [...]"
      const match = html.match(/var documents = (\[.*\]);/s);
      if (match && match[1]) {
        documents = JSON.parse(match[1]);
      } else {
        console.error("No documents found in search file");
        documents = [];
      }
    })
    .catch((err) => {
      console.error("Failed to load search index:", err);
      documents = [];
    });
}

/* -----------------------------------------------------------
   Initialize Lunr (multi-language safe)
----------------------------------------------------------- */
function initLunr() {
  try {
    if (currentLang === 'ja' && typeof lunr.multiLanguage !== "undefined") {
      idx = lunr(function () {
        this.use(lunr.multiLanguage('ja', 'en'));
        this.ref('id');
        this.field('title', { boost: 10 });
        this.field('body');
        documents.forEach(function (doc) {
          this.add(doc);
        }, this);
      });
    } else {
      idx = lunr(function () {
        this.ref('id');
        this.field('title', { boost: 10 });
        this.field('body');
        documents.forEach(function (doc) {
          this.add(doc);
        }, this);
      });
    }
    console.log("Lunr initialized for:", currentLang);
  } catch (e) {
    console.error("Error initializing Lunr:", e);
  }
}

/* -----------------------------------------------------------
   Search function with modal result display
----------------------------------------------------------- */
function lunr_search(term) {
  if (!idx) {
    console.error("Lunr index not ready yet.");
    return false;
  }

  $('#lunrsearchresults').show(400);
  $("body").addClass("modal-open");

  document.getElementById('lunrsearchresults').innerHTML =
    '<div id="resultsmodal" class="modal fade show d-block" tabindex="-1" role="dialog" aria-labelledby="resultsmodal">' +
    '<div class="modal-dialog shadow" role="document">' +
    '<div class="modal-content">' +
    '<div class="modal-header" id="modtit">' +
    '<button type="button" class="close" id="btnx" data-dismiss="modal" aria-label="Close">&times;</button>' +
    '</div>' +
    '<div class="modal-body"><ul class="mb-0"></ul></div>' +
    '<div class="modal-footer"><button id="btnx" type="button" class="btn btn-primary btn-sm" data-dismiss="modal">Close</button></div>' +
    '</div></div></div>';

  if (term) {
    document.getElementById('modtit').innerHTML =
      `<h5 class='modal-title'>Search results for '${term}'</h5>` + document.getElementById('modtit').innerHTML;

    var results = idx.search(term);
    var resultsList = document.querySelector('#lunrsearchresults ul');

    if (results.length > 0) {
      for (var i = 0; i < results.length; i++) {
        var ref = results[i].ref;
        var doc = documents[ref];
        if (!doc) continue;

        var url = doc.url;
        var title = doc.title;
        var body = doc.body.substring(0, 160) + '...';

        resultsList.innerHTML +=
          `<li class='lunrsearchresult'>
             <a href='${url}'>
               <span class='title'>${title}</span>
               <small><span class='body'>${body}</span></small>
             </a>
           </li>`;
      }
    } else {
      resultsList.innerHTML = `<li class='lunrsearchresult'>No results found. Try another keyword.</li>`;
    }
  }
  return false;
}

/* -----------------------------------------------------------
   Modal Close Handler
----------------------------------------------------------- */
$(function () {
  $("#lunrsearchresults").on('click', '#btnx', function () {
    $('#lunrsearchresults').hide(5);
    $("body").removeClass("modal-open");
  });
});

/* -----------------------------------------------------------
   Boot sequence: load documents and build index
----------------------------------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
  loadDocuments().then(initLunr);
});

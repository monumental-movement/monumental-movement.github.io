/* ===========================================================
   Lunr Search Engine – Full Japanese/English Compatible
   =========================================================== */

var idx;
var documents = [];
var currentLang = window.location.pathname.startsWith('/en/') ? 'en' : 'ja';
var searchPath = currentLang === 'en' ? '/en/search.html' : '/search.html';

/* -----------------------------------------------------------
   Load index data
----------------------------------------------------------- */
function loadDocuments() {
  return fetch(searchPath)
    .then(res => res.text())
    .then(html => {
      const match = html.match(/var documents = (\[.*\]);/s);
      if (match && match[1]) {
        documents = JSON.parse(match[1]);
      } else {
        documents = [];
        console.error("No documents found in " + searchPath);
      }
    })
    .catch(err => {
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
      // ✅ Japanese + English tokenizer enabled
      idx = lunr(function () {
        this.use(lunr.multiLanguage('ja', 'en'));
        this.ref('id');
        this.field('title', { boost: 10 });
        this.field('body');
        documents.forEach(function (doc) {
          this.add(doc);
        }, this);
      });
      console.log("Lunr initialized in Japanese mode");
    } else {
      // English only
      idx = lunr(function () {
        this.ref('id');
        this.field('title', { boost: 10 });
        this.field('body');
        documents.forEach(function (doc) {
          this.add(doc);
        }, this);
      });
      console.log("Lunr initialized in English mode");
    }
  } catch (e) {
    console.error("Error initializing Lunr:", e);
  }
}

/* -----------------------------------------------------------
   Search execution + modal display
----------------------------------------------------------- */
function lunr_search(term) {
  if (!idx || !term) return false;

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

  document.getElementById('modtit').innerHTML =
    `<h5 class='modal-title'>Search results for '${term}'</h5>` + document.getElementById('modtit').innerHTML;

  var results = idx.search(term);
  var resultsList = document.querySelector('#lunrsearchresults ul');

  if (results.length > 0) {
    for (var i = 0; i < results.length; i++) {
      var ref = results[i].ref;
      var doc = documents[ref];
      if (!doc) continue;
      resultsList.innerHTML +=
        `<li class='lunrsearchresult'>
           <a href='${doc.url}'>
             <span class='title'>${doc.title}</span>
             <small><span class='body'>${doc.body.substring(0,160)}...</span></small>
           </a>
         </li>`;
    }
  } else {
    resultsList.innerHTML = `<li class='lunrsearchresult'>No results found. Try another keyword.</li>`;
  }

  return false;
}

/* -----------------------------------------------------------
   Modal close event
----------------------------------------------------------- */
$(function () {
  $("#lunrsearchresults").on('click', '#btnx', function () {
    $('#lunrsearchresults').hide(5);
    $("body").removeClass("modal-open");
  });
});

fetch('/search.html')
  .then(res => res.json())
  .then(data => {
    documents = data;
    initLunr();
  });
  
/* -----------------------------------------------------------
   Boot sequence
----------------------------------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
  loadDocuments().then(initLunr);
});

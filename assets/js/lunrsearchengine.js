/* ============================================================
   Lunr Search Engine (Stable Japanese/English Version)
   ============================================================ */

var idx = null;
var documents = [];
var currentLang = window.location.pathname.startsWith('/en/') ? 'en' : 'ja';
var searchIndexUrl = currentLang === 'en' ? '/en/search.html' : '/search.html';

/* ------------------------------------------------------------
   Wait until lunr & its plugins are ready
------------------------------------------------------------ */
function waitForLunrReady(callback) {
  if (typeof lunr !== 'undefined' && lunr.multiLanguage) {
    callback();
  } else {
    console.warn("Lunr not ready yet... retrying");
    setTimeout(function () {
      waitForLunrReady(callback);
    }, 300);
  }
}


/* ------------------------------------------------------------
   modal
------------------------------------------------------------ */

function lunr_search(term) {
  try {
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
        "<h5 class='modal-title'>Search results for '" + term + "'</h5>" +
        document.getElementById('modtit').innerHTML;

      var results = idx.search(term);
      var ul = document.querySelector('#lunrsearchresults ul');
      if (results.length > 0) {
        results.forEach(function (r) {
          var ref = r.ref;
          var d = documents[ref];
          var body = (d.body || '').substring(0, 160) + '...';
          ul.innerHTML +=
            "<li class='lunrsearchresult'><a href='" + d.url + "'>" +
            "<span class='title'>" + d.title + "</span>" +
            "<small><span class='body'>" + body + "</span><span class='url'>" + d.url + "</span></small></a></li>";
        });
      } else {
        ul.innerHTML = "<li class='lunrsearchresult'>Sorry, no results found. Close & try a different search!</li>";
      }
    }
  } catch (e) {
    console.error("Lunr modal error:", e);
  }

  return false;
}


/* ------------------------------------------------------------
   Load the index data
------------------------------------------------------------ */
function loadDocuments() {
  return fetch(searchIndexUrl, { cache: "no-store" })
    .then(res => {
      if (!res.ok) throw new Error("Index not found: " + searchIndexUrl);
      return res.text();
    })
    .then(text => {
      try {
        documents = JSON.parse(text);
        console.log("Loaded", documents.length, "documents from", searchIndexUrl);
      } catch (e) {
        console.error("Failed to parse search index JSON:", e);
        documents = [];
      }
    })
    .catch(err => {
      console.error("Failed to load search index:", err);
      documents = [];
    });
}

/* ------------------------------------------------------------
   Initialize Lunr
------------------------------------------------------------ */
function initLunr() {
  if (!documents || documents.length === 0) {
    console.warn("No documents to index.");
    return;
  }

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

  console.log("Lunr index built for", currentLang);
}

/* ------------------------------------------------------------
   Perform search
------------------------------------------------------------ */
function lunr_search(term) {
  if (!idx) {
    console.warn("Search index not ready yet.");
    return false;
  }

  const results = idx.search(term);
  const container = document.getElementById('lunrsearchresults');

  container.innerHTML = '<ul></ul>';
  const ul = container.querySelector('ul');

  if (results.length > 0) {
    results.forEach(r => {
      const doc = documents.find(d => d.id == r.ref);
      if (!doc) return;
      ul.innerHTML += `
        <li class="lunrsearchresult">
          <a href="${doc.url}">
            <span class="title">${doc.title}</span>
            <small><span class="body">${doc.body.substring(0,150)}...</span></small>
          </a>
        </li>`;
    });
  } else {
    ul.innerHTML = `<li>No results found. Try another keyword.</li>`;
  }
  return false;
}

/* ------------------------------------------------------------
   Initialize everything after page load
------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", function () {
  waitForLunrReady(function () {
    loadDocuments().then(initLunr);
  });
});

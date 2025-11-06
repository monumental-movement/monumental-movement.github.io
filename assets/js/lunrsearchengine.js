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

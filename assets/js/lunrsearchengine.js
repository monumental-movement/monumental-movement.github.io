/*!
 * lunrsearchengine.js (Multi-language + Modal, GitHub Pages safe)
 */

var documents = [];
var idx = null;

// --- 言語ごとに index URL を自動切り替え ---
function getSearchIndexUrl() {
  const base = "{{ site.baseurl }}";
  return window.location.pathname.startsWith(base + "/en/") 
         ? base + "/en/search.html" 
         : base + "/search.html";
}

// --- 現在のページ言語を判定 ---
function getCurrentLang() {
  const base = "{{ site.baseurl }}";
  return window.location.pathname.startsWith(base + "/en/") ? "en" : "ja";
}

// --- JSON 読み込み ---
async function loadDocuments() {
  const indexUrl = getSearchIndexUrl();
  console.log("🌐 Fetching index from:", indexUrl);

  try {
    const res = await fetch(indexUrl, { cache: "no-store" });
    if (!res.ok) throw new Error(res.status + " " + res.statusText);
    documents = await res.json();
    console.log(`✅ Loaded ${documents.length} documents from ${indexUrl}`);
  } catch (e) {
    console.error("❌ Failed to load search index:", e);
  }
}

// --- Lunr 初期化 ---
async function initLunr() {
  if (!documents.length) await loadDocuments();

  const currentLang = getCurrentLang();
  console.log("🌐 Current language:", currentLang);

  try {
    idx = lunr(function () {
      if (currentLang === "en") {
        this.use(lunr.multiLanguage("en"));
      } else {
        this.use(lunr.multiLanguage("ja","en"));
      }
      this.ref("id");
      this.field("title");
      this.field("body");

      documents.forEach((doc) => this.add(doc));
    });
    console.log("✅ Lunr index built for", currentLang);
  } catch (e) {
    console.error("❌ Lunr index build failed:", e);
  }
}

// --- 検索関数（モーダル付き） ---
function lunr_search(term) {
  console.log("🔍 Searching:", term);
  if (!idx) {
    console.warn("⚠️ Lunr not ready yet...");
    return false;
  }

  const resultBox = document.getElementById("lunrsearchresults");
  resultBox.style.display = "block";
  document.body.classList.add("modal-open");

  resultBox.innerHTML = `
    <div id="resultsmodal" class="modal fade show d-block" tabindex="-1" role="dialog">
      <div class="modal-dialog shadow" role="document">
        <div class="modal-content">
          <div class="modal-header" id="modtit">
            <h5 class="modal-title">Search results for '${term}'</h5>
            <button type="button" class="close" id="btnx" aria-label="Close">&times;</button>
          </div>
          <div class="modal-body"><ul class="mb-0"></ul></div>
          <div class="modal-footer">
            <button id="btnclose" type="button" class="btn btn-primary btn-sm">Close</button>
          </div>
        </div>
      </div>
    </div>
  `;

  const ul = resultBox.querySelector("ul");
  let results = [];

  if (term && term.trim().length > 0) {
    try {
      results = idx.search(term);
    } catch (e) {
      console.error("⚠️ Search error:", e);
    }
  }

  if (results.length > 0) {
    results.forEach(function (r) {
      const d = documents.find((doc) => String(doc.id) === String(r.ref));
      if (!d) return;
      const body = (d.body || "").substring(0, 160) + "...";
      ul.innerHTML += `
        <li class="lunrsearchresult">
          <a href="${d.url}">
            <span class="title">${d.title}</span>
            <small><span class="body">${body}</span><span class="url">${d.url}</span></small>
          </a>
        </li>`;
    });
  } else {
    ul.innerHTML = `<li class="lunrsearchresult">No results found. Try another keyword.</li>`;
  }

  return false;
}

// --- モーダルのクローズ処理 ---
$(document).on("click", "#btnx, #btnclose", function () {
  $("#lunrsearchresults").fadeOut(200);
  $("body").removeClass("modal-open");
});

// --- 起動時処理 ---
document.addEventListener("DOMContentLoaded", async () => {
  await loadDocuments();
  await initLunr();
});

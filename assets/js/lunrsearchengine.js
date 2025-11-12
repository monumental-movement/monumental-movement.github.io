/*!
 * lunrsearchengine.js (Fixed Modal + Multilingual)
 */

var documents = [];
var idx = null;

// --- 言語別 index URL ---
function getSearchIndexUrl() {
  return window.location.pathname.startsWith("/en/")
    ? "/en/search.html"
    : "/search.html";
}

// --- 現在のページ言語 ---
function getCurrentLang() {
  return window.location.pathname.startsWith("/en/") ? "en" : "ja";
}

// --- JSON 読み込み ---
async function loadDocuments() {
  const indexUrl = getSearchIndexUrl();
  try {
    const res = await fetch(indexUrl, { cache: "no-store" });
    if (!res.ok) throw new Error(res.statusText);
    documents = await res.json();
    console.log(`✅ Loaded ${documents.length} docs from ${indexUrl}`);
  } catch (e) {
    console.error("❌ Failed to load search index:", e);
  }
}

// --- Lunr 初期化 ---
async function initLunr() {
  if (!documents.length) await loadDocuments();

  const lang = getCurrentLang();
  console.log("🌐 Building Lunr index for:", lang);

  try {
    idx = lunr(function () {
      if (lang === "en") {
        this.use(lunr.en);
      } else {
        this.use(lunr.multiLanguage("ja", "en"));
      }
      this.ref("id");
      this.field("title");
      this.field("body");

      documents.forEach((doc) => this.add(doc));
    });
    console.log(`✅ Lunr index built (${lang})`);
  } catch (e) {
    console.error("❌ Lunr build failed:", e);
  }
}

// --- 検索（モーダル付き） ---
function lunr_search(term) {
  console.log("🔍 Searching:", term);
  if (!idx) {
    console.warn("⚠️ Lunr index not ready");
    return false;
  }

  const resultBox = document.getElementById("lunrsearchresults");
  resultBox.style.display = "block";
  document.body.classList.add("modal-open");

  resultBox.innerHTML = `
    <div id="resultsmodal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog shadow" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Search results for '${term}'</h5>
            <button type="button" class="close" id="btnx">&times;</button>
          </div>
          <div class="modal-body"><ul class="mb-0"></ul></div>
          <div class="modal-footer">
            <button id="btnclose" class="btn btn-primary btn-sm">Close</button>
          </div>
        </div>
      </div>
    </div>`;

  const ul = resultBox.querySelector("ul");
  let results = [];

  try {
    if (term && term.trim().length > 0) {
      results = idx.search(term);
    }
  } catch (e) {
    console.error("❌ Search failed:", e);
  }

  if (results.length > 0) {
    results.forEach((r) => {
      const d = documents.find((doc) => String(doc.id) === String(r.ref));
      if (!d) return;
      const body = (d.body || "").substring(0, 160) + "...";
      ul.innerHTML += `
        <li class="lunrsearchresult">
          <a href="${d.url}">
            <span class="title">${d.title}</span>
            <small><span class="body">${body}</span></small>
          </a>
        </li>`;
    });
  } else {
    ul.innerHTML = `<li>No results found.</li>`;
  }

  return false;
}

// --- モーダル閉じる ---
$(document).on("click", "#btnx, #btnclose", function () {
  $("#lunrsearchresults").fadeOut(200);
  $("body").removeClass("modal-open");
});

// --- 起動 ---
document.addEventListener("DOMContentLoaded", async () => {
  await loadDocuments();
  await initLunr();
});

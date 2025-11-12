/*!
 * lunrsearchengine.js (Modal Safe + Multi-language + GitHub Pages対応)
 */

var documents = [];
var idx = null;

// --- indexファイルの自動切り替え（確実に相対パスで動く） ---
function getSearchIndexUrl() {
  let path = window.location.pathname;
  if (path.includes("/en/")) {
    // 英語ページなら
    return window.location.origin + "/en/search.html";
  } else {
    // 日本語ページ
    return window.location.origin + "/search.html";
  }
}

// --- JSONロード ---
async function loadDocuments() {
  const indexUrl = getSearchIndexUrl();
  console.log("🌐 Trying to load search index from:", indexUrl);
  try {
    const res = await fetch(indexUrl, { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    documents = await res.json();
    console.log(`✅ Loaded ${documents.length} documents from ${indexUrl}`);
  } catch (e) {
    console.error("❌ Failed to load search index:", e);
  }
}

// --- Lunr初期化 ---
async function initLunr() {
  if (!documents.length) await loadDocuments();

  try {
    idx = lunr(function () {
      this.use(lunr.multiLanguage("en", "ja"));
      this.ref("id");
      this.field("title");
      this.field("body");
      documents.forEach((doc) => this.add(doc));
    });
    console.log("✅ Lunr index initialized.");
  } catch (e) {
    console.error("❌ Lunr initialization failed:", e);
  }
}

// --- 検索関数（モーダル付き） ---
function lunr_search(term) {
  console.log("🔍 Searching for:", term);
  if (!idx) {
    console.warn("⚠️ Lunr index not ready yet");
    return false;
  }

  const resultBox = document.getElementById("lunrsearchresults");
  if (!resultBox) {
    console.error("❌ #lunrsearchresults not found in HTML.");
    return false;
  }

  // モーダル生成
  resultBox.innerHTML = `
    <div id="resultsmodal" class="modal fade show d-block" tabindex="-1" role="dialog">
      <div class="modal-dialog shadow" role="document">
        <div class="modal-content">
          <div class="modal-header bg-dark text-white">
            <h5 class="modal-title">Search results for '${term}'</h5>
            <button type="button" class="close text-white" id="btnx">&times;</button>
          </div>
          <div class="modal-body"><ul class="mb-0"></ul></div>
          <div class="modal-footer">
            <button id="btnclose" class="btn btn-secondary btn-sm">Close</button>
          </div>
        </div>
      </div>
    </div>`;
  resultBox.style.display = "block";
  document.body.classList.add("modal-open");

  const ul = resultBox.querySelector("ul");
  let results = [];

  try {
    if (term && term.trim().length > 0) {
      results = idx.search(term);
    }
  } catch (e) {
    console.error("❌ Search error:", e);
  }

  if (results.length > 0) {
    results.forEach((r) => {
      const d = documents.find((doc) => String(doc.id) === String(r.ref));
      if (!d) return;
      const body = (d.body || "").substring(0, 160) + "...";
      ul.innerHTML += `
        <li class="lunrsearchresult">
          <a href="${d.url}">
            <strong>${d.title}</strong><br>
            <small>${body}</small>
          </a>
        </li>`;
    });
  } else {
    ul.innerHTML = `<li class="lunrsearchresult">No results found.</li>`;
  }

  return false;
}

// --- モーダルを閉じる ---
$(document).on("click", "#btnx, #btnclose", function () {
  $("#lunrsearchresults").fadeOut(200);
  $("body").removeClass("modal-open");
});

// --- 初期化 ---
document.addEventListener("DOMContentLoaded", async () => {
  console.log("🚀 Initializing LunrSearch...");
  await loadDocuments();
  await initLunr();
});

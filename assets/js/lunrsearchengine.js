/*!
 * lunrsearchengine.js (Japanese + English, modal style)
 * Works with: lunr.js / lunr.stemmer.support.js / lunr.ja.js / lunr.multi.js / tiny-segmenter.js
 */

var documents = [];
var idx = null;

// --- JSON 読み込み ---
async function loadDocuments() {
  try {
    const res = await fetch("/search.html");
    documents = await res.json();
    console.log("✅ Loaded", documents.length, "documents from /search.html");
  } catch (e) {
    console.error("❌ Failed to load search index:", e);
  }
}

// --- Lunr 初期化 ---
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
    console.log("✅ Lunr index built with multiLanguage (en, ja)");
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

  try {
    const resultBox = document.getElementById("lunrsearchresults");
    resultBox.style.display = "block";
    document.body.classList.add("modal-open");

    // モーダルHTML構築
    resultBox.innerHTML = `
      <div id="resultsmodal" class="modal fade show d-block" tabindex="-1" role="dialog" aria-labelledby="resultsmodal">
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
      results = idx.search(term);
    }

    if (results.length > 0) {
      results.forEach(function (r) {
        console.log("📄 Hit ref:", r.ref);
        const d = documents.find((doc) => String(doc.id) === String(r.ref));
        console.log("📄 Matched doc:", d);
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
  } catch (e) {
    console.error("⚠️ lunr_search() error:", e);
  }

  return false;
}

// --- モーダルのクローズ処理 ---
$(document).on("click", "#btnx, #btnclose", function () {
  $("#lunrsearchresults").hide(200);
  $("body").removeClass("modal-open");
});

// --- 起動時処理 ---
document.addEventListener("DOMContentLoaded", async () => {
  await loadDocuments();
  await initLunr();
});

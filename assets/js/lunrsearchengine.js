var documents = [];
var idx = null;

// --- 言語・パス自動判定 ---
function getSearchIndexUrl() {
  const path = window.location.pathname;
  return path.includes("/en/") ? SEARCH_INDEX_EN : SEARCH_INDEX_DEFAULT;
}


// --- JSON 読み込み ---
async function loadDocuments() {
  const indexUrl = getSearchIndexUrl();
  console.log("🌐 Fetching index from:", indexUrl);

  try {
    const res = await fetch(indexUrl, { cache: "no-store" });
    if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
    documents = await res.json();
    console.log(`✅ Loaded ${documents.length} documents from ${indexUrl}`);
  } catch (e) {
    console.error("❌ Failed to load search index:", e);
  }
}

// --- Lunr 初期化 ---
async function initLunr() {
  if (!documents.length) await loadDocuments();

  console.log("🌐 Building Lunr index...");
  try {
    idx = lunr(function () {
      this.use(lunr.multiLanguage("en", "ja"));
      this.ref("id");
      this.field("title");
      this.field("body");

      documents.forEach((doc) => {
        if (doc.title && doc.body) this.add(doc);
      });
    });
    console.log("✅ Lunr index built with multiLanguage(en, ja)");
  } catch (e) {
    console.error("❌ Lunr index build failed:", e);
  }
}

// --- 検索実行 ---
function lunr_search(term) {
  if (!idx) return false;

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
    if (term && term.trim().length > 0) results = idx.search(term);
  } catch (e) {
    console.error("❌ Search error:", e);
  }

  if (!documents.length) {
    ul.innerHTML = `<li>⚠️ No index loaded. Please refresh.</li>`;
    return false;
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
    ul.innerHTML = `<li>No results found. Try another keyword.</li>`;
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

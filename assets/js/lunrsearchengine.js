/*!
 * lunrsearchengine.js (Multi-language + Modal)
 * Fixed: search.html is HTML, not pure JSON
 */

var documents = [];
var idx = null;

// --- 現在のページ言語を判定 ---
function getCurrentLang() {
  if (window.location.pathname.startsWith("/en/")) return "en";
  if (window.location.pathname.startsWith("/de/")) return "de";
  if (window.location.pathname.startsWith("/es/")) return "es";
  if (window.location.pathname.startsWith("/ko/")) return "ko";
  if (window.location.pathname.startsWith("/zh-hant/")) return "zh-hant";
  if (window.location.pathname.startsWith("/fr/")) return "fr";
  return "ja";
}

// --- search.html のURLを決定 ---
function getSearchIndexUrl() {
  if (window.location.pathname.startsWith("/en/")) return "/en/search.html";
  if (window.location.pathname.startsWith("/de/")) return "/de/search.html";
  if (window.location.pathname.startsWith("/es/")) return "/es/search.html";
  if (window.location.pathname.startsWith("/ko/")) return "/ko/search.html";
  if (window.location.pathname.startsWith("/zh-hant/")) return "/zh-hant/search.html";
  if (window.location.pathname.startsWith("/fr/")) return "/fr/search.html";
  return "/search.html";
}

// --- search.html から JSON 配列だけを抽出して読み込む ---
async function loadDocuments() {
  const indexUrl = getSearchIndexUrl();

  try {
    const res = await fetch(indexUrl, { cache: "no-store" });
    const text = await res.text();

    // search.html 内の [ { ... } ] を抜き出す
    const match = text.match(/\[\s*{[\s\S]*?}\s*\]/);

    if (!match) {
      console.error("❌ No JSON array found in", indexUrl);
      documents = [];
      return;
    }

    documents = JSON.parse(match[0]);
    console.log(`✅ Loaded ${documents.length} documents from ${indexUrl}`);
  } catch (e) {
    console.error("❌ Failed to load search index:", e);
    documents = [];
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
      } else if (currentLang === "de") {
        this.use(lunr.multiLanguage("de", "en"));
      } else if (currentLang === "es") {
        this.use(lunr.multiLanguage("es", "en"));
      } else if (currentLang === "ko") {
        this.use(lunr.multiLanguage("ko", "en"));
      } else if (currentLang === "zh-hant") {
        this.use(lunr.multiLanguage("zh", "en"));
      } else if (currentLang === "fr") {
        this.use(lunr.multiLanguage("fr", "en"));
      } else {
        this.use(lunr.multiLanguage("ja", "en"));
      }

      this.ref("id");
      this.field("title");
      this.field("body");

      documents.forEach((doc) => this.add(doc));
    });

    console.log("✅ Lunr index built");
  } catch (e) {
    console.error("❌ Lunr index build failed:", e);
  }
}

// --- 検索実行 ---
function lunr_search(term) {
  if (!idx) {
    console.warn("⚠️ Lunr not ready yet");
    return false;
  }

  const resultBox = document.getElementById("lunrsearchresults");
  resultBox.style.display = "block";
  document.body.classList.add("modal-open");

  resultBox.innerHTML = `
    <div id="resultsmodal" class="modal fade show d-block">
      <div class="modal-dialog shadow">
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
    </div>
  `;

  const ul = resultBox.querySelector("ul");
  let results = [];

  if (term && term.trim()) {
    try {
      results = idx.search(term);
    } catch (e) {
      console.error("⚠️ Search error:", e);
    }
  }

  if (results.length) {
    results.forEach((r) => {
      const d = documents.find((doc) => String(doc.id) === String(r.ref));
      if (!d) return;

      const body = (d.body || "").substring(0, 160) + "...";
      ul.innerHTML += `
        <li class="lunrsearchresult">
          <a href="${d.url}">
            <span class="title">${d.title}</span>
            <small>
              <span class="body">${body}</span>
              <span class="url">${d.url}</span>
            </small>
          </a>
        </li>`;
    });
  } else {
    ul.innerHTML = `<li class="lunrsearchresult">No results found.</li>`;
  }

  return false;
}

// --- モーダルクローズ ---
$(document).on("click", "#btnx, #btnclose", function () {
  $("#lunrsearchresults").fadeOut(200);
  $("body").removeClass("modal-open");
});

// --- 起動 ---
document.addEventListener("DOMContentLoaded", async () => {
  await loadDocuments();
  await initLunr();
});

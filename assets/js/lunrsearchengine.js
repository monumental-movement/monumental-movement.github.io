/*!
 * lunrsearchengine.js (Multi-language + Modal)
 * Fixed: no jQuery / safe language handling
 */

var documents = [];
var idx = null;

// --- 現在のページ言語を判定 ---
function getCurrentLang() {
  if (location.pathname.startsWith("/en/")) return "en";
  if (location.pathname.startsWith("/de/")) return "de";
  if (location.pathname.startsWith("/es/")) return "es";
  if (location.pathname.startsWith("/ko/")) return "ko";
  if (location.pathname.startsWith("/zh-hant/")) return "zh-hant";
  if (location.pathname.startsWith("/fr/")) return "fr";
  return "ja";
}

// --- search.html URL ---
function getSearchIndexUrl() {
  if (location.pathname.startsWith("/en/")) return "/en/search.html";
  if (location.pathname.startsWith("/de/")) return "/de/search.html";
  if (location.pathname.startsWith("/es/")) return "/es/search.html";
  if (location.pathname.startsWith("/ko/")) return "/ko/search.html";
  if (location.pathname.startsWith("/zh-hant/")) return "/zh-hant/search.html";
  if (location.pathname.startsWith("/fr/")) return "/fr/search.html";
  return "/search.html";
}

// --- search.html から JSON 抽出 ---
async function loadDocuments() {
  try {
    const res = await fetch(getSearchIndexUrl(), { cache: "no-store" });
    const text = await res.text();
    const match = text.match(/\[\s*{[\s\S]*?}\s*\]/);

    if (!match) {
      console.error("❌ No JSON array found");
      documents = [];
      return;
    }

    documents = JSON.parse(match[0]);
    console.log(`✅ Loaded ${documents.length} documents`);
  } catch (e) {
    console.error("❌ Failed to load documents", e);
    documents = [];
  }
}

// --- Lunr 初期化 ---
async function initLunr() {
  if (!documents.length) await loadDocuments();

  try {
    idx = lunr(function () {
      // 🔒 実在する tokenizer のみ使用
      if (getCurrentLang() === "ja") {
        this.use(lunr.multiLanguage("ja"));
      } else {
        this.use(lunr.multiLanguage("en"));
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

// --- 検索 ---
function lunr_search(term) {
  if (!idx) return false;

  const box = document.getElementById("lunrsearchresults");
  box.style.display = "block";
  document.body.classList.add("modal-open");

  box.innerHTML = `
    <div class="modal fade show d-block">
      <div class="modal-dialog shadow">
        <div class="modal-content">
          <div class="modal-header">
            <h5>Search results for '${term}'</h5>
            <button id="btnx">&times;</button>
          </div>
          <div class="modal-body"><ul></ul></div>
          <div class="modal-footer">
            <button id="btnclose">Close</button>
          </div>
        </div>
      </div>
    </div>
  `;

  const ul = box.querySelector("ul");
  const results = term ? idx.search(term) : [];

  ul.innerHTML = results.length
  ? results.map(r => {
      const d = documents.find(doc => String(doc.id) === r.ref);
      if (!d) return "";

      return `
        <li class="search-item">
          <a href="${d.url}">
            <div class="search-title">${d.title}</div>
            <div class="search-body">
              ${(d.body || "").slice(0, 140)}…
            </div>
            <div class="search-url">${d.url}</div>
          </a>
        </li>
      `;
    }).join("")
  : `<li class="search-empty">No results found.</li>`;

  return false;
}

// --- モーダル close（純JS） ---
document.addEventListener("click", (e) => {
  if (e.target.id === "btnx" || e.target.id === "btnclose") {
    document.getElementById("lunrsearchresults").style.display = "none";
    document.body.classList.remove("modal-open");
  }
});

// --- 起動 ---
document.addEventListener("DOMContentLoaded", async () => {
  await loadDocuments();
  await initLunr();
});

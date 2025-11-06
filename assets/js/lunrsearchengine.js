function lunr_search(term) {
  console.log("🔍 Searching:", term);

  // 安全ガード（他スクリプトの干渉回避）
  try {
    // 検索ウィンドウを初期化
    const resultBox = document.getElementById("lunrsearchresults");
    resultBox.style.display = "block";
    document.body.classList.add("modal-open");

    // モーダルHTMLを生成
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

    // 検索処理
    if (term && term.trim().length > 0) {
      results = idx.search(term);
    }

    if (results.length > 0) {
      results.forEach(function (r) {
        const ref = r.ref;
        const d = documents[ref];
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

    // 閉じるボタンの動作
    $("#lunrsearchresults").off("click", "#btnx");
    $("#lunrsearchresults").on("click", "#btnx", function () {
      $("#lunrsearchresults").hide(200);
      $("body").removeClass("modal-open");
    });

    $("#lunrsearchresults").off("click", "#btnclose");
    $("#lunrsearchresults").on("click", "#btnclose", function () {
      $("#lunrsearchresults").hide(200);
      $("body").removeClass("modal-open");
    });
  } catch (e) {
    console.error("⚠️ lunr_search() error:", e);
  }

  return false;
}

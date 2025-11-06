/*!
 * TinySegmenter 0.2 (for Lunr.js Japanese support)
 * MIT Licensed
 * https://github.com/takuyaa/tiny-segmenter
 */
var TinySegmenter = (function () {
  function TinySegmenter() {
    this.BIAS__ = -332;
    this.BC1__ = { "AA": -294, "AI": -327, "AN": 451, "AO": 97, "A!": -123, "A?": -230 };
    this.BC2__ = { "AA": 295, "AI": -26, "AN": -25, "AO": -356, "A!": -70, "A?": -54 };
    this.BC3__ = { "AA": 2, "AI": 16, "AN": -141, "AO": -88, "A!": -104, "A?": -100 };
    this.UP1__ = { "M": -212, "H": -233, "I": 109, "K": -34, "O": 5 };
    this.UP2__ = { "A": -295, "H": -77, "I": 27, "K": 57, "O": -45 };
    this.UP3__ = { "A": -276, "H": 34, "I": 4, "K": 76, "O": -55 };
    this.BP1__ = { "A": -211, "H": -240, "I": 11, "K": 18, "O": 43 };
    this.BP2__ = { "A": -183, "H": -53, "I": 13, "K": 19, "O": 18 };
    this.BP3__ = { "A": -165, "H": -50, "I": 15, "K": 6, "O": 18 };
  }

  TinySegmenter.prototype.chartype_ = function (c) {
    if (c.match(/[一-龠々〆ヵヶ]/)) return "H";
    if (c.match(/[ぁ-ん]/)) return "I";
    if (c.match(/[ァ-ヴーｱ-ﾝﾞｰ]/)) return "K";
    if (c.match(/[a-zA-Zａ-ｚＡ-Ｚ]/)) return "A";
    if (c.match(/[0-9０-９]/)) return "N";
    return "O";
  };

  TinySegmenter.prototype.segment = function (input) {
    var result = [];
    if (!input || input.length === 0) return result;
    var seg = ["B3", "B2", "B1"];
    for (var i = 0; i < input.length; i++) seg.push(input.charAt(i));
    seg.push("E1"); seg.push("E2"); seg.push("E3");

    var ch = [];
    for (i = 0; i < seg.length; i++) ch.push(this.chartype_(seg[i]));

    var word = seg[3];
    var score = 0;
    for (i = 4; i < seg.length - 3; i++) {
      score = this.BIAS__;
      var p1 = ch[i - 3] + ch[i - 2];
      var p2 = ch[i - 2] + ch[i - 1];
      var p3 = ch[i - 1] + ch[i];
      if (this.BC1__[p1]) score += this.BC1__[p1];
      if (this.BC2__[p2]) score += this.BC2__[p2];
      if (this.BC3__[p3]) score += this.BC3__[p3];
      if (this.UP1__[ch[i - 1]]) score += this.UP1__[ch[i - 1]];
      if (this.UP2__[ch[i]]) score += this.UP2__[ch[i]];
      if (this.UP3__[ch[i + 1]]) score += this.UP3__[ch[i + 1]];
      if (this.BP1__[ch[i - 1]]) score += this.BP1__[ch[i - 1]];
      if (this.BP2__[ch[i - 2]]) score += this.BP2__[ch[i - 2]];
      if (this.BP3__[ch[i - 3]]) score += this.BP3__[ch[i - 3]];
      if (score > 0) {
        result.push(word);
        word = "";
      }
      word += seg[i];
    }
    if (word) result.push(word);
    return result;
  };

  return TinySegmenter;
})();

// ✅ Lunr.js で参照できるように登録
if (typeof lunr !== "undefined") {
  lunr.TinySegmenter = TinySegmenter;
}

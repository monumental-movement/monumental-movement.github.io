---
layout: page
title: お問合せ
permalink: /contact
comments: false
---

<form action="https://formspree.io/{{site.email}}" method="POST">    
<p class="mb-4">何かご質問などがございましたら、 {{site.name}}までお気軽にお問い合わせください。</p>
<div class="form-group row">
<div class="col-md-6">
<input class="form-control" type="text" name="name" placeholder="お名前*" required>
</div>
<div class="col-md-6">
<input class="form-control" type="email" name="_replyto" placeholder="Eメールアドレス*" required>
</div>
</div>
<textarea rows="8" class="form-control mb-3" name="message" placeholder="メッセージ*" required></textarea>    
<input class="btn btn-dark" type="submit" value="send">
</form>
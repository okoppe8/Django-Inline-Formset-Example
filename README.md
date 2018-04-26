# Django-Inline-Formset-Example

Simple Invoice Entry App

Django-Inline-Formset-Example のサンプルコードです。
簡単な注文登録アプリケーションになっています。

紹介記事：[Python] Djangoで注文アプリケーションを作る（inline-formsets 使用方法）
https://github.com/okoppe8/Django-Inline-Formset-Example

以下のコードで実行可能です。（Windows用）

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py createsuperuser 
manage.py runserver
manage.py loaddata fixture/item.json
```

作成にあたっては以下のリポジトリを参考にしました。
[epicserve:Django Inline Formset Example]
https://github.com/epicserve/inlineformset-example

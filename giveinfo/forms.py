from django import forms

class SubmitForm(forms.Form):
    your_name = forms.CharField(label="お名前（ペンネーム可）", max_length=100, required=True)
    email = forms.EmailField(label="メールアドレス（必須）", required=True)
    dislike = forms.CharField(label="チュービンゲンでの苦い思い出を簡単に！（任意）", widget=forms.Textarea, required=False)
    like = forms.CharField(label="チュービンゲンでの楽しい思い出を簡単に！（任意）", widget=forms.Textarea, required=False)
    others = forms.CharField(label="その他の投稿文・ご意見をいくらでも！（任意）", widget=forms.Textarea, required=False)
    cc_myself = forms.BooleanField(label="提出した内容を自分にも送る（送るならチェック）", required=False)
    agree = forms.BooleanField(label="投稿された内容を掲載してもいいですか？（よければチェック）", required=False)

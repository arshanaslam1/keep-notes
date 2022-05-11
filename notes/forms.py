from django import forms
from notes.models import Notes


class NoteForm(forms.ModelForm):
    title = forms.CharField(required=True, label=False,
                            widget=forms.Textarea(
                                attrs={"rows": "4",
                                       "placeholder": "Write title here . . ."
                                       }
                            )
                            )

    body = forms.CharField(required=True, label=False,
                           widget=forms.Textarea(
                               attrs={
                                   "rows": "6",
                                   "placeholder": "Write note here . . ."
                               }
                           )
                           )

    class Meta:
        model = Notes
        fields = ('title', 'body')

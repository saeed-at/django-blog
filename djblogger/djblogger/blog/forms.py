from django import forms


class PostSearchForm(forms.Form):
    """
    This form provides a single search field that allows users to enter
    search queries for filtering blog posts.

    Parameters
    ----------
    forms.Form : django.forms.Form
        Inherits from Django's base Form class

    Attributes
    ----------
    q : forms.CharField
        The search query field that users will input their search terms into, the q parameter will be use to generate urls like below:
        localhost:8000/tags/?q=python
    """

    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        """
        Extends the parent Form initialization and adds Bootstrap styling
        to the search input field.

        Parameters
        ----------
        *args : tuple
            Variable length argument list
        **kwargs : dict
            Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)

        # Add Bootstrap's form-control class to the search input field
        self.fields["q"].widget.attrs.update({"class": "form-control"})

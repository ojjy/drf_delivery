from django import forms
from .models import Customereq

class CustomereqForm(forms.ModelForm):
    class Meta:
        model=Customereq
        fields=['sender_name', 'sender_address', 'sender_detailAddress', 'sender_extraAddress', 'sender_postcode', 'receiver_name', 'receiver_address', 'receiver_detailAddress', 'receiver_extraAddress', 'receiver_postcode', 'items', 'request_message', 'dam_request_id']
        widgets={
            'sender_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'보내는 사람', 'aria-label':'sender_name', 'aria-describedby':'basic-addon1','value':'보내는 사람'}),
            'sender_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'보내는 사람 주소', 'id':'sender_address','aria-label':'sender_address', 'aria-describedby':'basic-addon1','value':'서울시 강남구 학동로 212'}),
            'sender_detailAddress':forms.TextInput(attrs={'class':'form-control', 'placeholder':'상세주소','id':'sender_detailAddress','aria-label':'sender_detailAddress', 'aria-describedby':'basic-addon1','value':'703호'}),
            'sender_extraAddress': forms.TextInput(attrs={'class':'form-control','placeholder': '참고항목','id':'sender_extraAddress','aria-label':'sender_extraAddress', 'aria-describedby':'basic-addon1','value':'논현동'}),
            'sender_postcode': forms.TextInput(attrs={'class':'form-control','placeholder': '우편번호','id':'sender_postcode','aria-label':'sender_postcode', 'aria-describedby':'basic-addon1','value':'00000'}),
            'receiver_name': forms.TextInput(attrs={'class':'form-control','placeholder': '받는사람','id':'receiver_name','aria-label':'receiver_name', 'aria-describedby':'basic-addon1','value':'받는사람'}),
            'receiver_address': forms.TextInput(attrs={'class':'form-control','placeholder': '받는 사람 주소','id':'receiver_address','aria-label':'receiver_address', 'aria-describedby':'basic-addon1','value':'서울시 노원구 월계1동 68-80'}),
            'receiver_detailAddress': forms.TextInput(attrs={'class':'form-control','placeholder': '상세주소','id':'receiver_detailAddress','aria-label':'receiver_detailAddress', 'aria-describedby':'basic-addon1','value':'뒷집'}),
            'receiver_extraAddress': forms.TextInput(attrs={'class':'form-control','placeholder': '참고항목','id':'receiver_extraAddress','aria-label':'receiver_extraAddress', 'aria-describedby':'basic-addon1','value':'월계1동'}),
            'receiver_postcode': forms.TextInput(attrs={'class':'form-control','placeholder': '우편번호','id':'receiver_postcode','aria-label':'receiver_postcode', 'aria-describedby':'basic-addon1','value':'01902'}),
            'items': forms.TextInput(attrs={'class':'form-control','placeholder': '보내는 물건','id':'items','aria-label':'items', 'aria-describedby':'basic-addon1','value':'이사짐'}),
            'request_message': forms.Textarea(attrs={'class':'form-control','placeholder': '요청사항','id':'request_message','aria-label':'request_message', 'aria-describedby':'basic-addon1'}),
            'dam_request_id': forms.HiddenInput(),
        }
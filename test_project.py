from project import CHOICE_QUAL_VID,CHOICE_QUAL_AUD,VALID_VID_URL
import builtins

def iv(prompt=None):
    return iv.value

def ia(prompt=None):
    return ia.value

def test_qual_vid():
    iv.value="1"
    builtins.input=iv
    assert CHOICE_QUAL_VID()=="bestvideo+bestaudio/best"
    iv.value="2"
    builtins.input=iv
    assert CHOICE_QUAL_VID()=="bestvideo[height<=720]+bestaudio/best[height<=720]"
    iv.value="24"
    builtins.input=iv
    assert CHOICE_QUAL_VID()=="bestvideo+bestaudio/best"

def test_qual_aud():
    ia.value="1"
    builtins.input=ia
    assert CHOICE_QUAL_AUD()=="bestaudio/best"
    ia.value="2"
    builtins.input=ia
    assert CHOICE_QUAL_AUD()== "bestaudio[abr<=128]/worstaudio"
    ia.value="qae"
    builtins.input=ia
    assert CHOICE_QUAL_AUD()=="bestaudio/best"

def test_valid_url():
    assert VALID_VID_URL("hehee")==False
    assert VALID_VID_URL("www.google.com")==True
    assert VALID_VID_URL("https://www.youtube.com/watch?v=0RpKc55SA5Q")==True

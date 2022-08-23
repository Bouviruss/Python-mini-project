from urllib.request import urlopen
from bs4 import BeautifulSoup

site = "[insert name of the site]"
html = urlopen("https://mobile.facebook.com/100007380371214/posts/pcb.2485604481695540/?photo_id=2485604281695560&mds=%2Fphotos%2Fviewer%2F%3Fphotoset_token%3Dpcb.2485604481695540%26photo%3D2485604281695560%26profileid%3D100002743939549%26source%3D48%26refid%3D18%26_ft_%3Dqid.-6170607206087022721%253Amf_story_key.615949289676729%253Atop_level_post_id.615949289676729%253Atl_objid.615949289676729%253Acontent_owner_id_new.100007380371214%253Aoriginal_content_id.2485604481695540%253Aoriginal_content_owner_id.100007380371214%253Apage_id.166779504593712%253Asrc.22%253Astory_location.6%253Aattached_story_attachment_style.album%253Afilter.GroupStoriesByActivityEntQuery%253Aott.AX9rnyFP_TGlZZ65%253Aattached_story_type.EntStatusCreationStory%253Aattached_story_attachment_type.PhotoSetAttachment%253Apage_insights.%257B%2522166779504593712%2522%253A%257B%2522page_id%2522%253A166779504593712%252C%2522page_id_type%2522%253A%2522group%2522%252C%2522actor_id%2522%253A100007380371214%252C%2522dm%2522%253A%257B%2522isShare%2522%253A1%252C%2522originalPostOwnerID%2522%253A2485604481695540%257D%252C%2522psn%2522%253A%2522EntGroupMallPostCreationStory%2522%252C%2522post_context%2522%253A%257B%2522object_fbtype%2522%253A657%252C%2522publish_time%2522%253A1640880474%252C%2522story_name%2522%253A%2522EntGroupMallPostCreationStory%2522%252C%2522story_fbid%2522%253A[615949289676729]%257D%252C%2522role%2522%253A1%252C%2522sl%2522%253A6%257D%257D%253Aactrs.100007380371214%253Atds_flgs.3%253Aftmd_400706.111111l%26__tn__%3DEHH-R%26cached_data%3Dfalse%26ftid%3D&mdp=1&mdf=1")
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all("div", {"class": "_i81 _7buy"})
for img in images:
    if img.has_attr('src'):
        print(images)
import requests
import urllib.parse


Headers = {
    'Accept': '*/*', 
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Content-Type': 'application/json',
    'Cookie': 'guest_id=v1%3A169526252327425033; _ga=GA1.2.820292769.1695262522; guest_id_marketing=v1%3A169526252327425033; guest_id_ads=v1%3A169526252327425033; g_state={"i_l":0}; kdt=qemGr1mAl6BpZdTyhJBWk77cxDZxpr7dL8rV7Tu8; auth_token=2cc99649d330dc04e02a33c8e4c2b3b8f7f8ebe1; ct0=92a8306937b93ee2ddfa43de387aadf5499c5f832f6168be65352b3d4206ac10d24766728d467ab66181c35469862976c20420085cbd03c8b8f78ad2d247c74a68cae6b6e1e3efbb842ac1a51a03f9e5; twid=u%3D1704685048996429824; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ2Bb5t0uKS%2F7M%2FLHajVsdsE%3D|0|8e8t2xd8A2w%3D; _gid=GA1.2.1998198342.1699333198; personalization_id="v1_5MLMrdGcW2uE96YAzaCf3g=="',
    'Referer':'https://twitter.com/search?q=%EC%A7%80%EB%93%9C%EB%9E%98%EA%B3%A4&src=typed_query&f=live',
    'Sec-Ch-Ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="118"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36',
    'X-Client-Transaction-Id': 'NDnOTsjBtrdwpvl/9NXu8A0THyjstkXYoy4CDIBknwrkNtLlxxunIHWMrOWfoAjePwlXzjR6fMW5Dtczfz8iXOtd6WihNQ',
    'X-Client-Uuid': '51525061-27b9-437e-854d-43daf99f8b4f',
    'X-Csrf-Token': '92a8306937b93ee2ddfa43de387aadf5499c5f832f6168be65352b3d4206ac10d24766728d467ab66181c35469862976c20420085cbd03c8b8f78ad2d247c74a68cae6b6e1e3efbb842ac1a51a03f9e5',
    'X-Twitter-Active-User': 'yes',
    'X-Twitter-Auth-Type': 'OAuth2Session',
    'X-Twitter-Client-Language': 'en'
}

url = 'https://twitter.com/i/api/graphql/lZ0GCEojmtQfiUQa5oJSEw/SearchTimeline?variables=%7B%22rawQuery%22%3A%22%EC%A7%80%EB%93%9C%EB%9E%98%EA%B3%A4%22%2C%22count%22%3A20%2C%22cursor%22%3A%22DAADDAABCgABF-TokcSboO8KAAIX5Oc1gVvQuAAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUX5OiTBEAnEAoABhfk6JMEP9jwAAA%22%2C%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22Latest%22%7D&features=%7B%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_home_pinned_timelines_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Afalse%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'

response = requests.get(url, headers=Headers)
# print(response.text) # json 형태의 데이터가 그대로 나옴
print(response.json()) # 딕셔너리 형태로 가져옴

# print(urllib.parse.quote("지드래곤"))


for tweet in response.json()['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]['entries']:
    try:
        print(tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'].replace('\n',''))
    except:
        pass

    cursor = response.json()['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][-1]['entry']['content']['value']
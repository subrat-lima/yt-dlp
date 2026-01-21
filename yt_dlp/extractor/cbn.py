from .common import InfoExtractor
from ..utils import (
    extract_attributes,
)
from ..utils.traversal import (
    find_element,
    traverse_obj,
)


class CBNBaseIE(InfoExtractor):
    _ACCOUNT_ID = '734546207001'
    _PLAYER_ID = 'TADSYViJy'
    _EMBED = 'default'

    def _extract_brightcove(self, video_id):
        return {
            '_type': 'url_transparent',
            'url': f'https://players.brightcove.net/{self._ACCOUNT_ID}/{self._PLAYER_ID}_{self._EMBED}/index.html?videoId={video_id}',
            'ie_key': 'BrightcoveNew',
        }


class CBNIE(CBNBaseIE):
    IE_NAME = 'cbn'
    _VALID_URL = r'https?://(?:www\.)?cbn\.com/video/(?:[^/?#]+/)?(?P<id>[^/?&#]+)'

    _TESTS = [{
        'url': 'https://cbn.com/video/shows/faith-nation-january-20-2026',
        'info_dict': {
            'id': '6388008634112',
            'ext': 'mp4',
            'title': 'Faith Nation: January 20, 2026',
            'timestamp': 1768948577,
            'description': 'md5:f5a2886dfb7e00f44f39cbe280863bba',
            'upload_date': '20260120',
            'uploader_id': '734546207001',
            'duration': 1710.059,
            'thumbnail': r're:https?://.*\.(jpg|jpeg)',
            'tags': list,
        },
    }, {
        'url': 'https://cbn.com/video/stories/newsmakers-israel-chaos-and-deception-last-days-1826',
        'info_dict': {
            'id': '6387447294112',
            'ext': 'mp4',
            'title': 'Newsmakers: Israel, Chaos and Deception in the Last Days 1/8/26',
            'timestamp': 1767925448,
            'description': 'md5:1be4e6cad7a2fcc211da0cbd2c379e91',
            'upload_date': '20260109',
            'uploader_id': '734546207001',
            'duration': 1710.059,
            'thumbnail': r're:https?://.*\.(jpg|jpeg)',
            'tags': list,
        },
    }, {
        'url': 'https://cbn.com/video/news/exploring-marketplace-episode21-kim-avery',
        'info_dict': {
            'id': '6313599036112',
            'ext': 'mp4',
            'title': 'Exploring The Marketplace - Episode#21 - Kim Avery',
            'timestamp': 1665364860,
            'description': 'md5:13d14fd4835f96e12f46bc7afcc0e4a8',
            'upload_date': '20221010',
            'uploader_id': '734546207001',
            'duration': 1710.059,
            'thumbnail': r're:https?://.*\.(jpg|jpeg)',
            'tags': list,
        },
    }, {
        'url': 'https://cbn.com/video/vida-dura-529',
        'info_dict': {
            'id': '6140275877001',
            'ext': 'mp4',
            'title': 'Vida Dura # 529',
            'timestamp': 1583878397,
            'description': 'md5:8af1a15400f7249dff333c3df4d19b7b',
            'upload_date': '20200310',
            'uploader_id': '734546207001',
            'duration': 1714.513,
            'thumbnail': r're:https?://.*\.(jpg|jpeg)',
            'tags': list,
        },
    }]

    def _real_extract(self, url):
        display_id = self._match_id(url)
        webpage = self._download_webpage(url, display_id)
        video_id = traverse_obj(webpage, (
            {find_element(tag='video-js', attr='id', value=r'player-\d+', html=True, regex=True)},
            {extract_attributes}, 'data-video-id', {str}))
        return self._extract_brightcove(video_id)


class CBNFamilyIE(CBNBaseIE):
    IE_NAME = 'cbnfamily'
    _VALID_URL = r'https?://(?:www\.)?secure\.cbn\.com/partners/video/(shows|impactstories)/[^/?#]+/(?P<id>[^/?&#]+)'

    _TESTS = [{
        'url': 'https://secure.cbn.com/partners/video/shows/miraclelivingtoday/6365325644112',
        'info_dict': {
            'id': '6365325644112',
            'ext': 'mp4',
            'title': 'Miracle Living Today - November 30, 2024',
            'timestamp': 1732886296,
            'description': 'md5:eccc5d55ae759d4c881e86e2875d68ae',
            'upload_date': '20241129',
            'uploader_id': '734546207001',
            'duration': 1710.72,
            'thumbnail': r're:https?://.*\.(jpg|jpeg)',
            'tags': list,
        },
    }, {
        'url': 'https://secure.cbn.com/partners/video/impactstories/salvations/6338841578112',
        'info_dict': {
            'id': '6338841578112',
            'ext': 'mp4',
            'title': 'Freed from Resentment Toward God',
            'timestamp': 1761304213,
            'description': 'md5:510a636865b809fc3ae923eaafa017ae',
            'upload_date': '20251024',
            'uploader_id': '734546207001',
            'duration': 355.627,
            'thumbnail': r're:https?://.*\.(jpg|jpeg)',
            'tags': list,
        },
    }]

    def _real_extract(self, url):
        display_id = self._match_id(url)
        return self._extract_brightcove(display_id)

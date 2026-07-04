import pytest
import respx
import httpx

from app.sources.registry import RSSSource, YoutubeSearchSource
from app.sources.rss import RSSCrawler
from app.sources.youtube import YoutubeSearchCrawler

SAMPLE_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Test Feed</title>
    <item>
      <title>Bitcoin hits new high</title>
      <link>https://example.com/article/1</link>
      <guid>https://example.com/article/1</guid>
      <pubDate>Fri, 04 Jul 2025 10:00:00 +0000</pubDate>
      <description>Bitcoin surged past $100k today.</description>
    </item>
  </channel>
</rss>"""

SAMPLE_YT_RESPONSE = {
    "items": [
        {
            "id": {"videoId": "cREz8Pesyxg"},
            "snippet": {
                "title": "PEARL Coin Analysis",
                "description": "Deep dive into PEARL tokenomics.",
                "channelTitle": "CryptoReviews",
                "publishedAt": "2025-07-01T12:00:00Z",
                "thumbnails": {"high": {"url": "https://i.ytimg.com/vi/cREz8Pesyxg/hqdefault.jpg"}},
            },
        }
    ]
}


@pytest.mark.asyncio
@respx.mock
async def test_rss_crawler_parses_items(respx_mock: respx.MockRouter) -> None:
    source = RSSSource(name="TestFeed", url="https://example.com/feed.rss")
    respx_mock.get("https://example.com/feed.rss").mock(
        return_value=httpx.Response(200, text=SAMPLE_RSS)
    )
    crawler = RSSCrawler(source)
    # Just test parsing — don't need a real DB session for unit test
    xml = await crawler._fetch_xml()
    import feedparser
    feed = feedparser.parse(xml)
    assert len(feed.entries) == 1
    assert feed.entries[0].title == "Bitcoin hits new high"


@pytest.mark.asyncio
@respx.mock
async def test_youtube_crawler_builds_correct_url(respx_mock: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.sources.youtube.settings.youtube_api_key", "test-key")
    source = YoutubeSearchSource(name="PEARL coin", query="PEARL coin crypto", coin_tags=["PEARL"])
    respx_mock.get("https://www.googleapis.com/youtube/v3/search").mock(
        return_value=httpx.Response(200, json=SAMPLE_YT_RESPONSE)
    )
    crawler = YoutubeSearchCrawler(source)
    items = await crawler._fetch()
    assert len(items) == 1
    assert items[0]["id"]["videoId"] == "cREz8Pesyxg"

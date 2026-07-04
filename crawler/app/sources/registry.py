from dataclasses import dataclass, field


@dataclass
class YoutubeSearchSource:
    name: str                       # used as source_name in DB and log lines
    query: str                      # YouTube Data API search query
    coin_tags: list[str] = field(default_factory=list)
    channel_id: str | None = None   # if set, restricts search to that channel
    max_results: int = 10
    interval_minutes: int = 60


@dataclass
class RSSSource:
    name: str                       # used as source_name in DB and log lines
    url: str                        # RSS / Atom feed URL
    coin_tags: list[str] = field(default_factory=list)  # empty = general market news
    interval_minutes: int = 30


# ---------------------------------------------------------------------------
# YouTube — known channel IDs
# Use channel_id to pin a source to a specific creator.
# Without channel_id the query searches all of YouTube.
# ---------------------------------------------------------------------------

_COIN_BUREAU     = "UCqK_GSMbpiV8spgD3ZGloSw"
_ALTCOIN_DAILY   = "UCbLhGKVY-bJPcawebgtNfbw"
_INTO_CRYPTOVERSE = "UCRvqjQPSeaWn-uEx-w0XOIg"  # Benjamin Cowen

YOUTUBE_SEARCHES: list[YoutubeSearchSource] = [

    # ── Specific channels ────────────────────────────────────────────────────
    YoutubeSearchSource(
        name="Coin Bureau",
        query="crypto",
        channel_id=_COIN_BUREAU,
        max_results=5,
        interval_minutes=360,
    ),
    YoutubeSearchSource(
        name="Altcoin Daily",
        query="crypto news",
        channel_id=_ALTCOIN_DAILY,
        max_results=5,
        interval_minutes=360,
    ),
    YoutubeSearchSource(
        name="Into The Cryptoverse",
        query="crypto analysis",
        channel_id=_INTO_CRYPTOVERSE,
        max_results=5,
        interval_minutes=360,
    ),

    # ── General topics ────────────────────────────────────────────────────────
    YoutubeSearchSource(
        name="Crypto market overview",
        query="crypto market news today",
        interval_minutes=120,
    ),
    YoutubeSearchSource(
        name="Bitcoin ETF",
        query="Bitcoin ETF news",
        coin_tags=["BTC"],
        interval_minutes=120,
    ),
    YoutubeSearchSource(
        name="Crypto regulation",
        query="crypto regulation SEC CFTC news",
        interval_minutes=120,
    ),
    YoutubeSearchSource(
        name="DeFi news",
        query="DeFi decentralized finance news",
        interval_minutes=120,
    ),
    YoutubeSearchSource(
        name="NFT market",
        query="NFT market news 2025",
        interval_minutes=180,
    ),
    YoutubeSearchSource(
        name="Layer 2 news",
        query="Layer 2 blockchain Ethereum scaling news",
        interval_minutes=120,
    ),
    YoutubeSearchSource(
        name="RWA tokenization",
        query="real world assets RWA tokenization crypto",
        interval_minutes=180,
    ),
    YoutubeSearchSource(
        name="AI crypto tokens",
        query="AI crypto tokens artificial intelligence blockchain",
        interval_minutes=120,
    ),
    YoutubeSearchSource(
        name="Crypto hacks security",
        query="crypto hack exploit DeFi security",
        interval_minutes=60,
    ),
    YoutubeSearchSource(
        name="Stablecoin news",
        query="stablecoin USDC USDT regulation news",
        interval_minutes=180,
    ),
    YoutubeSearchSource(
        name="Crypto whale moves",
        query="crypto whale alert on-chain analysis",
        interval_minutes=120,
    ),

    # ── Layer 1 coins ─────────────────────────────────────────────────────────
    YoutubeSearchSource(name="Bitcoin",       query="Bitcoin BTC news",          coin_tags=["BTC"]),
    YoutubeSearchSource(name="Ethereum",      query="Ethereum ETH news",         coin_tags=["ETH"]),
    YoutubeSearchSource(name="Solana",        query="Solana SOL news",           coin_tags=["SOL"]),
    YoutubeSearchSource(name="BNB",           query="BNB Binance coin news",     coin_tags=["BNB"]),
    YoutubeSearchSource(name="XRP",           query="XRP Ripple news",           coin_tags=["XRP"]),
    YoutubeSearchSource(name="Cardano",       query="Cardano ADA news",          coin_tags=["ADA"]),
    YoutubeSearchSource(name="Avalanche",     query="Avalanche AVAX news",       coin_tags=["AVAX"]),
    YoutubeSearchSource(name="Polkadot",      query="Polkadot DOT news",         coin_tags=["DOT"]),
    YoutubeSearchSource(name="Chainlink",     query="Chainlink LINK news",       coin_tags=["LINK"]),
    YoutubeSearchSource(name="Litecoin",      query="Litecoin LTC news",         coin_tags=["LTC"]),
    YoutubeSearchSource(name="Monero",        query="Monero XMR privacy coin",   coin_tags=["XMR"]),
    YoutubeSearchSource(name="Cosmos",        query="Cosmos ATOM IBC news",      coin_tags=["ATOM"]),
    YoutubeSearchSource(name="NEAR Protocol", query="NEAR Protocol crypto news", coin_tags=["NEAR"]),
    YoutubeSearchSource(name="Hedera",        query="Hedera HBAR news",          coin_tags=["HBAR"]),
    YoutubeSearchSource(name="Internet Computer", query="Internet Computer ICP dfinity", coin_tags=["ICP"]),
    YoutubeSearchSource(name="VeChain",       query="VeChain VET news",          coin_tags=["VET"]),
    YoutubeSearchSource(name="Algorand",      query="Algorand ALGO news",        coin_tags=["ALGO"]),
    YoutubeSearchSource(name="Tezos",         query="Tezos XTZ news",            coin_tags=["XTZ"]),
    YoutubeSearchSource(name="Filecoin",      query="Filecoin FIL storage news", coin_tags=["FIL"]),
    YoutubeSearchSource(name="Kaspa",         query="Kaspa KAS coin news",       coin_tags=["KAS"]),
    YoutubeSearchSource(name="Bittensor",     query="Bittensor TAO AI crypto",   coin_tags=["TAO"]),
    YoutubeSearchSource(name="Stacks",        query="Stacks STX Bitcoin L2",     coin_tags=["STX"]),

    # ── Layer 2 / scaling ────────────────────────────────────────────────────
    YoutubeSearchSource(name="Arbitrum",  query="Arbitrum ARB news",        coin_tags=["ARB"]),
    YoutubeSearchSource(name="Optimism",  query="Optimism OP crypto news",  coin_tags=["OP"]),
    YoutubeSearchSource(name="Polygon",   query="Polygon POL MATIC news",   coin_tags=["POL", "MATIC"]),
    YoutubeSearchSource(name="zkSync",    query="zkSync ZK news",           coin_tags=["ZK"]),
    YoutubeSearchSource(name="StarkNet",  query="StarkNet STRK news",       coin_tags=["STRK"]),
    YoutubeSearchSource(name="Base",      query="Base Coinbase L2 news",    coin_tags=[]),
    YoutubeSearchSource(name="Mantle",    query="Mantle MNT network news",  coin_tags=["MNT"]),

    # ── New / emerging ────────────────────────────────────────────────────────
    YoutubeSearchSource(name="Sui",        query="Sui SUI blockchain news",      coin_tags=["SUI"]),
    YoutubeSearchSource(name="Aptos",      query="Aptos APT blockchain news",    coin_tags=["APT"]),
    YoutubeSearchSource(name="Injective",  query="Injective INJ DeFi news",      coin_tags=["INJ"]),
    YoutubeSearchSource(name="Celestia",   query="Celestia TIA modular blockchain", coin_tags=["TIA"]),
    YoutubeSearchSource(name="Render",     query="Render RNDR GPU crypto",       coin_tags=["RNDR"]),
    YoutubeSearchSource(name="Fetch.ai",   query="Fetch ai FET crypto news",     coin_tags=["FET"]),
    YoutubeSearchSource(name="Worldcoin",  query="Worldcoin WLD news",           coin_tags=["WLD"]),
    YoutubeSearchSource(name="Immutable",  query="Immutable IMX gaming NFT",     coin_tags=["IMX"]),
    YoutubeSearchSource(name="Sei",        query="Sei network SEI news",         coin_tags=["SEI"]),
    YoutubeSearchSource(name="Beam",       query="Beam BEAM gaming blockchain",  coin_tags=["BEAM"]),

    # ── Memecoins ─────────────────────────────────────────────────────────────
    YoutubeSearchSource(name="Dogecoin",   query="Dogecoin DOGE news",        coin_tags=["DOGE"], interval_minutes=120),
    YoutubeSearchSource(name="Shiba Inu",  query="Shiba Inu SHIB news",       coin_tags=["SHIB"], interval_minutes=120),
    YoutubeSearchSource(name="PEPE coin",  query="PEPE meme coin news",       coin_tags=["PEPE"], interval_minutes=120),
    YoutubeSearchSource(name="WIF",        query="dogwifhat WIF Solana meme", coin_tags=["WIF"],  interval_minutes=120),
    YoutubeSearchSource(name="BONK",       query="BONK Solana meme coin",     coin_tags=["BONK"], interval_minutes=120),

    # ── PEARL ─────────────────────────────────────────────────────────────────
    YoutubeSearchSource(
        name="PEARL coin",
        query="PEARL coin crypto",
        coin_tags=["PEARL"],
        interval_minutes=60,
    ),
]


# ---------------------------------------------------------------------------
# RSS feeds
# ---------------------------------------------------------------------------

RSS_FEEDS: list[RSSSource] = [

    # ── Tier 1: High-frequency news outlets ───────────────────────────────────
    RSSSource(name="CoinDesk",      url="https://www.coindesk.com/arc/outboundfeeds/rss/"),
    RSSSource(name="CoinTelegraph", url="https://cointelegraph.com/rss"),
    RSSSource(name="Decrypt",       url="https://decrypt.co/feed"),
    RSSSource(name="The Block",     url="https://www.theblock.co/rss.xml"),
    RSSSource(name="Blockworks",    url="https://blockworks.co/feed"),
    RSSSource(name="CryptoSlate",   url="https://cryptoslate.com/feed/"),
    RSSSource(name="Bitcoinist",    url="https://bitcoinist.com/feed/"),
    RSSSource(name="NewsBTC",       url="https://www.newsbtc.com/feed/"),
    RSSSource(name="AMBCrypto",     url="https://ambcrypto.com/feed/"),
    RSSSource(name="BeInCrypto",    url="https://beincrypto.com/feed/"),
    RSSSource(name="U.Today",       url="https://u.today/rss"),
    RSSSource(name="The Daily Hodl",url="https://dailyhodl.com/feed/"),
    RSSSource(name="CryptoPotato",  url="https://cryptopotato.com/feed/"),
    RSSSource(name="CoinGape",      url="https://coingape.com/feed/"),
    RSSSource(name="Coinpedia",     url="https://coinpedia.org/feed/"),
    RSSSource(name="ZyCrypto",      url="https://zycrypto.com/feed/"),
    RSSSource(name="Crypto Briefing", url="https://cryptobriefing.com/feed/"),
    RSSSource(name="Protos",        url="https://protos.com/feed/"),
    RSSSource(name="WatcherGuru",   url="https://watcher.guru/news/feed"),
    RSSSource(name="CryptoNews",    url="https://cryptonews.com/news/feed/"),
    RSSSource(name="DailyCoin",     url="https://dailycoin.com/feed/"),
    RSSSource(name="99Bitcoins",    url="https://99bitcoins.com/feed/"),

    # ── Tier 2: Analysis & research ───────────────────────────────────────────
    RSSSource(name="Messari",       url="https://messari.io/rss/news.xml",    interval_minutes=60),
    RSSSource(name="Milk Road",     url="https://www.milkroad.com/rss",       interval_minutes=60),
    RSSSource(name="The Defiant",   url="https://thedefiant.io/feed",         interval_minutes=60),
    RSSSource(name="Bankless",      url="https://banklesshq.com/rss",         interval_minutes=120),
    RSSSource(name="Unchained",     url="https://unchainedcrypto.com/feed/",  interval_minutes=120),
    RSSSource(name="Glassnode Insights", url="https://insights.glassnode.com/rss/", interval_minutes=120),
    RSSSource(name="Dune Analytics Blog", url="https://dune.com/blog/rss",   interval_minutes=120),

    # ── Bitcoin focused ───────────────────────────────────────────────────────
    RSSSource(name="Bitcoin Magazine",  url="https://bitcoinmagazine.com/.rss/full/",     coin_tags=["BTC"]),
    RSSSource(name="Bitcoin.com News",  url="https://news.bitcoin.com/feed/",             coin_tags=["BTC"]),
    RSSSource(name="What Bitcoin Did",  url="https://www.whatbitcoindid.com/feed/podcast",coin_tags=["BTC"], interval_minutes=120),

    # ── Protocol / chain official blogs ──────────────────────────────────────
    RSSSource(name="Ethereum Foundation", url="https://blog.ethereum.org/en/feed.xml",  coin_tags=["ETH"], interval_minutes=120),
    RSSSource(name="Vitalik Buterin",     url="https://vitalik.eth.limo/feed.xml",      coin_tags=["ETH"], interval_minutes=360),
    RSSSource(name="Bitcoin.org Blog",    url="https://bitcoin.org/en/rss/blog.rss",    coin_tags=["BTC"], interval_minutes=360),
    RSSSource(name="Solana News",         url="https://solana.com/news/rss.xml",         coin_tags=["SOL"], interval_minutes=120),
    RSSSource(name="Chainlink Blog",      url="https://blog.chain.link/rss/",            coin_tags=["LINK"], interval_minutes=120),
    RSSSource(name="Polygon Blog",        url="https://polygon.technology/blog-feed.xml",coin_tags=["POL", "MATIC"], interval_minutes=120),
    RSSSource(name="Arbitrum Blog",       url="https://arbitrumfoundation.medium.com/feed", coin_tags=["ARB"], interval_minutes=120),
    RSSSource(name="Optimism Blog",       url="https://optimism.mirror.xyz/feed/atom",   coin_tags=["OP"], interval_minutes=120),
    RSSSource(name="Uniswap Blog",        url="https://blog.uniswap.org/rss.xml",        interval_minutes=120),
    RSSSource(name="Aave Blog",           url="https://medium.com/feed/aave",            interval_minutes=120),
    RSSSource(name="MakerDAO Blog",       url="https://medium.com/feed/makerdao",        interval_minutes=120),
    RSSSource(name="Compound Blog",       url="https://medium.com/feed/compound-finance",interval_minutes=120),

    # ── Exchange / infrastructure blogs ──────────────────────────────────────
    RSSSource(name="Coinbase Blog",    url="https://www.coinbase.com/blog/rss",     interval_minutes=120),
    RSSSource(name="Binance Blog",     url="https://www.binance.com/en/feed",       interval_minutes=120),
    RSSSource(name="Kraken Blog",      url="https://blog.kraken.com/feed",          interval_minutes=120),
    RSSSource(name="OKX Insights",     url="https://www.okx.com/learn/rss",         interval_minutes=120),
    RSSSource(name="Ledger Blog",      url="https://www.ledger.com/blog-rss-feed",  interval_minutes=180),

    # ── Mainstream finance (crypto sections) ──────────────────────────────────
    RSSSource(name="Investopedia Crypto", url="https://www.investopedia.com/feeds/news-and-analysis/cryptocurrency.xml", interval_minutes=60),
    RSSSource(name="Forbes Crypto",       url="https://www.forbes.com/crypto-blockchain/feed/",         interval_minutes=60),
    RSSSource(name="TechCrunch Crypto",   url="https://techcrunch.com/category/cryptocurrency/feed/",   interval_minutes=60),
    RSSSource(name="Wired Crypto",        url="https://www.wired.com/feed/category/business/money/cryptocurrency/rss", interval_minutes=60),
    RSSSource(name="Reuters Crypto",      url="https://feeds.reuters.com/reuters/businessNews",          interval_minutes=60),
    RSSSource(name="Financial Times Crypto", url="https://www.ft.com/rss/home/technology",              interval_minutes=60),
]

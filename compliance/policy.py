import re

DISCLAIMER_PATTERNS = [
    re.compile(r"unofficial\s+fan[\s-]*site", re.I),
    re.compile(
        r"not\s+affiliated\s+with\s+(?:or\s+endorsed\s+by\s+)?"
        r"(?:RSI|CIG|Cloud\s+Imperium|Roberts\s+Space\s+Industries)",
        re.I,
    ),
    re.compile(
        r"this\s+(?:is\s+an?\s+)?unofficial.*Star\s+Citizen",
        re.I,
    ),
]

RSI_TRADEMARKS = [
    "star citizen",
    "starcitizen",
    "squadron 42",
    "squadron42",
    "roberts space industries",
    "cloud imperium",
]

REFERRAL_URL_RE = re.compile(
    r"https?://(?:www\.)?robertsspaceindustries\.com/(?:[a-z]{2}/)?enlist\?referral=([A-Z0-9-]+)",
    re.I,
)
RSI_LINK_RE = re.compile(
    r"https?://(?:www\.)?robertsspaceindustries\.com/[^\s\"'<>]*",
    re.I,
)

COMMERCIAL_KEYWORDS = [
    "buy now",
    "purchase here",
    "add to cart",
    "checkout",
    "subscribe for",
    "premium membership",
    "donate to unlock",
    "patreon",
    "ko-fi",
    "buymeacoffee",
]

AD_NETWORK_INDICATORS = [
    "googlesyndication.com",
    "doubleclick.net",
    "adservice.google",
    "googleadservices",
    "amazon-adsystem.com",
    "criteo.net",
    "media.net",
    "adnxs.com",
    "rubiconproject.com",
    "taboola.com",
    "outbrain.com",
]

SQUADRON_42_INDICATORS = [
    "squadron 42",
    "squadron42",
    "sq42",
    "sq.42",
]

# Tokens in a domain name that suggest commercial framing of RSI IP.
COMMERCIAL_DOMAIN_TOKENS = ["buy", "store", "shop", "sell", "market", "cart", "pay"]

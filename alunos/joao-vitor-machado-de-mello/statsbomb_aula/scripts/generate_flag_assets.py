from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


FLAG_SOURCES = {
    "ARG": "ar",
    "AUS": "au",
    "BEL": "be",
    "BRA": "br",
    "CMR": "cm",
    "CAN": "ca",
    "CRC": "cr",
    "CRO": "hr",
    "DEN": "dk",
    "ECU": "ec",
    "ENG": "gb-eng",
    "FRA": "fr",
    "GER": "de",
    "GHA": "gh",
    "IRN": "ir",
    "JPN": "jp",
    "MEX": "mx",
    "MAR": "ma",
    "NED": "nl",
    "POL": "pl",
    "POR": "pt",
    "QAT": "qa",
    "KSA": "sa",
    "SEN": "sn",
    "SRB": "rs",
    "KOR": "kr",
    "ESP": "es",
    "SUI": "ch",
    "TUN": "tn",
    "USA": "us",
    "URU": "uy",
    "WAL": "gb-wls",
}

FALLBACK_COLORS = {
    "ARG": ["#74acdf", "#ffffff", "#74acdf"],
    "AUS": ["#012169", "#ffcd00", "#00843d"],
    "BEL": ["#000000", "#ffd90c", "#ef3340"],
    "BRA": ["#009b3a", "#ffdf00", "#002776"],
    "CMR": ["#007a5e", "#ce1126", "#fcd116"],
    "CAN": ["#ff0000", "#ffffff", "#ff0000"],
    "CRC": ["#002b7f", "#ffffff", "#ce1126"],
    "CRO": ["#ff0000", "#ffffff", "#171796"],
    "DEN": ["#c60c30", "#ffffff", "#c60c30"],
    "ECU": ["#ffdd00", "#034ea2", "#ed1c24"],
    "ENG": ["#ffffff", "#ce1124", "#ffffff"],
    "FRA": ["#0055a4", "#ffffff", "#ef4135"],
    "GER": ["#000000", "#dd0000", "#ffce00"],
    "GHA": ["#ce1126", "#fcd116", "#006b3f"],
    "IRN": ["#239f40", "#ffffff", "#da0000"],
    "JPN": ["#ffffff", "#bc002d", "#ffffff"],
    "MEX": ["#006847", "#ffffff", "#ce1126"],
    "MAR": ["#c1272d", "#006233", "#c1272d"],
    "NED": ["#ae1c28", "#ffffff", "#21468b"],
    "POL": ["#ffffff", "#dc143c"],
    "POR": ["#006600", "#ff0000"],
    "QAT": ["#ffffff", "#8a1538"],
    "KSA": ["#006c35", "#ffffff", "#006c35"],
    "SEN": ["#00853f", "#fdef42", "#e31b23"],
    "SRB": ["#c6363c", "#0c4076", "#ffffff"],
    "KOR": ["#ffffff", "#c60c30", "#003478"],
    "ESP": ["#aa151b", "#f1bf00", "#aa151b"],
    "SUI": ["#ff0000", "#ffffff", "#ff0000"],
    "TUN": ["#e70013", "#ffffff", "#e70013"],
    "USA": ["#b22234", "#ffffff", "#3c3b6e"],
    "URU": ["#ffffff", "#0038a8", "#fcd116"],
    "WAL": ["#ffffff", "#d30731", "#00ad36"],
}


def fallback_svg(code):
    colors = FALLBACK_COLORS[code]
    width = 900 / len(colors)
    stripes = "\n".join(
        f'<rect x="{index * width:.2f}" y="0" width="{width + 0.5:.2f}" height="600" fill="{color}"/>'
        for index, color in enumerate(colors)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" role="img" aria-label="{code}">
<rect width="900" height="600" rx="42" fill="#f7f4ee"/>
{stripes}
<rect x="10" y="10" width="880" height="580" rx="34" fill="none" stroke="rgba(0,0,0,.22)" stroke-width="20"/>
</svg>
"""


def fetch_flag(slug):
    request = Request(
        f"https://flagcdn.com/{slug}.svg",
        headers={"User-Agent": "statsbomb-aula-flag-generator/1.0"},
    )
    with urlopen(request, timeout=20) as response:
        content = response.read().decode("utf-8")
    if "<svg" not in content:
        raise ValueError(f"Invalid SVG content for {slug}")
    return content


def main():
    out_dir = Path(__file__).resolve().parents[1] / "app" / "static" / "flags"
    out_dir.mkdir(parents=True, exist_ok=True)
    for code, slug in FLAG_SOURCES.items():
        try:
            content = fetch_flag(slug)
            source = "FlagCDN"
        except (TimeoutError, URLError, ValueError) as exc:
            content = fallback_svg(code)
            source = f"fallback ({exc})"
        (out_dir / f"{code.lower()}.svg").write_text(content, encoding="utf-8")
        print(f"{code}: {source}")


if __name__ == "__main__":
    main()
